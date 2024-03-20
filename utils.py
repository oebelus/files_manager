import os
from pypdf import PdfReader

def get_extension(file):
    indexes = []
    count = 0
    for char in file:
        if '.' == char:
            indexes.append(count)
        count+=1
    return file[indexes[-1]:len(file)]

def get_directories(folder_path):
    return [folder for folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, folder))]

def display_directories(directory_array, isPdf):
    count = 1
    for directory in directory_array:
        print(f'({count})> {directory}')
        count += 1
    print('> Enter a number to access the directory')
    print('> Enter (r) to read the file') if isPdf else None
    print('> Enter (.) to save the file here')
    print('> Enter (+) to create a directory')
    print('> Enter (-) to cancel')

def read_file(file_path):
    with open(file_path) as file:
        print(file.readlines())

def check_pdf(file_path):
    return get_extension(file_path) == '.pdf'

def read_pdf(pdf_path, page_number):
    pdf = PdfReader(pdf_path)
    num_of_pages = len(pdf.pages)
    if page_number >= num_of_pages:
        page = pdf.pages[num_of_pages-1]
    elif page_number == 0:
        page = pdf.pages[0]
    else :
        page = pdf.pages[abs(page_number)-1]
    return page.extract_text()
