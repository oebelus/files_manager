import os
import shutil

from fire import Fire

class Manager:
    def __init__(self, files_directory, new_directory, folder_name, keywords):
        self.files_directory = files_directory.replace('\\', '/')
        self.new_directory = new_directory
        self.folder_name = folder_name

        self.target_directory = os.path.join(self.new_directory, self.folder_name)
        self.keywords = keywords

    def create_folder(self):
        os.mkdir(self.target_directory)
        print(f'Your folder: "{self.folder_name}" has been created')

    def organize_files(self):
        if self.files_directory == ".":
            self.files_directory = os.getcwd()
            
        files = os.listdir(self.files_directory)

        for file in files:
            if all(keyword in file for keyword in self.keywords):
                shutil.move(f'{self.files_directory}/{file}', f'{self.new_directory}/{self.folder_name}')
                print(f'Your file: {file} has been moved to the folder: {self.folder_name}')


def get_user_input():
    files_directory = input("Enter your files directory: ").replace('\\', '/')
    new_directory = input('Enter the directory where you want to create the folder: ')
    folder_name = input("Enter a name for your folder: ")

    num_of_keywords = int(input("Enter the number of keywords: "))
    keywords = [input(f"Enter the keyword no: {i}: ") for i in range(num_of_keywords)]

    return files_directory, new_directory, folder_name, keywords

def start():
    files_directory, new_directory, folder_name, keywords = get_user_input()
    
    manager = Manager(files_directory, new_directory, folder_name, keywords)
    manager.create_folder()
    manager.organize_files()
    
def main():
    Fire(start)

if __name__ == '__main__':
    main()