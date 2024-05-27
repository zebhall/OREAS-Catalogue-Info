# analysis method prefs for preferentially parsing oreas catalogue.
# last updated ZH 20240524

# all assay methods as of 20231012:
#  '4-Acid Digestion'
#  '3-Acid Digestion (no HF)'
#  'Acid Digestion (no HF)'
#  'Pb Fire Assay'
#  'NiS Fire Assay'
#  'Pb Fire Assay (Grav)'
#  'Pb/NiS Fire Assay'
#  'Pb Fire Assay (full corrections)'
#  'Borate Fusion XRF'
#  'Oxidising Fusion XRF'
#  'Pressed Powder Pellet XRF'
#  'Borate / Peroxide Fusion ICP'
#  'Peroxide Fusion ICP'
#  'Aqua Regia Digestion'
#  'Aqua Regia Digestion (sample weights 0.15-50g)'
#  'Aqua Regia Digestion (sample weights 10-50g)'
#  'Infrared Combustion'
#  'Thermogravimetry'
#  'Cyanide Leach'
#  'Gas / Liquid Pycnometry'
#  'Sulphuric Acid 5% Leach'
#  'PhotonAssay'
#  'Classical Wet Chemistry'
#  'Sulphuric Acid 10% Leach'
#  'Acid Digestion Titration'
#  'Satmagan 135'
#  'Davis Tube Recovery'
#  'Miscellaneous Assay Methods'

all_analysis_methods = [
    "4-Acid Digestion",
    "3-Acid Digestion (no HF)",
    "Acid Digestion (no HF)",
    "Pb Fire Assay",
    "NiS Fire Assay",
    "Pb Fire Assay (Grav)",
    "Pb/NiS Fire Assay",
    "Pb Fire Assay (full corrections)",
    "Borate Fusion XRF",
    "Oxidising Fusion XRF",
    "Pressed Powder Pellet XRF",
    "Borate / Peroxide Fusion ICP",
    "Peroxide Fusion ICP",
    "Aqua Regia Digestion",
    "Aqua Regia Digestion (sample weights 0.15-50g)",
    "Aqua Regia Digestion (sample weights 10-50g)",
    "Infrared Combustion",
    "Thermogravimetry",
    "Cyanide Leach",
    "Gas / Liquid Pycnometry",
    "Sulphuric Acid 5% Leach",
    "PhotonAssay",
    "Classical Wet Chemistry",
    "Sulphuric Acid 10% Leach",
    "Acid Digestion Titration",
    "Satmagan 135",
    "Davis Tube Recovery",
    "Miscellaneous Assay Methods",
	"Acid Leach",
	"Alkaline Leach",
	"Aqua Regia Digestion (sample weights 0.15-1.0g)",
	"Borate Fusion ICP",
	"Coulometry",
	"Fire Assay",
	"Fusion ICP",
	"Fusion X-Ray Fluorescence",
	"Instrumental Neutron Activation Analysis",
	"Ion Selective Electrode",
	"Laser Ablation ICP-MS",
	"Partial Digestion",
	"Proximate Analysis",
]


# set up dict of preferred analysis methods for each element - format: (key)*Element*: (value)[*1st pref*, *2nd pref*, *3rd pref*,...]
analysis_method_prefs_dict = {
    "Ag": [
        "Pb Fire Assay",
        "NiS Fire Assay",
        "Pb Fire Assay (Grav)",
        "Pb/NiS Fire Assay",
        "Pb Fire Assay (full corrections)",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
    ],
    "Al": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "As": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Au": [
        "Pb Fire Assay",
        "NiS Fire Assay",
        "Pb Fire Assay (Grav)",
        "Pb/NiS Fire Assay",
        "Pb Fire Assay (full corrections)",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "B": [
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Ba": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Be": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Bi": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Ca": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Cd": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Ce": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Cl": [
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
    ],
    "Co": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF" "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
    ],
    "Cr": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Cs": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Cu": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Dy": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Er": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Eu": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Fe": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Ga": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Peroxide Fusion ICP",
        "Borate / Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Gd": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Peroxide Fusion ICP",
        "Borate / Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Ge": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Peroxide Fusion ICP",
        "Borate / Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Hf": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Peroxide Fusion ICP",
        "Borate / Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Hg": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Ho": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Peroxide Fusion ICP",
        "Borate / Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "In": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Peroxide Fusion ICP",
        "Borate / Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Ir": [
        "Pb Fire Assay",
        "NiS Fire Assay",
        "Pb Fire Assay (Grav)",
        "Pb/NiS Fire Assay",
        "Pb Fire Assay (full corrections)",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "K": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate / Peroxide Fusion ICP",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "La": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate / Peroxide Fusion ICP",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Li": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Peroxide Fusion ICP",
        "Borate / Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Lu": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Peroxide Fusion ICP",
        "Borate / Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Mg": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate / Peroxide Fusion ICP",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Mn": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate / Peroxide Fusion ICP",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Mo": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Peroxide Fusion ICP",
        "Borate / Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Na": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Nb": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate / Peroxide Fusion ICP",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Nd": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Ni": [
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "P": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Pb": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Pd": [
        "Pb Fire Assay",
        "NiS Fire Assay",
        "Pb Fire Assay (Grav)",
        "Pb/NiS Fire Assay",
        "Pb Fire Assay (full corrections)",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Pr": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Pt": [
        "Pb Fire Assay",
        "NiS Fire Assay",
        "Pb Fire Assay (Grav)",
        "Pb/NiS Fire Assay",
        "Pb Fire Assay (full corrections)",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Rb": [
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Re": [
        "Pb Fire Assay",
        "NiS Fire Assay",
        "Pb Fire Assay (Grav)",
        "Pb/NiS Fire Assay",
        "Pb Fire Assay (full corrections)",
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Rh": [
        "Pb Fire Assay",
        "NiS Fire Assay",
        "Pb Fire Assay (Grav)",
        "Pb/NiS Fire Assay",
        "Pb Fire Assay (full corrections)",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Ru": [
        "Pb Fire Assay",
        "NiS Fire Assay",
        "Pb Fire Assay (Grav)",
        "Pb/NiS Fire Assay",
        "Pb Fire Assay (full corrections)",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "S": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Sb": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Sc": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Se": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Si": [
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
    ],
    "Sm": [
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Sn": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
        "Borate / Peroxide Fusion ICP",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Peroxide Fusion ICP",
    ],
    "Sr": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Ta": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
    ],
    "Tb": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Te": [
        "Peroxide Fusion ICP",
        "Borate / Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Th": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Ti": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Tl": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Tm": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "U": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "V": [
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "W": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Y": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Yb": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Zn": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate Fusion XRF",
        "Oxidising Fusion XRF",
        "Pressed Powder Pellet XRF",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
        "Aqua Regia Digestion",
        "Aqua Regia Digestion (sample weights 0.15-50g)",
        "Aqua Regia Digestion (sample weights 10-50g)",
    ],
    "Zr": [
        "4-Acid Digestion",
        "3-Acid Digestion (no HF)",
        "Acid Digestion (no HF)",
        "Borate / Peroxide Fusion ICP",
        "Peroxide Fusion ICP",
    ],
}

# superCRM list last updated 2023/11/03.
supercrm_list = set(
    [
        "OREAS 20a",
        "OREAS 20b",
        "OREAS 24b",
        "OREAS 25a",
        "OREAS 25b",
        "OREAS 30a",
        "OREAS 45d",
        "OREAS 45e",
        "OREAS 45f",
        "OREAS 45h",
        "OREAS 46",
        "OREAS 47",
        "OREAS 60d",
        "OREAS 60e",
        "OREAS 61f",
        "OREAS 61h",
        "OREAS 62f",
        "OREAS 62h",
        "OREAS 70b",
        "OREAS 72b",
        "OREAS 73b",
        "OREAS 74b",
        "OREAS 75b",
        "OREAS 76b",
        "OREAS 77b",
        "OREAS 85",
        "OREAS 86",
        "OREAS 120",
        "OREAS 121",
        "OREAS 122",
        "OREAS 123",
        "OREAS 124",
        "OREAS 130",
        "OREAS 135",
        "OREAS 135b",
        "OREAS 136",
        "OREAS 137",
        "OREAS 138",
        "OREAS 139",
        "OREAS 147",
        "OREAS 148",
        "OREAS 149",
        "OREAS 151b",
        "OREAS 151c",
        "OREAS 152b",
        "OREAS 152c",
        "OREAS 153b",
        "OREAS 153c",
        "OREAS 173",
        "OREAS 174",
        "OREAS 175",
        "OREAS 211",
        "OREAS 230",
        "OREAS 231b",
        "OREAS 232b",
        "OREAS 233",
        "OREAS 233b",
        "OREAS 234",
        "OREAS 234b",
        "OREAS 235b",
        "OREAS 236",
        "OREAS 237b",
        "OREAS 238b",
        "OREAS 239b",
        "OREAS 240",
        "OREAS 240b",
        "OREAS 241",
        "OREAS 241b",
        "OREAS 242",
        "OREAS 243",
        "OREAS 250b",
        "OREAS 250c",
        "OREAS 251b",
        "OREAS 252b",
        "OREAS 252c",
        "OREAS 253b",
        "OREAS 254c",
        "OREAS 255b",
        "OREAS 255c",
        "OREAS 256b",
        "OREAS 258",
        "OREAS 262b",
        "OREAS 264",
        "OREAS 266",
        "OREAS 273",
        "OREAS 282",
        "OREAS 284",
        "OREAS 285",
        "OREAS 286",
        "OREAS 287",
        "OREAS 288",
        "OREAS 289",
        "OREAS 290",
        "OREAS 291",
        "OREAS 292",
        "OREAS 293",
        "OREAS 294",
        "OREAS 295",
        "OREAS 296",
        "OREAS 297",
        "OREAS 298",
        "OREAS 299",
        "OREAS 315",
        "OREAS 316",
        "OREAS 317",
        "OREAS 353",
        "OREAS 353b",
        "OREAS 460",
        "OREAS 461",
        "OREAS 462",
        "OREAS 463",
        "OREAS 464",
        "OREAS 465",
        "OREAS 501b",
        "OREAS 501c",
        "OREAS 501d",
        "OREAS 501e",
        "OREAS 502b",
        "OREAS 502c",
        "OREAS 502d",
        "OREAS 503b",
        "OREAS 503c",
        "OREAS 503d",
        "OREAS 503e",
        "OREAS 504b",
        "OREAS 504c",
        "OREAS 504d",
        "OREAS 505",
        "OREAS 505b",
        "OREAS 506",
        "OREAS 506b",
        "OREAS 507",
        "OREAS 507b",
        "OREAS 508",
        "OREAS 520",
        "OREAS 520c",
        "OREAS 521",
        "OREAS 522",
        "OREAS 523",
        "OREAS 523b",
        "OREAS 524",
        "OREAS 525",
        "OREAS 550",
        "OREAS 551",
        "OREAS 552",
        "OREAS 552b",
        "OREAS 553",
        "OREAS 554",
        "OREAS 554b",
        "OREAS 555",
        "OREAS 555b",
        "OREAS 556",
        "OREAS 556b",
        "OREAS 600",
        "OREAS 600b",
        "OREAS 600c",
        "OREAS 601",
        "OREAS 601b",
        "OREAS 601c",
        "OREAS 602",
        "OREAS 602b",
        "OREAS 603",
        "OREAS 603b",
        "OREAS 603c",
        "OREAS 604",
        "OREAS 604b",
        "OREAS 605",
        "OREAS 605b",
        "OREAS 606",
        "OREAS 606b",
        "OREAS 607",
        "OREAS 607b",
        "OREAS 607c",
        "OREAS 608",
        "OREAS 608b",
        "OREAS 609",
        "OREAS 609b",
        "OREAS 609c",
        "OREAS 610",
        "OREAS 610b",
        "OREAS 611",
        "OREAS 611b",
        "OREAS 620",
        "OREAS 621",
        "OREAS 622",
        "OREAS 623",
        "OREAS 624",
        "OREAS 625",
        "OREAS 626",
        "OREAS 627",
        "OREAS 628",
        "OREAS 629",
        "OREAS 630",
        "OREAS 630b",
        "OREAS 680",
        "OREAS 681",
        "OREAS 682",
        "OREAS 683",
        "OREAS 684",
        "OREAS 700",
        "OREAS 701",
        "OREAS 750",
        "OREAS 751",
        "OREAS 752",
        "OREAS 753",
        "OREAS 901",
        "OREAS 902",
        "OREAS 903",
        "OREAS 904",
        "OREAS 905",
        "OREAS 905b",
        "OREAS 906",
        "OREAS 906b",
        "OREAS 907",
        "OREAS 907b",
        "OREAS 908",
        "OREAS 908b",
        "OREAS 920",
        "OREAS 920b",
        "OREAS 921",
        "OREAS 921b",
        "OREAS 922",
        "OREAS 923",
        "OREAS 924",
        "OREAS 925",
        "OREAS 926",
        "OREAS 927",
        "OREAS 928",
        "OREAS 929",
        "OREAS 930",
        "OREAS 931",
        "OREAS 931b",
        "OREAS 932",
        "OREAS 932b",
        "OREAS 933",
        "OREAS 934",
        "OREAS 935",
        "OREAS 990b",
        "OREAS 990c",
        "OREAS 992b",
        "OREAS 993",
        "OREAS 994",
        "OREAS 995",
        "OREAS 999",
    ]
)
