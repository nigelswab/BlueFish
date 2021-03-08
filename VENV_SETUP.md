# General Testing Scripts
- This repository contains all general scripts used in BlueFish
- In order to make all scripts run deterministically on different computers, this repository makes use of a **virtual environment**.

### Table of Contents  
[Setup](#setup)<br>
[Run scripts in virtual environment](#run-scripts-in-virtual-environment)<br>
[Add a package to virtual environment](#add-package-to-virtual-environment)

<a name="setup"></a>
## Setup
### Install Python

1. Go to the official Python website (https://www.python.org/) and download the latest version of Python 3.9 (64-bit).
2. Run the installer.
   - Check "Add Python 3.9 to PATH"
   - Choose "Customize installation".
   - Go with the default options, **except** on the "Advanced options" page:
      - Check "Install for all users".

### Cloning the repo
1. Clone this repository using HTTPS
   - Using the GIT command line client:
      - Open command line
      - Navigate to a location where you want to save the repo
        - Note: Using a local drive is highly recommended for better performance
      - `git clone https://github.com/nigelswab/BlueFish.git`
      - Use your uvic github usename and password
   - Alternatively you can use any of your favourite GIT clients
2. Initialize the virtual environment:
      - Run the `setup_venv.bat` file in the repository root folder, and it will do all the hard setup work for you.



<a name="run-scripts-in-virtual-environment"></a>
## Run scripts in virtual environment
### In command line
1. In a command prompt, make sure you are in the root folder of the repository.
2. Run  `.\.venv\Scripts\activate`
3. Now run commands the normal way for python, ex. `python name_of_script.py`
4. If you'd like to exit the virtual environment, type `deactivate`

### In PyCharm
PyCharm has built-in support for virtual environments.
1. If an `.idea` folder already exists in the root folder of your repo, close pycharm and delete it
   - This will remove any link to old interpreters
2. Open the root folder of the repository in PyCharm.
   - PyCharm should now find the `.venv` folder with the virtual environment and be able to run all scripts in it. 
3. Check that PyCharm detects the virtual environment: 
   - Open Python Console in PyCharm (usually a button at the bottom of the window).
   - It will print the python version, which should be 3.9.x.

If PyCharm does not detect the virtual environment automatically:
1. In PyCharm, go to "File" -> "Settings" -> "Project: general_testing_scripts" -> "Python Interpreter"
2. In the "Python Interpreter" dropdown menu:
   - If the virtual environment interpreter is present, select that one.
   - If it is NOT present: 
      1. Select "Show all" in the dropdown menu.
      2. In the dialog window that appears, add a new interpreter by pressing the "+" button. 
      3. Under "Virtualenv Environment", select "Existing Environment" and browse for the following file: 
    `<path-to-repo>/.venv/Scripts/python.exe`
3. Click "OK" and enjoy your virtual environment.


<a name="add-package-to-virtual-environment"></a>
## Add a package to virtual environment

1. Open the Pycharm Terminal, or open command prompt in the base directory of the repo
   - If using command prompt, activate the virtual environment `.\.venv\Scripts\activate`
2. Install a package:
   - For the newest version `pip install package_name`
   - For a specific version `pip install package_name==XX.XX.XX`
   - For the newest version within a range `pip install package_name>=2.0.0,<3.0.0`
    - The PyPi website (https://pypi.org/) might be a useful resource for choosing among versions. 
3. Add the package to the requirements.txt file
   - Run `pip freeze` to get the current installed version, then add that to the requirements.txt
   - For zaber packages, don't specify a version, so we always get the latest
4. Commit any changes to requirements.txt to GIT