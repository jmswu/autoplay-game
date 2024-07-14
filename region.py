
import pyautogui
import numpy as np
import image
import my_logger

logger = my_logger.getLogger(__name__)


def make_card_region(point):
    """ Make a region as the size of a card

    Args:
        point (Point): Point as in (x, y)

    Returns:
        tuple: Region (x, y, width, hight)
    """
    WIDTH = 138
    HIGTH = 144
    x = point[0]
    y = point[1]
    new_x = x - int((WIDTH / 2))
    new_y = y - int((HIGTH / 2))
    return [new_x, new_y, WIDTH, HIGTH]


def get_game_region():
    """ Locate the game screen, then return the x,y position of the
        start of the image, and the width and hight
    """

    pos_left = None
    pos_right = None
    try:
        pos_left = pyautogui.locateCenterOnScreen(
            image.icon("music"), confidence=0.8)
    except pyautogui.ImageNotFoundException as e:
        logger.error("Can't find top left connor anchor")
        return None

    try:
        pos_right = pyautogui.locateCenterOnScreen(
            image.icon("full_screen"), confidence=0.8)
    except pyautogui.ImageNotFoundException as e:
        logger.error("Can't find lower right connor anchor")
        return None

    pos_1 = [int(x) for x in pos_left]
    pos_2 = [int(x) for x in pos_right]

    np_pos_1 = np.array(pos_1)
    np_pos_2 = np.array(pos_2)

    pos_diff = np_pos_2 - np_pos_1

    return pos_1 + pos_diff.tolist()
