import os
import shutil

files_directory = input("Enter your files directory: ")
files_directory.replace('\\', '/')
new_directory = input('Enter the directory where you want to create the folder: ')
folder_name = input("Enter a name for your folder: ")

target_directory = os.path.join(new_directory, folder_name)
os.mkdir(target_directory) 

num_of_keywords = int(input("Enter the number of keywords: "))
keywords = []
for i in range(num_of_keywords):
    keyword = input(f"Enter the keyword no: {i}: ")
    keywords.append(keyword)

def organize(files_directory, folder_name, keywords):
    if files_directory == ".":
        files_directory = os.getcwd()
    print(f'Your folder: "{folder_name}" has been created')
    files = os.listdir(files_directory)
    for file in files:
        if all(keyword in file for keyword in keywords):
            shutil.move(f'{files_directory}/{file}', f'{new_directory}/{folder_name}')
            print(f'Your file: {file} has been moved to the folder: {folder_name}')
