import time
from pyautogui import *
import sys

def locateAndClick(image_path, minSearchTime=10, confidence=0.8, retriesLeft=2):
    """
    Locates an image on the screen and clicks it.
    
    Args:
        image_path (str): The path to the image file.
        max_wait (int, optional): The maximum number of seconds to wait before failing. Defaults to 10.
        confidence (float, optional): The confidence level of the image match. Defaults to 0.8.
        retriesLeft (int, optional): The number of retries left. Defaults to 2. If the image is not found, it will try again if there are retries left and the game had to reload.
    
    Returns:
        bool: True if the image was found and clicked successfully, False otherwise.
    """

    reloadCheck()

    print(f"Clicking {image_path}.")

    location = locateOnScreen(
        image_path, 
        confidence=confidence,
        minSearchTime=minSearchTime
    )

    if location is not None:
        click(location)
        return True
    
    # if not found, try again if retries left
    if retriesLeft > 0 and reloadCheck():
        return locateAndClick(image_path, minSearchTime, confidence, retriesLeft - 1)
    
    # if still not found, return False, even if there are retries left.
    return False
    
def getArg():
    # sys.argv[0] is the script name itself
    if len(sys.argv) > 1:
        argument = sys.argv[1]
        return argument
    else:
        return None

def reloadCheck():
    location = locateOnScreen(
        "img/reload_game.png", 
        confidence=0.8,
        minSearchTime=0
    )

    doReload = location is not None

    if doReload:
        print("Reloading.")
        click(location)
        time.sleep(5)
    
    return doReload
        