import os
import PyPDF2
from natsort import natsorted

def merge_pdfs(input_folder):
    pdf_merger = PyPDF2.PdfMerger()

    pdf_files = natsorted(os.listdir(input_folder))
    for filename in pdf_files:
        if filename.endswith('.pdf'):
            file_path = os.path.join(input_folder, filename)
            with open(file_path, 'rb') as pdf_file:
                pdf_merger.append(pdf_file)

    # Determine the output file name based on the first part of the input file name before "-"
    output_file_name = pdf_files[0].split('-')[0] + ".pdf"

    with open(output_file_name, 'wb') as merged_pdf:
        pdf_merger.write(merged_pdf)

    print("PDF files have been merged successfully!")

# Example usage:
input_folder = 'input'  # Replace 'input' with the actual folder path containing the PDF files

merge_pdfs(input_folder)
