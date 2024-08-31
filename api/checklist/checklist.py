from api.model.checkListItemModel import CheckListItem
from api.model.inventoryItemModel import InventoryItem
from api.inventory.inventory import add_item as add_to_inv

items2 : list[CheckListItem] = []

items2.append(CheckListItem(id=1, itemName="CHK 1", size=10, units="kg",quantity=1))
items2.append(CheckListItem(id=2, itemName="CHK 2", size=10, units="L",quantity=12))
items2.append(CheckListItem(id=3, itemName="CHK 3", size=10, units="ml",quantity=31))
items2.append(CheckListItem(id=4, itemName="CHK 4", size=10, units="g",quantity=43))

__CHK_ID__ : int = 5


def get_all_items() -> list[CheckListItem]:
    return items2

def add_new_checklist_item(newItem : CheckListItem)->int:
    global __CHK_ID__
    newItem.id = __CHK_ID__
    __CHK_ID__ = __CHK_ID__ + 1
    items2.append(newItem)

    return (__CHK_ID__-1)

def add_to_inventory(check_itm_id : int, exp_date : str) -> int:
    filtered : list[CheckListItem] = [item for item in items2 if item.id == check_itm_id]
    if(len(filtered) == 0):
        return -1
    else:
        checked_item : CheckListItem = filtered[0]
        inv_item : InventoryItem = InventoryItem(id=0, itemName=checked_item.itemName, size=checked_item.size, units=checked_item.units, quantity=checked_item.quantity)
        inv_item.expDate = exp_date
        inv_itm_id : int = add_to_inv(inv_item)
        remove_checklist_item(check_itm_id)
        return inv_itm_id



def remove_checklist_item(id : int)->int:
    items2[:] = [item for item in items2 if item.id != id]
    return 0 