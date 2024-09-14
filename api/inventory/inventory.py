from typing import List
from api.model.inventoryItemModel import InventoryItem


items :List[InventoryItem] = []
__ID__ : int = 40

items.append(InventoryItem(id=1, itemName='Test itm 1', size=900, units='g', quantity=2, expDate='2024-10-19',price=None))
items.append(InventoryItem(id=2, itemName='Test itm 2', size=450, units='g', quantity=5, expDate='2026-10-29',price=None))
items.append(InventoryItem(id=3, itemName='Test itm 3', size=2, units='kg', quantity=1, expDate='2024-12-09',price=None))
items.append(InventoryItem(id=4, itemName='Test itm 4', size=8, units='L', quantity=5, expDate='2024-08-22',price=None))
items.append(InventoryItem(id=5, itemName='Test itm 5', size=75, units='dl', quantity=8, expDate=None,price=None))

# for i in range(6,36):
#     invItem : InventoryItem = InventoryItem(id=__ID__, itemName=('Fill Itm '+str(i)), size=888,units='dl',quantity=99,expDate=None,price=None)
#     __ID__ += 1
#     items.append(invItem)



def get_all_items():
    return items

def get_item_by_id(id: int) -> InventoryItem | None:
    filtered = [inv_item for inv_item in items if inv_item.id == id]
    if filtered == []:
        return None
    else:
        return filtered[0]

def get_subset(start: int, end : int) -> list[InventoryItem]:
    if (start >= 0 and end >= len(items)):
        return []
    elif (start<=0):
        return []
    else:
        return items[start : end]

def add_item(newItem: InventoryItem) -> int:
    if not type(newItem) == InventoryItem:
        return -1
    global __ID__
    newItem.id= __ID__
    __ID__ = __ID__ + 1

    items.append(newItem)
    return (__ID__ - 1)

def remove_item(id : int) -> int:
    index_list = [index for index,item in enumerate(items) if item.id == id]
    if len(index_list) == 1:
        items.pop(index_list[0])
        return index_list[0]
    else:
        return -1

        
def modify_quantity(id : int, value : int)->bool:
    index : list[int] = [idx for idx,item in enumerate(items) if item.id == id]
    if len(index) == 0:
        return False
    else:
        if (value == 0):
            remove_item(id)
            return True
        item : InventoryItem  = items[index[0]]
        item.quantity = value
        items[index[0]] = item
        return True
    