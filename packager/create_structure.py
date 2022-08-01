import os
import logging
import sys
import shutil
from packager.constants import SUBFOLDERS, FILES, IGNORE

class Structure:
    def __init__(self, 
                 project_name:str, 
                 folder:str=None, 
                 subfolders:list=[],
                 files:list=[],
                 ignore:list=[]):
        self.folder = folder
        self.project_name = project_name
        self.project_path = os.path.join(folder, project_name)
        self.subfolders = subfolders + [project_name]
        self.files = files
        self.ignore=ignore
        self.create_repo_structure()
        
    def create_repo_structure(self):
        self.create_folder_structure()
        self.write_init()
        self.write_files()
        
    def create_folder_structure(self):
        logging.info("Creating folder structure...")
        [os.makedirs(os.path.join(self.project_path, subfolder)) for subfolder in self.subfolders]
        
    def write_init(self, skip=["docs", "static", "tests"]):  
        logging.info("Writing __init__.py...")   
        [self.crate_init_file(os.path.join(self.project_path,subfolder))
        for subfolder in self.subfolders if subfolder not in skip]
        
    def write_files(self):
        logging.info("Writing files...")
        for file in self.files:
            file_path = os.path.join(self.project_path, file)
            if file == "setup.py":
                setup_path = os.path.join(os.path.dirname(__file__), "setup_outline.py")
                logging.info("Creating a mock setup.py file.\nEdit it before trying to install the package.")
                logging.info("To install the package locally\ncd to name_of_your_project/setup.py and run\n'pip install -e ./'")
                shutil.copy(setup_path, self.project_path)
                os.rename(os.path.join(self.project_path, "setup_outline.py"), file_path)
            else:
                open(file_path, 'w')
        
        self.write_gitignore()
        
    @staticmethod
    def crate_init_file(folder_path):
        file_path = os.path.join(folder_path, '__init__.py')
        open(file_path, "w") 
        
    def write_gitignore(self):
        logging.info("Writing .gitignore")
        ignore_path = os.path.join(self.project_path, ".gitignore")
        with open(ignore_path, 'w') as f:
            f.writelines("{}\n".format(ig) for ig in self.ignore)
        
    def __repr__(self):
        return "Structure of the project: {}".format(self.project_name)
    
def main():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.info("Welcome to the Packager: Python repo configuration")
    project_name = input("Project Name:\n")
    folder = input("Folder (default ./):\n") or "./"
    Structure(project_name, folder=folder, subfolders=SUBFOLDERS, 
              files=FILES, ignore=IGNORE)
    logging.info("You are all set up!")
    
        

if __name__ == '__main__':
    main()
    
    

