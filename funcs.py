# All Functions Needed for Project

import csv, json
from colorama import Fore
import requests, normal, sys

APP_ID = "2b1520594578e63d1640ee6f3cb0525a"

# TODO : Check Via City Name
def checkViaName():
    print()
    print('-'*40)
    print()
    name = input("Enter the name of City : ").strip().title()
    code = input("Enter the Country Code : ").strip().lower()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={name},{code}&appid={APP_ID}&units=metric"
    
    try:
        response = requests.get(url=url)
    except:
        print(Fore.RED)
        print("You don't have internet connection..!!")
        normal.quitMe()
    try:
        response.raise_for_status()
    except:
        print(Fore.RED)
        print("Invalid City Name or Code")
        return None
    print(Fore.YELLOW)
    printData(response.text)


# TODO : Check Via Zip Code
def checkViaZipCode():
    print()
    print('-'*40)
    print()
    name = input("Enter your Zip Code : ").strip()
    code = input("Enter the Country Code : ").strip().lower()
    url = f"https://api.openweathermap.org/data/2.5/weather?zip={name},{code}&appid={APP_ID}&units=metric"
    try:
        response = requests.get(url=url)
    except:
        print(Fore.RED)
        print("You don't have internet connection..!!")
        normal.quitMe()
    try:
        response.raise_for_status()
    except:
        print(Fore.RED)
        print("Invalid Zip Code or Code")
        return None
    print(Fore.YELLOW)
    printData(response.text)

# TODO : Check Country Code
def checkCode():
    print()
    print('-'*40)
    print()
    name = input("Enter The Name of Your Country : ").strip().title()
    files = open('files/codes.csv', 'r', newline='')
    codeReader = csv.DictReader(files, ['Name','Alpha-2','Alpha-3','Country-code','Iso_3166-2','Region','Sub-region','Intermediate-region','Region-code','Sub-region-code','Intermediate-region-code'])

    for codes in codeReader:
        if codes['Name'].title() == name:
            print(Fore.YELLOW)
            print(f"Country Code for {name} is  -> ",codes['Alpha-2'])
            return None
    print(Fore.RED)
    print("Given Country Don't have code..!!")

# TODO : Check Country Name
def findCountry(code):
    files = open('files/codes.csv', 'r', newline='')
    codeReader = csv.DictReader(files, ['Name','Alpha-2','Alpha-3','Country-code','Iso_3166-2','Region','Sub-region','Intermediate-region','Region-code','Sub-region-code','Intermediate-region-code'])

    for codes in codeReader:
        if codes['Alpha-2'] == code:            
            return codes['Name'].title()

def printData(jsonData):
    print(Fore.YELLOW)
    dictData = json.loads(jsonData)
    normal.printBrand("Co-ordinates",color=Fore.YELLOW, symbol='-')
    print("Longitude : ",dictData['coord']['lon'])
    print("Latitude : ",dictData['coord']['lat'])
    normal.printBrand("Weather",color=Fore.YELLOW, symbol='-')
    print("Weather : ", dictData['weather'][0]['description'])
    print("Temperature : ", dictData['main']['temp']," ^ C")
    print("Wind : ", dictData['wind']['speed'], " meter/sec")
    normal.printBrand("Geo-Data",color=Fore.YELLOW, symbol='-')
    print("Name of City : ", dictData['name'])
    print("Name of Country : ", findCountry(dictData['sys']['country']))
    print("Time Zone -> ", (dictData['timezone']//3600),' : ',((dictData['timezone']%3600)//60), " hr")
