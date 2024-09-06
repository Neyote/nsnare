# nsnare
A File Integrity Checker written in Python
By Neyote

This script currently has two options:
- Create a baseline file (nsnarebaseline.txt) in the script's current directory containing a file's path and its corresponding hash
- Run an integrity check of the scan directory (currently statically set as ./files_to_scan) using the directory's current state and comparing it to the baseline file

I started off by following the tutorial [shown here by @sebastienwebdev](https://medium.com/@sebastienwebdev/file-integrity-monitor-in-python-a-beginners-guide-fedefc9d9284) but started to deviate once I made it to the monitoring section. I wanted the script to be run every time a check is made, rather than continuously monitor. Plus the "Begin Monitoring" section didn't have any code anyway.

I plan on making the scan directory and baseline file more dynamic by taking in arguments from the user when running the script, but for now it is statically set.
