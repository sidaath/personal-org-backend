from fastapi import FastAPI, Path, Query, Body, status
from typing import Annotated
import api.inventory.inventory  as inventory
from api.model.inventoryItemModel import InventoryItem

app = FastAPI()

@app.get("/")
def test():
    return 'helloooo'


@app.get('/inventory', status_code=status.HTTP_200_OK)
def getInventory():
    print('get inv')
    return inventory.get_all_items()


@app.get('/inventory/{item_id}', status_code=status.HTTP_200_OK)
def get_inv_item(item_id : Annotated[int, Path(title='ID of inventory item to retrieve')]):
    return inventory.get_item_by_id(item_id)


@app.get('/inventory/', status_code=status.HTTP_200_OK)
def get_items(start: Annotated[int, Query(title='Start index')], 
              end: Annotated[int, Query(title='End index')] 
              ):
    return inventory.get_subset(start, end)


@app.post('/inventory', status_code=status.HTTP_201_CREATED)
def addInvItem(item : InventoryItem) -> str:
    print('add to inv')
    inventory.add_item(item)
    return ("success")


@app.delete('/inventory/{id}', status_code=status.HTTP_202_ACCEPTED)
def remove_item(id : int):
    print(f'remove item %d',id)
    return {}
    
