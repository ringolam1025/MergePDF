# PDF Merger

## Description
PDF Merger is a Python script that merges multiple PDF files into a single PDF file in a specified order. It uses the PyPDF2 library for handling PDF files and the natsort library for sorting files in natural order.

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Install the required libraries using pip:
    ```python
    pip install PyPDF2 natsort
    ```

## Usage
1. Place the PDF files you want to merge into the 'input' folder.
2. Open a terminal (or command prompt) and navigate to the directory containing the 'merge_pdfs.py' script.
3. Run the script by executing the following command:
    ```python
    python merge_pdfs.py
    ```

The script will read the PDF files from the 'input' folder, merge them in natural order, and save the merged file in the current directory with the appropriate name.

## Customizing Output File Name
By default, the output file name will be derived from the first part of the first input file name before the "-" character and will be saved with a '.pdf' extension. If you want to customize the output file name, you can edit the 'merge_pdfs.py' script and modify the 'output_file_name' variable as needed.

## Dependencies
- PyPDF2: A Python library to work with PDF files. It can be installed using 'pip install PyPDF2'.
- natsort: A Python library for natural sorting file names. It can be installed using 'pip install natsort'.

## Compatibility
This script is compatible with Python 3.x.

## License
[MIT License](LICENSE)
