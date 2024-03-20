import os
import shutil
from utils import get_extension, get_directories, display_directories, read_pdf, check_pdf

files_directory = input("Enter your files directory: ")
files_directory.replace('\\', '/')
new_directory = input('Enter the directory where you want to create the folder(s): ')
#folder_name = input("Enter a name for your folder: ")

#target_directory = os.path.join(new_directory, folder_name)
#os.mkdir(target_directory) 

"""num_of_keywords = int(input("Enter the number of keywords: "))
keywords = []
for i in range(num_of_keywords):
    keyword = input(f"Enter the keyword no: {i}: ")
    keywords.append(keyword)
"""
def organize(files_directory, new_directory):
    if files_directory == ".":
        files_directory = os.getcwd()
    
    files = os.listdir(files_directory)
    for file in files:
        directories = get_directories(new_directory)
        display_directories(directories, check_pdf(os.path.join(files_directory, file)))
        command = input(f"For file {file}, enter your command: ")
        skip_file = False
        while not skip_file:
            while command != '.' and command != '+' and not skip_file:
                if command.isdigit():
                    new_directory = os.path.join(new_directory, directories[int(command)-1])
                    print('new directory', new_directory)
                    directories = get_directories(new_directory)
                    display_directories(directories)
                    command = input("Enter your command: ")
                elif command == 'r':
                    page_number = int(input("Enter the page number:"))
                    try:
                        print(read_pdf(new_directory, page_number))
                    except:
                        print("Failed to read file")
                        command = input("Enter your command again: ")
                elif command == '-':
                    skip_file = True
                    break
                else:
                    print('Invalid command or directory index')
            
            if skip_file:
                continue

            if command == '.':
                target_directory = new_directory
            elif command == '+':
                directory_name = input("Enter a name for your folder: ")
                target_directory = os.path.join(new_directory, directory_name)
            rename = input('Do you want to rename the file? (Y/N)')
            if rename == 'Y':
                new_name = input('Enter the new name without extension: ')
                extension = get_extension(file)
                try:
                    os.rename(os.path.join(files_directory, file), os.path.join(files_directory, new_name + extension))
                    print(f"File '{file}' renamed to '{new_name + extension}'.")
                except FileNotFoundError:
                    print(f"File '{file}' not found. Skipping rename operation.")
            
            if not os.path.exists(target_directory):
                os.mkdir(target_directory)
            shutil.move(os.path.join(files_directory, file), os.path.join(target_directory, file))
            print("File moved successfully")
     
organize(files_directory, new_directory)
