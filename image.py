import os

IMAGE_PATH = "./images/"


def image(name: str):
    """ Convert a image file name to full name with path
    """
    EXTENTION_NAME = ".png"
    return f"{IMAGE_PATH}{name}{EXTENTION_NAME}"


def icon(name: str):
    """ Convert a icon file name to full icon name with path
    """
    PRE_FIX = "icon_"
    return image(f"{PRE_FIX}{name}")


def card(name: str):
    """ Convert a card file name to full card name with path
    """
    PRE_FIX = "card_"
    return image(f"{PRE_FIX}{name}")


def get_all_cards() -> list[str]:
    """ Get a list of card image file

    Returns:
        list[str]: card image file in a list
    """
    files = os.listdir(IMAGE_PATH)
    cards = [f"{IMAGE_PATH}{file}" for file in files if "card_" in file]
    return cards


def get_all_animals() -> list[str]:
    """ Return the name of all animals in images

    Returns:
        list[str]: List of animal names
    """
    cards = get_all_cards()
    return [animal.lower().replace("./images/card_", "").replace(".png", "") for animal in cards]
