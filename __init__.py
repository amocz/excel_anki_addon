# import the main window object (mw) from aqt
import re
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect, chooseList, getText, askUser
# import all of the Qt GUI library
from aqt.qt import *

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def Unsuspendest() -> None:
    deck_name = get_deck_name()
    update_txt_file(deck_name)


def update_txt_file(deck_name):
    data = []
    new_data = []
    filepath = "C:\\Users\\u105625\\AppData\\Roaming\\Anki2\\addons21\\excel_anki_addon\\test.txt"
    filepath1 = "C:\\Users\\u105625\\AppData\\Roaming\\Anki2\\addons21\\excel_anki_addon\\test1.txt"
    with open(filepath, "r") as file:
        data = file.readlines()

    for search_item in data:
        search_item = search_item.strip()
        unsus_search_count, sus_search_count = find_and_unsuspend_cards(deck_name, search_item)
        search_item = (f"{search_item}: \t Total Found: {unsus_search_count+sus_search_count} \t Found Unsuspended: {unsus_search_count} \t Found Suspended: {sus_search_count}\n")
        new_data.append(search_item)

    with open(filepath1, 'w', encoding='utf-8') as file:
        file.writelines(new_data)


def get_deck_name():
    deck_list = mw.col.decks.all_names_and_ids()
    deck_name_list = []
    for deck in deck_list:
        deck_name_list.append(deck.name)
    deck_index = chooseList("Pick your deck", deck_name_list)
    deck = deck_list[deck_index]
    deck_name = deck.name
    # deck_id = deck.id
    return deck_name

def find_and_unsuspend_cards(deck_name, search_item):
    # search_field = getText("Search names: ")[0]

    # found_cards = (mw.col.find_cards("deck:current is:suspended macromolecules"))
    # found_cards = (mw.col.find_cards(f"\"deck:{deck_name}\" is:suspended {search_field}"))
    found_unsuspended_cards = mw.col.find_cards(f"\"deck:{deck_name}\" -is:suspended {search_item}")
    found_unsuspended_cards_count = len(found_unsuspended_cards)
    found_suspended_cards = mw.col.find_cards(f"\"deck:{deck_name}\" is:suspended {search_item}")
    found_suspended_cards_count = len(found_suspended_cards)
    # mw.col.sched.unsuspend_cards(found_cards)
    mw.col.sched.unsuspend_cards(found_suspended_cards_count)

    # showInfo("Found unsuspended card count: " + str(found_cards_count))
    # if found_cards_count != 0:
    #     if_proceed = askUser("Do you want to unsuspend these cards?")
    #     if if_proceed:
    #         mw.col.sched.unsuspend_cards(found_cards)
    return found_unsuspended_cards_count, found_suspended_cards_count


# create a new menu item, "test"
action = QAction("Unsuspendest :)", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, Unsuspendest)
# and add it to the tools menu
mw.form.menuTools.addAction(action)




# aqt.utils.chooseList("will you?", ["yes","no"])
