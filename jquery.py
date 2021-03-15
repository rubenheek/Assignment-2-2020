
import csv
import os
import re

releases = []
sizzle = ['1.11.0', '1.11.1', '1.11.2', '1.11.3', '2.1.0', '2.1.1', '2.1.2', '2.1.3', '2.1.4']
direc = []#'build', 'speed', 'test', 'external']
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
        for dire in direc:
            command = f"rm -r {dire}"
            print(f"Executing {command}")
            os.system(command)

        if release['tag'] in sizzle:
            command = f"src"
            print(f"Executing {command}")
            os.chdir(command)
            command = f"sizzle"
            print(f"Executing {command}")
            os.chdir(command)
            command = f"rm -r test"
            print(f"Executing {command}")
            os.system(command)
            command = f"../"
            print(f"Executing {command}")
            os.chdir(command)
            command = f"../"
            print(f"Executing {command}")
            os.chdir(command)

        command = f"../"
        print(f"Executing {command}")
        os.chdir(command)
