import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import os
import sys
import shutil
import pydicom

class TextRedirector(object):
    def __init__(self, widget):
        self.widget = widget

    def write(self, message):
        self.widget.insert(tk.END, message)
        self.widget.see(tk.END)  # Auto-scroll to the bottom

    def flush(self):
        pass

def sort_dicom_files(input_path, progress_callback):
    # Dictionary to track series and their files
    # series_dict = {}

    # Define the output path
    output_path = os.path.join(input_path, 'sorted')
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
                # if series_id not in series_dict:
                    # series_dict[series_id] = []
                # series_dict[series_id].append(file_path)

                # Make the full output path for a series
                series_folder = os.path.join(output_path, series_id)
                # Create output directory, if necessary
                if not os.path.exists(series_folder):
                    os.makedirs(series_folder)
                    print(f"Created folder for {series_id}\n")
                shutil.copy(file_path, series_folder)
                print(f"Copied {file_path} to {series_folder}\n")
                progress_callback(file_path)
            except Exception as e:
                print(f"Failed to read {file_path}: {e}")
            

def run_sorting_in_thread(input_path, progress_callback):

    def sorting_task():
            try:
                sort_dicom_files(input_path, progress_callback)
                messagebox.showinfo("Success", "DICOM files sorted successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred:\n{e}")

    sorting_thread = threading.Thread(target=sorting_task)
    sorting_thread.start()

def main():
    root = tk.Tk()
    root.title("DICOM Sorter")
    root.geometry("400x400")  # Width x Height

    # Input Folder
    input_label = tk.Label(root, text="Select Input Folder:")
    input_label.pack(pady=10)

    input_entry = tk.Entry(root, width=50)
    input_entry.pack()

    def browse_input():
        folder_selected = filedialog.askdirectory()
        input_entry.delete(0, tk.END)
        input_entry.insert(0, folder_selected)

    input_button = tk.Button(root, text="Browse", command=browse_input)
    input_button.pack(pady=5)

    # Text Log (multiline text box)
    log_text = tk.Text(root, height=10, width=60)
    log_text.pack(pady=10)

    # Redirect stdout to the Text widget
    sys.stdout = TextRedirector(log_text)

    def progress_callback(current_file):
        log_text.insert(tk.END, f"Processed {current_file}\n")
        log_text.see(tk.END)

    # Run Button
    def run_sorting():
        input_folder = input_entry.get()

        if not input_folder:
            messagebox.showerror("Error", "Please select input folder.")
            return
        
        run_sorting_in_thread(input_folder, progress_callback)

    run_button = tk.Button(root, text="Sort DICOM Files", command=run_sorting, bg="green", fg="white")
    run_button.pack(pady=20)

    

    root.mainloop()




if __name__ == "__main__":
    main()