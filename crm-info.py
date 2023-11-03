# oreas catalogue info-grabber
# started 2023/10/02 ZH

versionNum = "v0.0.5"
versionDate = "2023/11/03"

import os
import sys
import re
import pandas as pd
import numpy as np
import chemparse
import json
from collections import Counter
from functools import cache, wraps
from time import time

from analysismethodprefs import analysis_method_prefs_dict as PREFS
from analysismethodprefs import supercrm_list as SUPERCRMS


# for sorting analysis method, USE: 4-Acid Digestion >
# chris has doc: Merging.xlsx G:\.shortcut-targets-by-id\1w2nUsja1tidZ-QYTuemO6DzCaclAmIlm\PXRFS\12. Certified Reference Material\5_CRM Master Spreadsheet\OREAS Sorting
# get Principle cert vals and which are superCRMs from copying search


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print("func:%r args:[%r, %r] took: %2.4f sec" % (f.__name__, args, kw, te - ts))
        return result

    return wrap


class Crm:
    def __init__(
        self,
        crm_id: str,
        crm_group: str,
        crm_type: str,
        crm_matrix: str,
        crm_mineralisation: str,
        crm_status: str,
    ):
        self.id = crm_id
        self.group = crm_group
        self.type = crm_type
        self.matrix = crm_matrix
        self.mineralisation = crm_mineralisation
        self.status = crm_status
        self.supercrm = "yes" if isSuperCRM(crm_id) else "no"
        self.units = "ppm"  # this will be the format it will convert all other units to
        if crm_id.startswith(
            "OREAS "
        ):  # if oreas CRM, format ID to comply with chris' preferred formatting i.e. 'OREAS 100a' -> 'OREAS0100a'
            self.id = format_oreas_crm_id(crm_id)
        self.chemistry = {}

        # print(f'Initialising CRM... {self.id=} {self.group=}, {self.type=}, {self.matrix=}, {self.mineralisation=}, {self.status=}, {self.supercrm=}')

    def addChemistry(
        self, chem_formula, chem_concentration, chem_unit, chem_analysis_method
    ):
        # check formula - attempt conversion
        new_element = getFirstElementOfCompound(chem_formula)
        conv_factor = compoundToElementConversionFactor(chem_formula)
        if conv_factor == 1:
            new_element = chem_formula  # if cannot do stoich, (i.e. invalid symbols), then just resort to compound conc.
        # check unit - convert if necessary ( can just multiply by conv_factor from compound conv. fact)
        conv_factor = conv_factor * getUnitConversionFactor(
            units_from=chem_unit, units_to=self.units
        )
        new_concentration = chem_concentration * conv_factor
        # add to chem dict
        if new_element not in self.chemistry.keys():
            # print(f'adding {new_element} to chemistry dict for {self.id}...')
            self.chemistry[new_element] = {}
        self.chemistry[new_element][chem_analysis_method] = (
            np.round(new_concentration, decimals=0)
            if new_concentration > 20
            else np.round(new_concentration, decimals=3)
        )
        # if len(str(new_concentration)) > 8:
        #     print(f'{self.id}: {new_element} conc: {new_concentration} rounded to {np.round(new_concentration,decimals=0) if new_concentration > 20 else np.round(new_concentration,decimals=3)}')


def isSuperCRM(crm_id: str):
    if crm_id in SUPERCRMS:
        return True
    else:
        return False


def getUnitConversionFactor(units_from: str, units_to: str):
    # returns factor to multiply by to convert from units_from to units_to
    if units_from == "wt.%" or units_from == "wt %":
        units_from = "%"
    if units_to == "wt.%" or units_to == "wt %":
        units_to = "%"

    if units_from == "Unity":
        return 1

    if units_from == units_to:
        return 1
    elif units_from == "ppm" and units_to == "ppb":
        return 1000
    elif units_from == "ppm" and units_to == "%":
        return 1 / 10000
    elif units_from == "ppb" and units_to == "ppm":
        return 1 / 1000
    elif units_from == "ppb" and units_to == "%":
        return 1 / 10000000
    elif units_from == "%" and units_to == "ppm":
        return 10000
    elif units_from == "%" and units_to == "ppb":
        return 10000000
    else:
        raise Exception(
            f"Invalid unit conversion requested! {units_from=}, {units_to=}"
        )


@cache
def format_oreas_crm_id(crm_id: str):
    # Define regex pattern to match desired formatting from chris
    pattern = r"^OREAS (\d+)"

    # use re.sub to apply pattern to crm id strings, and replace space?
    formatted_string = re.sub(
        pattern, lambda match: f"OREAS {match.group(1).zfill(4)}", crm_id
    ).replace(" ", "")

    return formatted_string


@cache
def getFirstElementOfCompound(compound: str):
    eoi_predicted = compound[0]
    strposition = 1
    cont = True
    while cont and (strposition < len(compound)):
        if compound[strposition].isupper():
            # print(f'{compound[strposition]} is upper!')
            cont = False
        elif compound[strposition].isnumeric():
            # print(f'{compound[strposition]} is number!')
            cont = False
        else:
            eoi_predicted += compound[strposition]
        strposition += 1

    return eoi_predicted


@cache
def getFirstElementOfNameAndCompound(nameandcompound: str):
    """for oreas catalogue 'Element' column. e.g. input: 'Iron(III) oxide, Fe2O3' -> 'Fe'."""
    if ", " not in nameandcompound:
        print(f"no comma in {nameandcompound}!!")
        raise Exception
    compound = nameandcompound.split(", ")[1]

    element_symbol_matchstrs = [
        "H",
        "He",
        "Li",
        "Be",
        "B",
        "C",
        "N",
        "O",
        "F",
        "Ne",
        "Na",
        "Mg",
        "Al",
        "Si",
        "P",
        "S",
        "Cl",
        "Ar",
        "K",
        "Ca",
        "Sc",
        "Ti",
        "V",
        "Cr",
        "Mn",
        "Fe",
        "Co",
        "Ni",
        "Cu",
        "Zn",
        "Ga",
        "Ge",
        "As",
        "Se",
        "Br",
        "Kr",
        "Rb",
        "Sr",
        "Y",
        "Zr",
        "Nb",
        "Mo",
        "Tc",
        "Ru",
        "Rh",
        "Pd",
        "Ag",
        "Cd",
        "In",
        "Sn",
        "Sb",
        "Te",
        "I",
        "Xe",
        "Cs",
        "Ba",
        "La",
        "Ce",
        "Pr",
        "Nd",
        "Pm",
        "Sm",
        "Eu",
        "Gd",
        "Tb",
        "Dy",
        "Ho",
        "Er",
        "Tm",
        "Yb",
        "Lu",
        "Hf",
        "Ta",
        "W",
        "Re",
        "Os",
        "Ir",
        "Pt",
        "Au",
        "Hg",
        "Tl",
        "Pb",
        "Bi",
        "Po",
        "At",
        "Rn",
        "Fr",
        "Ra",
        "Ac",
        "Th",
        "Pa",
        "U",
        "Np",
        "Pu",
        "Am",
        "Cm",
        "Bk",
        "Cf",
        "Es",
        "Fm",
        "Md",
        "No",
        "Lr",
        "Rf",
        "Db",
        "Sg",
        "Bh",
        "Hs",
        "Mt",
        "Ds",
        "Rg",
        "Cn",
        "Nh",
        "Fl",
        "Mc",
        "Lv",
        "Ts",
        "Og",
    ]
    elementsymbol = getFirstElementOfCompound(compound)
    if elementsymbol in element_symbol_matchstrs:
        return elementsymbol
    else:
        return compound


def compoundToElementConversionFactor(compound: str, element_of_interest: str = ""):
    """Returns the conversion factor to apply to a compound concentration to get the
    concentration of the element of interest (eoi), given the compound and eoi as strs.
    e.g. given 'Al2O3' and 'Al', returns 0.529251.
    If no eoi is given, will assume the first element symbol found in the compound str is the eoi.
    """

    def shouldAttemptStoichConversion(stoich_dict: dict):
        element_symbol_matchstrs = [
            "H",
            "He",
            "Li",
            "Be",
            "B",
            "C",
            "N",
            "O",
            "F",
            "Ne",
            "Na",
            "Mg",
            "Al",
            "Si",
            "P",
            "S",
            "Cl",
            "Ar",
            "K",
            "Ca",
            "Sc",
            "Ti",
            "V",
            "Cr",
            "Mn",
            "Fe",
            "Co",
            "Ni",
            "Cu",
            "Zn",
            "Ga",
            "Ge",
            "As",
            "Se",
            "Br",
            "Kr",
            "Rb",
            "Sr",
            "Y",
            "Zr",
            "Nb",
            "Mo",
            "Tc",
            "Ru",
            "Rh",
            "Pd",
            "Ag",
            "Cd",
            "In",
            "Sn",
            "Sb",
            "Te",
            "I",
            "Xe",
            "Cs",
            "Ba",
            "La",
            "Ce",
            "Pr",
            "Nd",
            "Pm",
            "Sm",
            "Eu",
            "Gd",
            "Tb",
            "Dy",
            "Ho",
            "Er",
            "Tm",
            "Yb",
            "Lu",
            "Hf",
            "Ta",
            "W",
            "Re",
            "Os",
            "Ir",
            "Pt",
            "Au",
            "Hg",
            "Tl",
            "Pb",
            "Bi",
            "Po",
            "At",
            "Rn",
            "Fr",
            "Ra",
            "Ac",
            "Th",
            "Pa",
            "U",
            "Np",
            "Pu",
            "Am",
            "Cm",
            "Bk",
            "Cf",
            "Es",
            "Fm",
            "Md",
            "No",
            "Lr",
            "Rf",
            "Db",
            "Sg",
            "Bh",
            "Hs",
            "Mt",
            "Ds",
            "Rg",
            "Cn",
            "Nh",
            "Fl",
            "Mc",
            "Lv",
            "Ts",
            "Og",
        ]
        if not stoich_dict:  # if stoich dict is empty
            return False
        for key in stoich_dict.keys():
            if key not in element_symbol_matchstrs:
                return False
        return True

    compound_stoich_dict = {}
    compound_stoich_dict = chemparse.parse_formula(
        compound
    )  # returns e.g. {'Al': 2, 'O': 3} from 'Al2O3'
    if not shouldAttemptStoichConversion(compound_stoich_dict):
        return 1

    if element_of_interest == "":
        element_of_interest = getFirstElementOfCompound(compound)

    compound_mass = 0
    eoi_mass_single = 0
    eoi_mass = 0

    masses = {
        "H": 1.00794,
        "He": 4.002602,
        "Li": 6.941,
        "Be": 9.012182,
        "B": 10.811,
        "C": 12.0107,
        "N": 14.0067,
        "O": 15.9994,
        "F": 18.9984032,
        "Ne": 20.1797,
        "Na": 22.98976928,
        "Mg": 24.305,
        "Al": 26.9815386,
        "Si": 28.0855,
        "P": 30.973762,
        "S": 32.065,
        "Cl": 35.453,
        "Ar": 39.948,
        "K": 39.0983,
        "Ca": 40.078,
        "Sc": 44.955912,
        "Ti": 47.867,
        "V": 50.9415,
        "Cr": 51.9961,
        "Mn": 54.938045,
        "Fe": 55.845,
        "Co": 58.933195,
        "Ni": 58.6934,
        "Cu": 63.546,
        "Zn": 65.409,
        "Ga": 69.723,
        "Ge": 72.64,
        "As": 74.9216,
        "Se": 78.96,
        "Br": 79.904,
        "Kr": 83.798,
        "Rb": 85.4678,
        "Sr": 87.62,
        "Y": 88.90585,
        "Zr": 91.224,
        "Nb": 92.90638,
        "Mo": 95.94,
        "Tc": 98.9063,
        "Ru": 101.07,
        "Rh": 102.9055,
        "Pd": 106.42,
        "Ag": 107.8682,
        "Cd": 112.411,
        "In": 114.818,
        "Sn": 118.71,
        "Sb": 121.760,
        "Te": 127.6,
        "I": 126.90447,
        "Xe": 131.293,
        "Cs": 132.9054519,
        "Ba": 137.327,
        "La": 138.90547,
        "Ce": 140.116,
        "Pr": 140.90465,
        "Nd": 144.242,
        "Pm": 146.9151,
        "Sm": 150.36,
        "Eu": 151.964,
        "Gd": 157.25,
        "Tb": 158.92535,
        "Dy": 162.5,
        "Ho": 164.93032,
        "Er": 167.259,
        "Tm": 168.93421,
        "Yb": 173.04,
        "Lu": 174.967,
        "Hf": 178.49,
        "Ta": 180.9479,
        "W": 183.84,
        "Re": 186.207,
        "Os": 190.23,
        "Ir": 192.217,
        "Pt": 195.084,
        "Au": 196.966569,
        "Hg": 200.59,
        "Tl": 204.3833,
        "Pb": 207.2,
        "Bi": 208.9804,
        "Po": 208.9824,
        "At": 209.9871,
        "Rn": 222.0176,
        "Fr": 223.0197,
        "Ra": 226.0254,
        "Ac": 227.0278,
        "Th": 232.03806,
        "Pa": 231.03588,
        "U": 238.02891,
        "Np": 237.0482,
        "Pu": 244.0642,
        "Am": 243.0614,
        "Cm": 247.0703,
        "Bk": 247.0703,
        "Cf": 251.0796,
        "Es": 252.0829,
        "Fm": 257.0951,
        "Md": 258.0951,
        "No": 259.1009,
        "Lr": 262,
        "Rf": 267,
        "Db": 268,
        "Sg": 271,
        "Bh": 270,
        "Hs": 269,
        "Mt": 278,
        "Ds": 281,
        "Rg": 281,
        "Cn": 285,
        "Nh": 284,
        "Fl": 289,
        "Mc": 289,
        "Lv": 292,
        "Ts": 294,
        "Og": 294,
    }

    try:
        eoi_mass_single = masses[element_of_interest]
    except KeyError:
        print(
            f"Error: Supplied Element of Interest ({element_of_interest}) for compound ({compound}) not found in molecular mass dictionary"
        )
        return 1

    # Calculate actual EOI mass in case of multiple stoich of EOI in compound (e.g. Al2O3)
    try:
        eoi_mass = (
            eoi_mass_single * compound_stoich_dict[element_of_interest]
        )  # e.g. 26.9815386 * 2 = 53.9630772
    except KeyError:
        print(
            f"Error: Supplied Element of Interest ({element_of_interest}) not found in compound ({compound})"
        )
        return 1

    for element, quantity in compound_stoich_dict.items():
        try:
            compound_mass += masses[element] * quantity
        except KeyError:
            (
                f"Error: Element ({element}) in Compound ({compound}) not found in molecular mass dictionary"
            )
            return 1

    return eoi_mass / compound_mass


def countAnalysisMethodsForElement(catdf: pd.DataFrame, element: str):
    """pass oreas catalogue dataframe and element of interest. recv counter object for analysis methods for that element."""
    copydf = catdf.copy()
    print(copydf)
    # copydf.set_index('Element', inplace=True)
    # copydf = copydf.filter(like=element,axis=0)
    copydf = copydf[copydf["Element Symbol"] == element]
    print(copydf)
    method_counter = Counter(copydf["Analysis Method"].tolist())
    return method_counter


@timing
def main():
    # open oreas catalogue as csv, convert to dataframe
    catalogue_path = "oreas-catalogue-2023-11-03.csv"
    cat_df = pd.read_csv(catalogue_path)

    # add element symbol only AND superCRM columns
    cat_df["Element Symbol"] = cat_df["Element"].apply(getFirstElementOfNameAndCompound)
    cat_df["SuperCRM"] = cat_df["CRM ID"].apply(isSuperCRM)
    # print(cat_df)
    # cat_df.to_csv('output.csv')
    # print(countAnalysisMethodsForElement(cat_df,'U'))

    # initially process CRMs from catalogue into Crm class objects
    crm_ids_seen = set([])
    crms = []
    for i in cat_df.index:
        id = cat_df["CRM ID"][i]
        # if crm id not seen before, then make new instance of CRM class
        if id not in crm_ids_seen:
            if crm_ids_seen:  # if ids seen list is NOT empty
                crms.append(currentcrm)
                # append currentCRM to list unless it's the first crm (list will be empty)
            crm_ids_seen.add(id)
            currentcrm = Crm(
                crm_id=id,
                crm_group=cat_df["CRM Group"][i],
                crm_type=cat_df["CRM Type"][i],
                crm_matrix=cat_df["Matrix"][i],
                crm_mineralisation=cat_df["Mineralisation Style"][i],
                crm_status=cat_df["Status"][i],
            )
        # add data to crm
        formula = cat_df["Element"][i]
        if ", " in formula:
            formula = formula.split(", ")[1]
        # check if value is INDICATIVE, (also e.g.<2ppm) - if so, DO NOT USE
        if cat_df["1SD"][i] != "IND":
            currentcrm.addChemistry(
                chem_formula=formula,
                chem_concentration=cat_df["Certified Value"][i],
                chem_unit=cat_df["Unit"][i],
                chem_analysis_method=cat_df["Analysis Method"][i],
            )
    crms.append(currentcrm)  # for the last on the list!

    crms_total_amount = len(crm_ids_seen)
    print(f"Total of {crms_total_amount} CRMs found in catalogue.")

    new_df = pd.DataFrame(
        columns=[
            "ID",
            "Group",
            "Type",
            "Matrix",
            "Mineralisation Style",
            "SuperCRM",
            "Status",
            "Catalogue File Name",
            "Ag",
            "Ag Method",
            "Al",
            "Al Method",
            "As",
            "As Method",
            "Au",
            "Au Method",
            "B",
            "B Method",
            "Ba",
            "Ba Method",
            "Be",
            "Be Method",
            "Bi",
            "Bi Method",
            "Ca",
            "Ca Method",
            "Cd",
            "Cd Method",
            "Ce",
            "Ce Method",
            "Cl",
            "Cl Method",
            "Co",
            "Co Method",
            "Cr",
            "Cr Method",
            "Cs",
            "Cs Method",
            "Cu",
            "Cu Method",
            "Dy",
            "Dy Method",
            "Er",
            "Er Method",
            "Eu",
            "Eu Method",
            "Fe",
            "Fe Method",
            "Ga",
            "Ga Method",
            "Gd",
            "Gd Method",
            "Ge",
            "Ge Method",
            "Hf",
            "Hf Method",
            "Hg",
            "Hg Method",
            "Ho",
            "Ho Method",
            "In",
            "In Method",
            "Ir",
            "Ir Method",
            "K",
            "K Method",
            "La",
            "La Method",
            "Li",
            "Li Method",
            "Lu",
            "Lu Method",
            "Mg",
            "Mg Method",
            "Mn",
            "Mn Method",
            "Mo",
            "Mo Method",
            "Na",
            "Na Method",
            "Nb",
            "Nb Method",
            "Nd",
            "Nd Method",
            "Ni",
            "Ni Method",
            "P",
            "P Method",
            "Pb",
            "Pb Method",
            "Pd",
            "Pd Method",
            "Pr",
            "Pr Method",
            "Pt",
            "Pt Method",
            "Rb",
            "Rb Method",
            "Re",
            "Re Method",
            "Rh",
            "Rh Method",
            "Ru",
            "Ru Method",
            "S",
            "S Method",
            "Sb",
            "Sb Method",
            "Sc",
            "Sc Method",
            "Se",
            "Se Method",
            "Si",
            "Si Method",
            "Sm",
            "Sm Method",
            "Sn",
            "Sn Method",
            "Sr",
            "Sr Method",
            "Ta",
            "Ta Method",
            "Tb",
            "Tb Method",
            "Te",
            "Te Method",
            "Th",
            "Th Method",
            "Ti",
            "Ti Method",
            "Tl",
            "Tl Method",
            "Tm",
            "Tm Method",
            "U",
            "U Method",
            "V",
            "V Method",
            "W",
            "W Method",
            "Y",
            "Y Method",
            "Yb",
            "Yb Method",
            "Zn",
            "Zn Method",
            "Zr",
            "Zr Method",
        ]
    )
    conc = 0
    statusi = 0
    for crm in crms:
        statusi += 1
        print(f"Processing CRM Data... [{str(statusi).zfill(3)}/{crms_total_amount}]")
        crm_row_dict = {}
        crm_row_dict["ID"] = crm.id
        crm_row_dict["Group"] = crm.group
        crm_row_dict["Type"] = crm.type
        crm_row_dict["Matrix"] = crm.matrix
        crm_row_dict["Mineralisation Style"] = crm.mineralisation
        crm_row_dict["SuperCRM"] = crm.supercrm
        crm_row_dict["Status"] = crm.status
        crm_row_dict["Catalogue File Name"] = catalogue_path
        # print(crm.chemistry)
        for element, method_conc_dict in crm.chemistry.items():
            if element not in PREFS:
                continue
            for pref_method in PREFS[element]:
                if pref_method not in method_conc_dict:
                    continue
                else:
                    # ADD CONCENTRATION FOR THAT ELEMENT: column title is element name = concentration value in dict for that method
                    crm_row_dict[str(element)] = method_conc_dict[str(pref_method)]
                    # ADD METHOD TO METHOD COLUMN FOR THAT ELEMENT.
                    crm_row_dict[f"{element} Method"] = pref_method
                    break
        # print(crm_row_dict)
        new_row_df = pd.DataFrame(data=crm_row_dict, index=[0])
        new_df = pd.concat([new_df, new_row_df])

    # print(new_df)
    new_df.to_csv("output_processed.csv", index=False)
    print(
        f"Processed data output to CSV. rows={new_df.shape[0]}, cols={new_df.shape[1]}"
    )

    # # output data to txt for testing
    # with open('output.txt',mode='w') as f:
    #     for crm in crms:
    #         f.write(f'start of {crm.id} chemistry:\n')
    #         f.write(json.dumps(crm.chemistry))
    #         f.write(f'\nend of {crm.id} chemistry.\n\n\n')

    # # find list of unique entries in given col
    # unique_methods_list = set(cat_df['Analysis Method'].tolist())
    # methods_counter = Counter(cat_df['Analysis Method'].tolist())
    # print(unique_methods_list)
    # print(f'NUMBER OF UNIQUE METHODS: {len(unique_methods_list)}')
    # print(methods_counter)

    # unique_compound_list = set(catalogue_df['Element'].tolist())
    # print(unique_compound_list)
    # print(f'NUMBER OF UNIQUE COMPOUNDS: {len(unique_compound_list)}')
    # unique_compound_formulas_list_all = []
    # for compound in unique_compound_list:
    #     if ', ' in compound:
    #         unique_compound_formulas_list_all.append(compound.split(', ')[1])
    #         stoich_dict = chemparse.parse_formula(compound.split(', ')[1])
    #         print(stoich_dict)
    # unique_compound_formulas = set(unique_compound_formulas_list_all)
    # print(unique_compound_formulas)
    # print(f'NUMBER OF UNIQUE COMPOUND FORMULAS: {len(unique_compound_formulas)}')

    # for i in catalogue_df.index:


if __name__ == "__main__":
    main()
