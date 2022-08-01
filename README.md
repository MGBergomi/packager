# Python packager

Generate a Python repository structure creating the command `packager`.

## Structure

```bash
.
+-- project_name
|    +-- contrib
|       +-- __init__.py
|    +-- docker
|    +-- docs
|    +-- lib
|       +-- __init__.py
|    +-- project_name
|       +-- __init__.py
|    +-- static
|    +-- test
|    +-- LICENSE
|    +-- requirements.txt
|    +-- setup.py
|    +-- .gitignore
```

### Notes

- The `.gitignore` file is pre-made. Feel free to modify it at need. Try to avoid uploading large files, unless it is necessary.
- The `setup.py` comes almost complete. Open and modify it including your project's name and features. See the **setup.py** section below.
- The `LICENSE` file is blank.

### Guidelines

1. It is important to respect the structure of the repo to ensure consistency throughout all projects.
2. Write unit and integration test using pytest
3. Containerize your repo, if necessary

## Install

1. Clone the repository
2. Run the following commands

   ```bash
   cd packager
   pip3 install ./
   ```

## Usage

Start configuring your repo by running the command

```bash
    packager
```

Follow the instruction and read the logs

```bash
> py_packager  

INFO:root:Welcome to the Packager: Python repo configuration
Project Name:
test
Folder (default ./):

INFO:root:Creating folder structure...
INFO:root:Writing __init__.py...
INFO:root:Writing files...
INFO:root:Creating a mock setup.py file.
Edit it before trying to install the package.
INFO:root:To install the package locally
cd to name_of_your_project/setup.py and run
'pip install -e ./'
INFO:root:Writing .gitignore
INFO:root:You are all set up!
```

## Setup.py

Create the requirements file through *pipreqs*. You can install the package via pip:

```bash
    pip install pipreqs
```

Then, move to the directory containing the file **setup.py** and create the file via the command

```bash
    pipreqs --force ./ 
```

Then, open the file setup.py and substitute the name of your project to the string YOUR PROJECT NAME.
Finally browse through the file to change fields that are not correct (e.g. version, minimum required Python version).
