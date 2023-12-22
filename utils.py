import time
from pyautogui import *
import sys

def locateAndClick(image_path, minSearchTime=10, confidence=0.8):
    """
    Locates an image on the screen and clicks it.
    
    Args:
        image_path (str): The path to the image file.
        max_wait (int, optional): The maximum number of seconds to wait before failing. Defaults to 10.
    
    Returns:
        bool: True if the image was found and clicked successfully, False otherwise.
    """

    print(f"Clicking {image_path}.")

    location = locateOnScreen(
        image_path, 
        confidence=confidence,
        minSearchTime=minSearchTime
    )

    if location is not None:
        click(location)
        return True
    else:
        return False
    
def getArg():
    # sys.argv[0] is the script name itself
    if len(sys.argv) > 1:
        argument = sys.argv[1]
        return argument
    else:
        return None