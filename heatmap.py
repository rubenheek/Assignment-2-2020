
import csv
import os
import re
import subprocess

 
releases = ['1.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1', '1.1.1', '1.1.2', '1.1.3', '1.1.3.1' 
,'1.1.4', '1.2', '1.2.1', '1.2.2', '1.2.3', '1.2.4', '1.2.5', '1.2.6', '1.3', '1.3.0', '1.3.1' 
,'1.3.2', '1.4', '1.4.0', '1.4.1', '1.4.2', '1.4.3', '1.4.4', '1.5', '1.5.0', '1.5.1', '1.5.2' 
,'1.6', '1.6.0', '1.6.1', '1.6.2', '1.6.3', '1.6.4', '1.7', '1.7.0', '1.7.1', '1.7.2', '1.8.0' 
,'1.8.1', '1.8.2', '1.8.3', '1.9.0', '1.9.1', '1.10.0', '1.10.1', '1.10.2', '1.11.0', '1.11.1'
,'1.11.2', '1.11.3', '1.12.0', '1.12.1', '1.12.2', '1.12.3', '1.12.4', '2.0.0', '2.0.1' 
,'2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.1.2', '2.1.3', '2.1.4', '2.2.0', '2.2.1', '2.2.2' 
,'2.2.3', '2.2.4', '3.0.0', '3.1.0', '3.1.1', '3.2.0', '3.2.1', '3.3.0', '3.3.1', '3.4.0', '3.4.1']

results = []

if __name__ == "__main__":
    for x in range(0, len(releases)):
        column = []
        for y in range(0, len(releases)):
            if x <= y:
                column.append(0)
            else:
                totalduplicatelines = 0
                totalduplicatelines2 = 0
                command = f"jsinspect -I -L -t 50 -r pmd '/usr/jquery-data/{releases[x]}/src' '/usr/jquery-data/{releases[y]}/src'"
                result = subprocess.getoutput(command)
                foundduplicatelines = re.findall(r'duplication lines="[+]?\d+', result, re.MULTILINE)
                for found in foundduplicatelines:
                    filteredint = re.search("\d+", found).group(0)
                    totalduplicatelines += int(filteredint)

                command = f"jsinspect -I -L -t 50 -r pmd '/usr/jquery-data/{releases[x]}/src'"
                result = subprocess.getoutput(command)
                foundduplicatelines = re.findall(r'duplication lines="[+]?\d+', result, re.MULTILINE)
                for found in foundduplicatelines:
                    filteredint = re.search("\d+", found).group(0)
                    totalduplicatelines -= int(filteredint)
                
                command = f"jsinspect -I -L -t 50 -r pmd '/usr/jquery-data/{releases[y]}/src'"
                result = subprocess.getoutput(command)
                foundduplicatelines = re.findall(r'duplication lines="[+]?\d+', result, re.MULTILINE)
                for found in foundduplicatelines:
                    filteredint = re.search("\d+", found).group(0)
                    totalduplicatelines -= int(filteredint)
                            
                

                command = f"cloc '/usr/jquery-data/{releases[x]}/src' --xml"
                result = subprocess.getoutput(command)
                found = re.findall(r'blank="[+]?\d+', result)
                filtered_blank = re.search("\d+", found[0]).group(0)
                found = re.findall(r'comment="[+]?\d+', result)
                filtered_comment = re.search("\d+", found[0]).group(0)
                found = re.findall(r'code="[+]?\d+', result)
                filtered_code = re.search("\d+", found[0]).group(0)
                
                lines1 = int(filtered_blank) + int(filtered_comment) + int(filtered_code)


                command = f"cloc '/usr/jquery-data/{releases[y]}/src' --xml"
                result = subprocess.getoutput(command)
                found = re.findall(r'blank="[+]?\d+', result)
                filtered_blank = re.search("\d+", found[0]).group(0)
                found = re.findall(r'comment="[+]?\d+', result)
                filtered_comment = re.search("\d+", found[0]).group(0)
                found = re.findall(r'code="[+]?\d+', result)
                filtered_code = re.search("\d+", found[0]).group(0)
                
                lines2 = int(filtered_blank) + int(filtered_comment) + int(filtered_code)

                coverage = totalduplicatelines / (lines1 + lines2)
                column.append(coverage)
                print('Added to column: ')

            
        results.append(column)
        print('Completed column')

    print(results)
