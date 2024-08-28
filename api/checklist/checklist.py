from api.model.checkListItemModel import CheckListItem

items2 : list[CheckListItem] = []

items2.append(CheckListItem(id=1, itemName="CHK 1", size=10, units="kg",quantity=1))
items2.append(CheckListItem(id=2, itemName="CHK 2", size=10, units="L",quantity=12))
items2.append(CheckListItem(id=3, itemName="CHK 3", size=10, units="ml",quantity=31))
items2.append(CheckListItem(id=4, itemName="CHK 4", size=10, units="g",quantity=43))


def get_all_items() -> list[CheckListItem]:
    return items2




