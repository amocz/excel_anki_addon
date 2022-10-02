# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect, chooseList, getText, askUser
# import all of the Qt GUI library
from aqt.qt import *

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def testFunction() -> None:
    deck_list = mw.col.decks.all_names_and_ids()
    deck_name_list = []
    for deck in deck_list:
        deck_name_list.append(deck.name)
    deck_index = chooseList("Pick your deck", deck_name_list)
    deck = deck_list[deck_index]
    deck_name = deck.name
    deck_id = deck.id
    search_field = getText("Search names: ")[0]

    # found_cards = (mw.col.find_cards("deck:current is:suspended macromolecules"))
    found_cards = (mw.col.find_cards(f"\"deck:{deck_name}\" is:suspended {search_field}"))
    found_cards_count = len(found_cards)
    # mw.col.sched.unsuspend_cards(found_cards)
    showInfo("Found unsuspended card count: " + str(found_cards_count))
    if_proceed = askUser("Do you want to unsuspend these cards?")
    if if_proceed:
        mw.col.sched.unsuspend_cards(found_cards)

# create a new menu item, "test"
action = QAction("test", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, testFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)




# aqt.utils.chooseList("will you?", ["yes","no"])
