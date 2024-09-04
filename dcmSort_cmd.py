import os
import shutil
import pydicom

def sort_dicom_files(input_path):
    # Dictionary to track series and their files
    series_dict = {}

    # Loop through each file in the directory
    for filename in os.listdir(input_path):
        file_path = os.path.join(input_path, filename)
        
        # Check if the file is a DICOM file
        if os.path.isfile(file_path) and filename.lower().endswith('.dcm'):
            try:
                # Read the DICOM file
                dicom_file = pydicom.dcmread(file_path, stop_before_pixels=True)
                series_id = dicom_file.SeriesDescription

                # Add file to the series dictionary
                if series_id not in series_dict:
                    series_dict[series_id] = []
                series_dict[series_id].append(file_path)
            except Exception as e:
                print(f"Failed to read {file_path}: {e}")

    # Create output directory, subfolders, and move files
    output_path = os.path.join(input_path, 'sorted')
    for series_id, files in series_dict.items():
        series_folder = os.path.join(output_path, series_id)
        if not os.path.exists(series_folder):
            os.makedirs(series_folder)

        for file in files:
            shutil.copy(file, series_folder)
            print(f"Copied {file} to {series_folder}")

if __name__ == "__main__":
    # Ask the user for the path to the DICOM folder
    folder_path = input("Enter the path to your DICOM folder: ")
    sort_dicom_files(folder_path)