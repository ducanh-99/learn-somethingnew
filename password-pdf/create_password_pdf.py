from typing import Any
import PyPDF2
import csv


def create_password_pdf(input_pdf_file: str, output_pdf_file: str, password: str):
    # Create a PDF object for input file
    pdf = PyPDF2.PdfFileReader(open(input_pdf_file, 'rb'))

    # Create a PDF writer object for the output file
    pdf_writer = PyPDF2.PdfFileWriter()

    # Add pages from the input PDF to the output PDF
    for page_num in range(pdf.numPages):
        page = pdf.getPage(page_num)
        pdf_writer.addPage(page)

    # Encrypt the PDF with the password
    pdf_writer.encrypt(password)

    # Write the encrypted PDF to the output file
    with open(output_pdf_file, 'wb') as output_file:
        pdf_writer.write(output_file)


def read_csv_file_human_management(file_name: str) -> Any:
    pass


if __name__ == "__main__":
    # Input PDF file and password
    input_pdf_file = 'other/input.pdf'
    output_pdf_file = 'other/output.pdf'
    password = 'test'
    print(f'Password-protected PDF created: {output_pdf_file}')
