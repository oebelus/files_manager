import os
import shutil
from utils import get_extension

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
        folder_name = input(f"Where do you want to put this file '{file}'? {'(Enter a number followed by + to read the number of lines of the file)' if open(os.path.join(files_directory, file)).readable() else '.'}")
        while ('+' in folder_name or folder_name == 'ls' or folder_name == '-'):
            if '+' in folder_name:
                modified_folder_name = folder_name.replace('+', '')
                line_numbers = int(modified_folder_name)
                print("Line numbers: ", line_numbers)
                file_path = os.path.join(files_directory, file)
                try: 
                    with open(file_path, 'r', encoding='utf-8') as opened_file:
                        lines = opened_file.readlines()
                        total_lines = len(lines)
                        if line_numbers >= total_lines:
                            print(lines[0:total_lines])
                        else:
                            print(lines[line_numbers])
                except:
                    print("Can't read file")
            elif folder_name == 'ls':
                print(os.listdir(new_directory))
            elif folder_name == '-':
                break
            folder_name = input(f"Where do you want to put this file '{file}'? {'(Enter a number followed by + to read the number of lines of the file)' if open(os.path.join(files_directory, file)).readable() else '.'}")
        rename = input('Do you want to rename the file? (Y/N)')
        if rename == 'Y':
            new_name = input('Enter the new name without extension: ')
            extension = get_extension(file)
            try:
                os.rename(os.path.join(files_directory, file), os.path.join(new_directory, new_name + extension))
                print(f"File '{file}' renamed to '{new_name + extension}'.")
            except FileNotFoundError:
                print(f"File '{file}' not found. Skipping rename operation.")
        if folder_name == ".":
            target_directory = os.getcwd()
        else:
            target_directory = os.path.join(new_directory, folder_name)
        if not os.path.exists(target_directory):
            os.mkdir(target_directory)
        shutil.move(f'{files_directory}/{file}', f'{new_directory}/{folder_name}')
        print("File moved successfully")
     
organize(files_directory, new_directory)