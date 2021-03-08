#!/bin/bash

## Install virtual environment ##
echo "Setting up virtual environment..."
pipenv install --skip-lock
echo "================================="

## Create .pth file in site-packages to include repo in python path ##
echo "Creating .pth file in site-packages of virtual environment..."
_name_of_pth_file="repo-path.pth"
_path_to_site_packages="$(pwd)/.venv/lib/python3.7/site-packages"
_path_to_pth_file="${_path_to_site_packages}/${_name_of_pth_file}"
_path_to_repo="$(dirname `pwd`)"
echo $_path_to_repo > $_path_to_pth_file
