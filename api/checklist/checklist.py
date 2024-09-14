from api.model.checkListItemModel import CheckListItem
from api.model.inventoryItemModel import InventoryItem
from api.inventory.inventory import add_item as add_to_inv

items2 : list[CheckListItem] = []

items2.append(CheckListItem(id=1, itemName="CHK 1", size=10, units="kg",quantity=1))
items2.append(CheckListItem(id=2, itemName="CHK 2", size=10, units="L",quantity=12))
items2.append(CheckListItem(id=3, itemName="CHK 3", size=10, units="ml",quantity=31))
items2.append(CheckListItem(id=4, itemName="CHK 4", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=5, itemName="CHK 5", size=10, units="kg",quantity=1))
# items2.append(CheckListItem(id=6, itemName="CHK 6", size=10, units="L",quantity=12))
# items2.append(CheckListItem(id=7, itemName="CHK 7", size=10, units="ml",quantity=31))
# items2.append(CheckListItem(id=8, itemName="CHK 8", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=9, itemName="CHK 9", size=10, units="kg",quantity=1))
# items2.append(CheckListItem(id=10, itemName="CHK 10", size=10, units="L",quantity=12))
# items2.append(CheckListItem(id=11, itemName="CHK 11", size=10, units="ml",quantity=31))
# items2.append(CheckListItem(id=12, itemName="CHK 12", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=13, itemName="CHK 13", size=10, units="kg",quantity=1))
# items2.append(CheckListItem(id=14, itemName="CHK 14", size=10, units="L",quantity=12))
# items2.append(CheckListItem(id=15, itemName="CHK 15", size=10, units="ml",quantity=31))
# items2.append(CheckListItem(id=16, itemName="CHK 16", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=17, itemName="CHK 17", size=10, units="kg",quantity=1))
# items2.append(CheckListItem(id=18, itemName="CHK 18", size=10, units="L",quantity=12))
# items2.append(CheckListItem(id=19, itemName="CHK 19", size=10, units="ml",quantity=31))
# items2.append(CheckListItem(id=20, itemName="CHK 20", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=21, itemName="CHK 21", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=22, itemName="CHK 22", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=23, itemName="CHK 23", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=24, itemName="CHK 24", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=25, itemName="CHK 25", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=26, itemName="CHK 26", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=27, itemName="CHK 27", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=28, itemName="CHK 28", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=29, itemName="CHK 29", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=30, itemName="CHK 30", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=31, itemName="CHK 31", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=32, itemName="CHK 32", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=33, itemName="CHK 33", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=34, itemName="CHK 34", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=35, itemName="CHK 35", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=36, itemName="CHK 36", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=37, itemName="CHK 37", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=38, itemName="CHK 38", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=39, itemName="CHK 39", size=10, units="g",quantity=43))
# items2.append(CheckListItem(id=40, itemName="CHK 40", size=10, units="g",quantity=43))

__CHK_ID__ : int = 41


def get_all_items() -> list[CheckListItem]:
    return items2

def add_new_checklist_item(newItem : CheckListItem)->int:
    global __CHK_ID__
    newItem.id = __CHK_ID__
    __CHK_ID__ = __CHK_ID__ + 1
    items2.append(newItem)

    return (__CHK_ID__-1)

def check_item(check_itm_id : int, exp_date : str, quantity : int | None) -> int:
    filtered : list[CheckListItem] = [item for item in items2 if item.id == check_itm_id]
    if(len(filtered) == 0):
        return -1
    else:
        print('exp=',exp_date)
        checked_item : CheckListItem = filtered[0]
        inv_item : InventoryItem = InventoryItem(id=0, itemName=checked_item.itemName, size=checked_item.size, units=checked_item.units, quantity=checked_item.quantity, expDate=None,price=None)
        inv_item.expDate = exp_date
        if quantity:
            inv_item.quantity = quantity
        inv_itm_id : int =  add_to_inventory(inv_item)
        if inv_itm_id > 0:
            remove_checklist_item(check_itm_id)
            return inv_itm_id
        else:
            return -1
    
def add_to_inventory(item : InventoryItem)->int:
    if type(item) != InventoryItem:
        return -1
    else:
        id : int = add_to_inv(item)
    return id



def remove_checklist_item(id : int)->int:
    index_list = [index for index,item in enumerate(items2) if item.id == id]
    if len(index_list) == 1:
        items2.pop(index_list[0])
        return index_list[0]
    else:
        return -1