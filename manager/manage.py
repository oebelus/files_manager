import os
import shutil
from manager.utils import get_extension, get_directories, display_directories, read_pdf, check_pdf, read_file, get_parent_directory, commands_list

class Manage:
    def __init__(self):
        pass

    def organize():
        in_loop = True
        while in_loop:
            command = input("--- Enter (new) to start over or (q) to quit: ")
            if command == 'new':
                files_directory = input("Enter your files directory: ")
                files_directory.replace('\\', '/')
                new_directory = input('Enter the directory where you want to create the folder(s): ')
                target_directory = new_directory
            
                files = os.listdir(files_directory)
                non_folders = [file for file in files if os.path.isfile(os.path.join(files_directory, file))]
                if len(non_folders) == 0:
                    print('> No files found')
                    if len(files) == 0:
                        print('> No directories found')
                    else:
                        print('> There are only directories in this folder')
                for file in non_folders:
                    extension = get_extension(file)
                    fullname = file
                    directories = get_directories(target_directory)
                    display_directories(directories)
                    command = input(f"--- For file '{file}', enter your command: ")
                    skip_file = False
                    while not skip_file:
                        while not skip_file and command != 'q':
                            if command.isdigit():
                                try:
                                    target_directory = os.path.join(target_directory, directories[int(command)-1])
                                    directories = get_directories(target_directory)
                                    display_directories(directories)
                                except:
                                    print("Directory Index Out of Range")
                                command = input("--- Enter your command: ")
                            elif command == 'r':
                                if check_pdf(file):
                                    try:
                                        page_number = int(input("--- Enter the page number:"))
                                        print(read_pdf(files_directory + '\\' + file, page_number))
                                    except:
                                        print("Failed to read file")
                                else:
                                    try:
                                        print(read_file(target_directory))
                                    except:
                                        print("Failed to read file")
                                command = input("--- Enter your command: ")
                            elif command == 'd':
                                try:
                                    os.remove(os.path.join(files_directory, file))
                                    print('File was successfully removed')
                                    skip_file = True
                                except:
                                    print('Failed to remove file')
                                command = input("--- Enter your command: ")
                            elif command == 'D':
                                try: 
                                    folder_to_remove = int(input("Enter the number of the directory to remove: "))
                                    directory_to_remove = os.path.join(target_directory, directories[folder_to_remove-1])
                                    shutil.rmtree(directory_to_remove, ignore_errors=False, onerror=None)
                                    print(f"The Folder {directories[folder_to_remove-1]} was successfully removed")
                                except:
                                    print("Failed to remove folder, enter a valid number")
                                command = input("--- Enter your command: ")
                            elif command == '-':
                                skip_file = True
                                break
                            elif command == '+':
                                directory_name = input("--- Enter a name for your folder: ")
                                target_directory = os.path.join(target_directory, directory_name)
                                try:
                                    os.mkdir(target_directory)
                                    directories.append(directory_name)
                                    print("Directory created successfully!")
                                except:
                                    print("Failed to create directory")
                                display_directories(directories)
                                command = input("--- Enter your command: ")
                            elif command == '..':
                                old_directory = target_directory
                                target_directory = get_parent_directory(old_directory)
                                directories = get_directories(target_directory)
                                display_directories(directories)
                                command = input("--- Enter your command again: ")
                            elif command == 'dirs':
                                display_directories(directories)
                                command = input("--- Enter your command: ")
                            elif command == 'n':
                                print(file)
                                command = input("--- Enter your command: ")
                            elif command == 're':
                                new_name = input('Enter the new name without extension: ')
                                fullname = new_name + extension
                                origin = os.path.join(target_directory, file)
                                updated = os.path.join(target_directory, fullname)
                                try:
                                    os.rename(origin, updated)
                                    file = fullname
                                    print(f"File '{file}' renamed to '{new_name + extension}'.")
                                except FileNotFoundError:
                                    print(f"File '{file}' not found.")
                                command =  input("--- Enter your command: ")
                            elif command == 'redir':
                                directory_to_rename = int(input('Enter the numer of the directory to rename: '))
                                new_name = input('Enter the new name: ')
                                os.rename(os.path.join(target_directory, directories[directory_to_rename-1]), os.path.join(target_directory, new_name))
                                directories[directory_to_rename-1] = new_name
                                print('Directory renamed successfully!')
                                command =  input("--- Enter your command: ")
                            elif command == 'mv':
                                directory_to_move_input = input("Enter the number of the directory to move: ")
                                directory_to_move = int(directory_to_move_input) if directory_to_move_input.isdigit() else None
                                where = input('Enter the number or the path of the target folder: ')
                                if where.isdigit():
                                    try:
                                        os.move(os.path.join(target_directory, directories[where-1]), os.path.join(target_directory, directories[directory_to_move-1]))
                                        print("**** Directory moved successfully ****")
                                    except:
                                        print("Failed to move directory")
                                else:
                                    target = os.path.join(target_directory, where)
                                    if not target:
                                        os.mkdir(target)
                                    try:
                                        os.move(target, os.path.join(target_directory, directories[directory_to_move-1]))
                                        print("**** Directory moved successfully ****")
                                    except: 
                                        print("Failed to move directory")
                                command = input("--- Enter your command: ")
                            elif command == 'h':
                                commands_list()
                                command = input("--- Enter your command: ")
                            elif command == '.':
                                if not os.path.exists(target_directory):
                                    os.mkdir(target_directory)
                                source_path = os.path.join(files_directory, file)
                                if os.path.exists(source_path):
                                    shutil.move(source_path, os.path.join(target_directory, file))
                                    print("**** File moved successfully ****")
                                    skip_file = True
                                else:
                                    print(f"Error: File '{file}' not found in the source directory.")
                            else: 
                                print("Invalid command or directory index")
                                command = input("--- Enter your command: ")
                        if skip_file:
                            continue

            if command == 'q':
                in_loop = False
                print("**** Bye Bye! Can't wait to see you again :3 *****")
                break

