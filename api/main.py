from fastapi import FastAPI, Path, Query, status, Response
from typing import Annotated
import api.inventory.inventory  as inventory
import api.checklist.checklist as checklist
from api.model.inventoryItemModel import InventoryItem

app = FastAPI()

@app.get("/")
def test():
    return 'helloooo'

########### INVENTORY ###############
@app.get('/inventory', status_code=status.HTTP_200_OK)
def get_inventory(res : Response):
    print('get inv')
    items = inventory.get_all_items()
    if list != type(items):
        res.status_code = status.HTTP_404_NOT_FOUND
        return {}
    else:
        return items


@app.get('/inventory/{item_id}', status_code=status.HTTP_200_OK)
def get_inv_item(item_id : Annotated[int, Path(title='ID of inventory item to retrieve')], res : Response):
    item: InventoryItem | None = inventory.get_item_by_id(item_id)
    if InventoryItem != type(item):
        res.status_code = status.HTTP_404_NOT_FOUND
        return {}
    else:
        return item


@app.get('/inventory/', status_code=status.HTTP_200_OK)
def get_items(start: Annotated[int, Query(title='Start index')], 
              end: Annotated[int, Query(title='End index')],
              res : Response
              ):
    result = inventory.get_subset(start, end)
    if result == []:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return result
    return result


@app.post('/inventory', status_code=status.HTTP_201_CREATED)
def add_inv_item(item : InventoryItem, res: Response) -> str:
    print('add to inv')
    ret : int = inventory.add_item(item)
    if type(ret) != int:
        res.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return ("fail")
    return ("success")


@app.delete('/inventory/{id}', status_code=status.HTTP_202_ACCEPTED)
def remove_item(id : int):
    return {}


########### CHECKLIST ###############

@app.get('/checklist', status_code=status.HTTP_200_OK)
def get_checklist():
    print('get checklist')
    items  = checklist.get_all_items()
    return items
