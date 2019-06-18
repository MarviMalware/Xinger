import requests
import re
import time
import argparse

#Banner
print("""
____  ___.__
\   \/  /|__| ____    ____   ___________
 \     / |  |/    \  / ___\_/ __ \_  __ \\
 /     \ |  |   |  \/ /_/  >  ___/|  | \/
/___/\  \|__|___|  /\___  / \___ _>__|   
      \_/        \//_____/          
         
Xinger Version 1.0 - June 2019
Alexander Marvi - @MarviMalware
""")

#Option Definitions
parser = argparse.ArgumentParser(description="Xinger: A tool to gather the names, roles and profiles of every employee in a specified company")
parser.add_argument(dest="URL", help="The Xing homepage of the company you want to scrape employees for", type=str)
parser.add_argument("-f", "--file", help="Specifies a filename and location to save the output to (Does not save by default)", type=str)
parser.add_argument("-s", "--silent", help="Hide Console Output", action="store_true")
commandLineOption = parser.parse_args()
file = commandLineOption.file
company = commandLineOption.URL
silent = commandLineOption.silent

#Variable Definition
offset = 0
listURL = company + "/employees.json?limit=50&offset=" + str(offset)
validOffset = 1
EmployeeList = []
r = requests.get(listURL)

#Regex Definition
noEmployeeList = re.compile(r'.*html\'\:\s\[\]\}\}\}')
findName = re.compile(r'(?<=title\=\")(.*?)(?=\")')
findRole = re.compile(r'(?<=n\s{4}\<\/li\>\\n\s{4}\<li\>)(.*?)(?=\<\/li\>)')
findURL = re.compile(r'(?<=image\"\shref=\")(.*?)(?=\")')
URLCondenser = re.compile(r'^\/.*?\/.*?(?=\/.*$)')

#Response Code Spot Check
if r.status_code == 404:
    print("Please Enter a Valid URL")
    exit()

#Menu Bar
if not silent:
    print("{0:45s} {1:80s} {2}".format("Name of Employee", "Role in Company", "Profile Link"))
    print("{0:45s} {1:80s} {2}".format('-'*16, '-'*15, '-'*12))
if file:
    with open(file, 'a') as f:
        f.write(("{0:45s} {1:80s} {2}".format("Name of Employee", "Role in Company", "Profile Link")))
        f.write('\n')
        f.write(("{0:45s} {1:80s} {2}".format('-' * 16, '-' * 15, '-' * 12)))

#Xing Parser
while validOffset == 1:
    html = str(requests.get(listURL).json())
    if noEmployeeList.match(html):
        print("\nScraping Finished")
        exit()
    else:
        for name, role, profile in zip(findName.findall(html), findRole.findall(html), findURL.findall(html)):
            URL = "https://www.xing.com" + str(URLCondenser.findall(str(profile))[0])
            role = role.replace("&amp;", "&")
            if not silent:
                print("{0:45s} {1:80s} {2}".format(name, role, URL))
            if file:
                with open(file, 'a', encoding='utf-8') as f:
                    f.write("\n")
                    f.write(("{0:45s} {1:80s} {2}".format(name, role, URL)))
        offset += int(50)
        listURL = company + "/employees.json?limit=50&offset=" + str(offset)
        time.sleep(.1)
