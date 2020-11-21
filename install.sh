#!/bin/bash

echo "This is an automated script designed to install necessary configuration files as they are used by For raspbian"

pip3 install pydrive adafruit-circuitpython-si7021 adafruit-circuitpython-adxl34x

echo "Next is curling the python code for running the hardware"
echo "this is a dummy txt file to know that the install.sh works" > dummy.txt
python3 dummy.py
python3 uploadtodrive.py