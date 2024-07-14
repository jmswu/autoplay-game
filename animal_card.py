import pyautogui
import region
import image
import my_logger
import helper

logger = my_logger.getLogger(__name__)


def click(point):
    while True:
        pyautogui.mouseDown(point)
        pyautogui.mouseUp(point)

        # We try to take another image match after a click, if the click
        # is successfully register, we should not be able to see the question
        # again. If we can find the quesiton mark, we need to click again
        qbox = None
        try:
            qbox = pyautogui.locate(needleImage=image.icon("qmark"),
                                    haystackImage=pyautogui.screenshot(),
                                    region=region.make_card_region(point))
        except pyautogui.ImageNotFoundException as e:
            pass
        if qbox is not None:
            logger.error(f"bad click: {point}")
        if qbox is None:
            break


def find_animal(screen, point, card_files: list[str]):
    """ Find an animal from the screen around that point

    Args:
        screen (Image): Screen image
        point (Point): A point that we need to location animal
        card_files (list(str)): A list of animal in file that can be identify

    Returns:
        str: Animal that is found
    """
    for one_card in card_files:
        box = None
        try:
            box = pyautogui.locate(needleImage=one_card,
                                   haystackImage=screen,
                                   region=region.make_card_region(point),
                                   confidence=0.7)
        except pyautogui.ImageNotFoundException as e:
            pass
        if box is None:
            # logger.info("... NOT found!")
            pass
        else:
            # logger.info(f"Found {one_card}!!")
            return one_card.lower().replace("./images/card_", "").replace(".png", "")

    return None


def locate_all_animal(qmark_boxes):
    count = 0
    point_and_animal = []
    for one_qmark in qmark_boxes:
        point = pyautogui.center(one_qmark)
        click(point)

        # move away so we can capture the screen with no mouse
        pyautogui.moveTo((10, 10))

        # screen capture for debugging
        count += 1
        game_screen_x = f"screen_{count}"
        game_screen = pyautogui.screenshot(f"{game_screen_x}.png")

        animal = find_animal(
            game_screen, point, image.get_all_cards())
        logger.info(f"Looking at {game_screen_x}, found [{animal}]")
        point_and_animal.append((animal, point))
    return point_and_animal


def click_on_matching_animals(point_and_animal):
    for animal in image.get_all_animals():
        matched_points = (animal, )
        for target in point_and_animal:
            if animal in target:
                matched_points += (target[1], )
        if len(matched_points) == 3:
            print(matched_points)
            point_1 = matched_points[1]
            point_2 = matched_points[2]
            click(point_1)
            click(point_2)


def get_qmark_boxes(screen_region):
    while True:
        # find all question marks locations
        qmark_boxes = pyautogui.locateAll(needleImage=image.icon("qmark"),
                                          haystackImage=pyautogui.screenshot(),
                                          region=screen_region,
                                          confidence=0.98)

        qmark_boxes_copy = helper.duplicate(qmark_boxes)

        if helper.is_even_items(qmark_boxes_copy):
            return qmark_boxes_copy
        else:
            logger.warn("question mark boxes is not even number")
