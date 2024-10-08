import os
import shutil

class Organize:
    def __init__(self, files_directory, new_directory, folder_name, keywords):
        self.files_directory = files_directory
        self.new_directory = new_directory
        self.folder_name = folder_name
        self.keywords = keywords
        self.target_directory = os.path.join(self.new_directory, self.folder_name)

    @staticmethod
    def get_user_input():
        files_directory = input("Enter your files directory: ").replace('\\', '/')
        new_directory = input('Enter the directory where you want to create the folder: ')
        folder_name = input("Enter a name for your folder: ")

        num_of_keywords = int(input("Enter the number of keywords: "))
        keywords = [input(f"Enter the keyword no: {i}: ") for i in range(num_of_keywords)]

        return files_directory, new_directory, folder_name, keywords


    def create_folder(self):
        if not os.path.exists(self.target_directory):
            os.mkdir(self.target_directory)
            print(f'Folder "{self.folder_name}" has been created in "{self.new_directory}"')
        else:
            print(f'Folder "{self.folder_name}" already exists.')

    def organize_files(self):
        if self.files_directory == ".":
            self.files_directory = os.getcwd()
            
        files = os.listdir(self.files_directory)
        print(f"Files in directory: {files}")

        for file in files:
            if all(keyword in file for keyword in self.keywords):
                try:
                    shutil.move(f'{self.files_directory}/{file}', f'{self.target_directory}/{file}')
                    print(f'File "{file}" has been moved to folder "{self.folder_name}"')
                except Exception as e:
                    print(f"Failed to move file {file}: {e}")
            else:
                print(f'File "{file}" does not match the keywords')

    @staticmethod
    def start():
        files_directory, new_directory, folder_name, keywords = Organize.get_user_input()
        
        manager = Organize(files_directory, new_directory, folder_name, keywords)
        manager.create_folder()
        manager.organize_files()