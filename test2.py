
import csv
import os
import re
import subprocess

release1 = '1.0.3'
release2 = '1.0.4'

files = ['build']
results = []

if __name__ == "__main__":
    totalduplicatelines = 0

    print('Amount of duplicate lines')
    command = f"jsinspect -r pmd '/usr/jquery-data/{release1}/src' '/usr/jquery-data/{release2}/src'"
    result = subprocess.getoutput(command)
    foundduplicatelines = re.findall(r'duplication lines="[+]?\d+', result, re.MULTILINE)
    for found in foundduplicatelines:
        filteredint = re.search("\d+", found).group(0)
        totalduplicatelines += int(filteredint)
    print(totalduplicatelines)
    
    command = f"jsinspect -r pmd '/usr/jquery-data/{release1}/src'"
    result = subprocess.getoutput(command)
    foundduplicatelines = re.findall(r'duplication lines="[+]?\d+', result, re.MULTILINE)
    for found in foundduplicatelines:
        filteredint = re.search("\d+", found).group(0)
        totalduplicatelines -= int(filteredint)
    print(totalduplicatelines)
    
    command = f"jsinspect -r pmd '/usr/jquery-data/{release2}/src'"
    result = subprocess.getoutput(command)
    foundduplicatelines = re.findall(r'duplication lines="[+]?\d+', result, re.MULTILINE)
    for found in foundduplicatelines:
        filteredint = re.search("\d+", found).group(0)
        totalduplicatelines -= int(filteredint)
    print(totalduplicatelines)


    command = f"cloc --ignore-whitespace '/usr/jquery-data/{release1}/src' --xml"
    result = subprocess.getoutput(command)
    found = re.findall(r'blank="[+]?\d+', result)
    filtered_blank = re.search("\d+", found[0]).group(0)
    found = re.findall(r'comment="[+]?\d+', result)
    filtered_comment = re.search("\d+", found[0]).group(0)
    found = re.findall(r'code="[+]?\d+', result)
    filtered_code = re.search("\d+", found[0]).group(0)
    
    lines1 = int(filtered_blank) + int(filtered_comment) + int(filtered_code)
    print('Amount of lines first release:')
    print(lines1)

    command = f"cloc --ignore-whitespace '/usr/jquery-data/{release2}/src' --xml"
    result = subprocess.getoutput(command)
    found = re.findall(r'blank="[+]?\d+', result)
    filtered_blank = re.search("\d+", found[0]).group(0)
    found = re.findall(r'comment="[+]?\d+', result)
    filtered_comment = re.search("\d+", found[0]).group(0)
    found = re.findall(r'code="[+]?\d+', result)
    filtered_code = re.search("\d+", found[0]).group(0)
    
    lines2 = int(filtered_blank) + int(filtered_comment) + int(filtered_code)
    print('Amount of lines second release:')
    print(lines2)

    coverage = totalduplicatelines / (lines1 + lines2)
    print("Coverage:")
    print(coverage)






    '''
     foundduplicatelines = re.findall(r'duplicate lines:"\s[+]?\d+', result, re.MULTILINE)
            for x in foundduplicatelines:
                filteredint = re.search("\d+", x)
                totalduplicatelines += int(filteredint)
    
    '''