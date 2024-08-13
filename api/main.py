from fastapi import FastAPI
from inventory.inventory import get_all_items, add_item, remove_item
from model.inventoryItemModel import InventoryItem

app = FastAPI()

@app.get("/")
def test():
    return 'helloooo'


@app.get('/inventory')
def getInventory():
    print('get inv')
    return get_all_items()

@app.post('/inventoy')
def addInvItem(item : InventoryItem) -> str:
    print('add to inv')
    add_item(item)
    return ("success")


@app.get('/remove')
def remove():
    print('remove')
    ret = remove_item(3)
    return get_all_items()