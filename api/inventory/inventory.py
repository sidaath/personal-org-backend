from typing import List
from model.inventoryItemModel import InventoryItem
from model.constants import null_string

items :List[InventoryItem] = []
__ID__ : int = 6

items.append(InventoryItem(id=1, itemName='Test itm 1', size=900, units='g', quantity=2, expDate='2024-10-19'))
items.append(InventoryItem(id=2, itemName='Test itm 2', size=450, units='g', quantity=5, expDate='2026-10-29'))
items.append(InventoryItem(id=3, itemName='Test itm 3', size=2, units='kg', quantity=1, expDate='2024-12-09'))
items.append(InventoryItem(id=4, itemName='Test itm 4', size=8, units='L', quantity=5, expDate='2024-08-22'))
items.append(InventoryItem(id=5, itemName='Test itm 5', size=75, units='dl', quantity=8, expDate='2025-02-11'))


def get_all_items():
    return items

def get_item_by_id(id: int) -> InventoryItem:
    filtered = [inv_item for inv_item in items if inv_item.id == id]
    return filtered[0]

def get_subset(start: int, end : int) -> list[InventoryItem]:
    return items[start : end]

def add_item(newItem: InventoryItem) -> int:
    global __ID__
    newItem.id= __ID__
    __ID__ = __ID__ + 1

    items.append(newItem)
    return (__ID__ - 1)

def remove_item(id : int) -> int:
    items[:] = [inv_item for inv_item in items if not inv_item.id == id]
    return 0

        
    