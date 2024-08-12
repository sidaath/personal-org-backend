from fastapi import FastAPI
from definitions import Inventory, InventoryItem
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()


inv = Inventory()

invItem1 = InventoryItem(itemName='Itm 1', size=1, units='kg', quantity=10, expDate='22' )
invItem2 = InventoryItem(itemName='Itm 2', size=44, units='L', quantity=3, expDate='2024-10-22' )

inv.addItem(invItem1)
inv.addItem(invItem2)

@app.get("/")
def test():
    return 'helloooo'


@app.get('/inventory')
def getInventory():
    print('get inv')
    return inv
