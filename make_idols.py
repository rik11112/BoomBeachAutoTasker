from pyautogui import *
from utils import *

type = getArg() or "dark"

def openSculptor():
    return (
        locateAndClick("img/buildings/sculptor.png")
        and locateAndClick("img/building_options/sculptor/sculptor.png")
    )

def deFocus():
    return locateAndClick("img/buildings/weird_statue.png")

count = 0

print("Making " + type + " idols.")

worked = True
while worked:
    deFocus()
    worked = worked and openSculptor()
    salvaged = locateAndClick("img/building_options/sculptor/salvage_statue.png", minSearchTime=2)
    if salvaged:
        worked = worked and locateAndClick("img/building_options/sculptor/confirm_salvage.png")
        deFocus()
        worked = worked and openSculptor()
    worked = worked and locateAndClick(f"img/building_options/sculptor/{type}.png")
    worked = worked and locateAndClick(f"img/building_options/sculptor/{type}_idol.png")
    print("Waiting 10 seconds for idol to be made.")
    sleep(10)   # takes a while to make the idol
    deFocus()
    worked = worked and locateAndClick("img/building_options/sculptor/deploy.png")
    if worked:
        count += 1
        print("Made " + str(count) + " idols.")
    

print("One of the steps failed.")