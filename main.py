# Main Code

from colorama import Fore
import normal, funcs

label = True

try:
    while label:
        normal.printBrand("Weather-App")
        ch = normal.myMenu(["Check Current Weather","Check Via City Name","Check Via Zip Code","Find Your Country Code","About Me","Exit"])

        if ch == 1:
            funcs.checkCurrent()
        elif ch == 2:
            funcs.checkViaName()
        elif ch == 3:
            funcs.checkViaZipCode()
        elif ch == 4:
            funcs.checkCode()
        elif ch == 5:
            normal.aboutMe()
        elif ch == 6:
            normal.quitMe()
            label = False
except:
    normal.quitMe()