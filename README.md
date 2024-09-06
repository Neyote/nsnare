# nsnare
A File Integrity Checker written in Python

This script currently has two options:
- Create a baseline file (nsnarebaseline.txt) in the script's current directory containing a file's path and its corresponding hash
- Run an integrity check of the scan directory (currently statically set as ./files_to_scan) using the directory's current state and comparing it to the baseline file

I plan on making the scan directory and baseline file more dynamic by taking in arguments from the user when running the script, but for now it is statically set.
