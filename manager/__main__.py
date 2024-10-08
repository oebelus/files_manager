from fire import Fire

from manager.organize import Organize
from manager.manage import Manage
from manager.utils import check_pdf, commands_list, display_directories, get_directories, get_extension, get_parent_directory, read_file, read_pdf

class Manager:
    def __init__(self):
        pass

    def organize(self):
        Organize.start()

    def manage(self):
        Manage.organize()

def main():
    Fire(Manager)

if __name__ == '__main__':
    main()