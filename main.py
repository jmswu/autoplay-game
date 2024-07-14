import pyautogui
import my_logger
import image
import region
import animal_card
import helper


# Create a logger
logger = my_logger.getLogger(__name__)
logger.info("== new session ==")

pyautogui.PAUSE = 0.12
pyautogui.FAILSAFE = True

screen_region = region.get_game_region()

if (screen_region == None):
    logger.info("Can't find screen region")
    exit(1)

# find all question mark boxes
qmark_boxes = animal_card.get_qmark_boxes(screen_region)

# find animal and points
point_and_animal = animal_card.locate_all_animal(qmark_boxes)

# click on the matching points
animal_card.click_on_matching_animals(point_and_animal)
