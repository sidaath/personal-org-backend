from fastapi import FastAPI
from inventory.inventory import get_all_items, add_item, remove_item
from definitions import InventoryItem

app = FastAPI()

@app.get("/")
def test():
    return 'helloooo'


@app.get('/inventory')
def getInventory():
    print('get inv')
    return get_all_items()

@app.get('/add')
def getInvSize():
    print('add')
    print(add_item(name='in 1', size=2, units='kg', quantity=3,expDate='2024-11-09'))
    return 

@app.get('/remove')
def remove():
    print('remove')
    ret = remove_item(3)
    return get_all_items()