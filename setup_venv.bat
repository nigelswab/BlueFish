:: Script to setup the virtual environment

:: For reference, venv shell commands: ".\.venv\Scripts\activate"  and  "deactivate"

@echo off 
echo --------------------------------------
echo #                                    #
echo #  Setup of virtual environment for  #
echo #    general_testing_scripts repo    #
echo #                                    #
echo --------------------------------------

:: PYTHON:

echo Setting up venv..
py -3.9 -m venv .venv
echo --------------------------------------

:: PACKAGES:

echo Installing packages..
echo --------------------------------------
.venv\Scripts\pip install -r requirements.txt  
echo --------------------------------------

:: PTH:

echo Creating .pth file in .venv\Lib\site-packages (so relative path imports work)...
echo %~dp0 > .venv\Lib\site-packages\zaber_lib_path.pth
echo --------------------------------------
echo Setup complete!
pause
