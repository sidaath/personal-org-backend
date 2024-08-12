from typing import List
from definitions import InventoryItem

items :List[InventoryItem] = []
__ID__ : int = 6

items.append(InventoryItem(id=1, itemName='Test itm 1', size=900, units='g', quantity=2, expDate='2024-10-19'))
items.append(InventoryItem(id=2, itemName='Test itm 2', size=450, units='g', quantity=5, expDate='2026-10-29'))
items.append(InventoryItem(id=3, itemName='Test itm 3', size=2, units='kg', quantity=1, expDate='2024-12-09'))
items.append(InventoryItem(id=4, itemName='Test itm 4', size=8, units='L', quantity=5, expDate='2024-08-22'))
items.append(InventoryItem(id=5, itemName='Test itm 5', size=75, units='dl', quantity=8, expDate='2025-02-11'))


def get_all_items():
    return items

def add_item(name:str, size:int, units:str, quantity:int, expDate:str) -> str:
    global __ID__
    item_id = __ID__
    __ID__ = __ID__ + 1
    items.append(InventoryItem(id=item_id, itemName=name, units=units, size=size,quantity=quantity,expDate=expDate ))
    return str(len(items) - 1)

def remove_item(id : int) -> int:
    items[:] = [item for item in items if not item.id == id]
    return 0

        
    