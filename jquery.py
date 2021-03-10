
import csv
import os
import re

releases = []
direc = [] #['build']
files = [] #['GPL-LICENSE.txt', 'MIT-LICENSE.txt', 'README.md']
results = []

if __name__ == "__main__":
    with open('jquery_releases.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            releases.append(row)

    for release in releases:
        command = f"{release['tag']}"
        print(f"Executing {command}")
        os.chdir(command)
        command = f"ls"
        print(f"Executing {command}")
        os.system(command)
        for fil in files:
            command = f"rm -r {fil}"
            print(f"Executing {command}")
            os.system(command)

        command = f"../"
        print(f"Executing {command}")
        os.chdir(command)

    '''
    for release1 in releases:
        totalduplicatelines = 0
        column = []
        for release2 in releases:
            if release1 == release2:
                column.append(0)
            else:
                command = f"npx jsinspect -I -L -r pmd 1.0 1.2"
                result = os.system(command)
                print(command)
                print(result)
                command = f"cloc --ignore-whitespace {release1}"
                result = os.system(command)

           


    command = f"npx jsinspect -I -L -r pmd 1.0 1.2"
    result = os.system(command)
    print("Printing results")
    print(result)

     foundduplicatelines = re.findall(r'duplicate lines:\s[+]?\d+', result, re.MULTILINE)
            for x in foundduplicatelines:
                filteredint = re.search("\d+", x)
                totalduplicatelines += int(filteredint)
    
    '''