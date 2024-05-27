import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd  # noqa: E402
import os  # noqa: E402
import datetime  # noqa: E402


def generate_file_paths_list(directory) -> list:
    """
    Generate a list of all CSV file paths in the given directory and its subdirectories.
    """
    file_paths = []

    for root, dirs, files in os.walk(directory):
        for file in files:
                file_path = os.path.join(root, file)
                file_paths.append(file_path)

    return file_paths


def fixPotentialAnalysisMethodNameErrors(analysis_method_name:str) -> str:
	""" function to fix stupid oreas database inconsistencies while processing. e.g. having two different analysis methods for '4-acid digest' and '4-acid digestion'."""
	if analysis_method_name == "4-Acid Digest":
		return "4-Acid Digestion"
	elif analysis_method_name == "Aqua Regia Digest":
		return "Aqua Regia Digestion"
	elif analysis_method_name == "Peroxide Fusion ICP*":
		return "Peroxide Fusion ICP"
	elif analysis_method_name == "Sulphuric Acid Leach (5%)":
		return "Sulphuric Acid 5% Leach"
	elif analysis_method_name == "X-ray Photon Assay":
		return "PhotonAssay"
	else: 
		return analysis_method_name

def getCrmIdFromFileName(file_name:str) -> str:
	"""given datapack file name, tries to give oreas CRM id."""
	strlist = file_name.replace("-"," ").split(" ")
	return f'{strlist[0]} {strlist[1]}'


def getIndicativesFromDatapackExcel(file_path:str) -> list[list]:
	"""Given file path to OREAS CRM Datapack XLSX file, returns list of rows for csv output."""
	# Load the Excel file
	# file_path = "OREAS 100a DataPack1.3.xlsx"
	xls = pd.ExcelFile(file_path)

	file_name = os.path.basename(file_path)
	crm_id =  getCrmIdFromFileName(file_name)

	# Load the 'Indicative Values' sheet
	sheet_name = 'Indicative Values'
	df = pd.read_excel(xls, sheet_name=sheet_name)
	# except Exception as e:
	# 	print(f"Error: File '{file_name}' does not have an 'Indicative Values' sheet. Skipping...")
	# 	return pd.DataFrame(columns=['CRM ID','Analysis Method', 'Element', 'Unit', 'Certified Value', '1SD'])
	#print(df)

	# Initialize a list to store the extracted data
	single_crm_data_rows = []

	# Iterate over the rows of the DataFrame
	current_analysis_method = None
	for index, row in df.iterrows():
		# print(f'{index=} : {row.to_list()=}')
		# col 0 should be nan every time. 
		# beginning at row 1, col 1 should be either the analysis method, or an element/compound name. testing if col 2 is nan should reveal if if's an analysis method name or not.
		# then, if element/compound name in col 1, (i.e. col2 is not nan), col 2 should be the unit, and col 3 should be the conc value.
		# same pattern repeats for col 4/5/6 and 7/8/9.
		
		# skip ahead to row 1.
		if index == 0:
			continue
			# move to next row.
		first_position_value = row[1]
		second_position_value = row[2]
		if pd.notna(first_position_value) and pd.isna(second_position_value):
			# found analysis method name row!
			# print(f'analysis method = {first_position_value}')
			current_analysis_method = fixPotentialAnalysisMethodNameErrors(first_position_value)
			# then can skip to next row.
			continue
		for col in range(1, 10, 3):
			if pd.notna(row[col]):
				element = row[col]
				unit = row[col + 1]
				value = row[col + 2]
				# print(f'{element=}')
				# print(f'{unit=}')
				# print(f'{value=}')
				single_crm_data_rows.append([crm_id,current_analysis_method, element, unit, value, 'IND'])

	# Convert the list to a DataFrame
	# output_df = pd.DataFrame(single_crm_data_rows, columns=['CRM ID','Analysis Method', 'Element', 'Unit', 'Certified Value', '1SD'])

	# Save the DataFrame to a CSV file
	# output_csv_path = 'extracted_chemistry_data.csv'
	# output_df.to_csv(mode='x',path_or_buf=output_csv_path, index=False)

	# print(f"Data successfully extracted from {file_name} for CRM {crm_id}.")

	return single_crm_data_rows


def main():
	datapack_dir = 'C:/Users/Zeb/Documents/GitHub/OREAS-Catalogue-Info/oreas_datapacks/'
	datapack_file_list = generate_file_paths_list('C:/Users/Zeb/Documents/GitHub/OREAS-Catalogue-Info/oreas_datapacks/')
	total_file_count = len(datapack_file_list)
	print(f"{total_file_count} files found in {datapack_dir}.")
	combined_crm_data_rows = []

	progress_count = 0
	failed_file_count = 0
	for datapack_path in datapack_file_list:
		try:
			combined_crm_data_rows += getIndicativesFromDatapackExcel(datapack_path)
		except Exception as e:
			print(f"Error: Datapack '{os.path.basename(datapack_path)}'could not be processed correctly. details: ({repr(e)})")
			failed_file_count += 1 
		progress_count += 1
		print(f"Progress: {progress_count} / {total_file_count} ...")


	combined_crm_dataframe = pd.DataFrame(data=combined_crm_data_rows, columns=['CRM ID','Analysis Method', 'Element', 'Unit', 'Certified Value', '1SD'])
	output_csv_path = f'Extracted_Indicative_Data_{datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}.csv'
	combined_crm_dataframe.to_csv(mode='x',path_or_buf=output_csv_path, index=False)

	print(f"Processing Complete. Files Processed successfully: {total_file_count - failed_file_count} / {total_file_count}. ({failed_file_count} failures)")

if __name__ == "__main__":
	main()