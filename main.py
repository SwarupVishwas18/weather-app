# Main Code

from colorama import Fore
import normal, funcs


try:
    while True:
        normal.printBrand("Weather-App")
        ch = normal.myMenu(["Check Via City Name","Check Via Zip Code","Find Your Country Code","About Me","Exit"])

        if ch == 1:
            funcs.checkViaName()
        elif ch == 2:
            funcs.checkViaZipCode()
        elif ch == 3:
            funcs.checkCode()
        elif ch == 4:
            normal.aboutMe()
        elif ch == 5:
            normal.quitMe()
except:
    normal.quitMe()