# DICOM Sorter

## Description

This is a simple app with a user-friendly interface that is intended to sort DICOM files exported to an external USB drive from the CINL Prisma. After the update to Numaris/X from Numaris/4, the scanner now exports enhanced DICOM files into a flat directory structure. Some people may find it easier to work with DICOM files that are sorted hierarchically into folders by sequence description (i.e. AAHScout, T1w_MPRAGE, etc.). This app copies DICOM files from a flat directory structure into a hierarchical directory structure, where each file is contained in a folder labeled with the DICOM SeriesDescription.

Currently, the standalone application is only available for Windows. Releases for Linux and MacOS are planned for the near future.

If you are interested and savvy, then you can run the Python script in your favorite installation of Python. Check out the [dcmSort.py](dcmSort.py) script to see which dependencies are needed to run it. There is also a CLI script: [dcmSort_cmd.py](dcmSort_cmd.py).

## Installation

DICOM Sorter is a standalone Python application. Simply download the executable file (dcmSort.exe) to your computer (e.g. C:\Users\YourName\Desktop).

## Usage

Open DICOM Sorter by double-clicking on it. A command prompt will appear followed by the Dicom Sorter window. Click Browse under Select Input Folder: and browse to the folder where your DICOM files are stored.

__The DICOM folder is expected to contain many DICOM files with no subfolders.__ When you open the folder in the Select Folder window, it should be blank, indicating that there are only files, and no folders, within the DICOM folder.

After selecting the input folder, the path to your DICOM folder will appear in the window. Click the Sort DICOM Files button to start sorting your DICOMs! Messages about which files are being copied will be printed to the text box in the window. The progress bar will fill up as files are copied.

The 'sorted' folder will be inside your input folder. If you try to sort a folder that contains a folder named 'sorted' you will be warned that your files may already be sorted, and the sorting will not continue.

## License

This project is licensed under the MIT license - see the [LICENSE](LICENSE) file for details.

## Authors and Contributors

Ryan Willoughby (@ryanwillo)

