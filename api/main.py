from fastapi import FastAPI, Path, Query, status, Response, Body
from typing import Annotated
import api.inventory.inventory  as inventory
import api.checklist.checklist as checklist
from api.model.inventoryItemModel import InventoryItem
from api.model.checkListItemModel import CheckListItem

app = FastAPI()

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

@app.patch('/inventory', status_code=status.HTTP_202_ACCEPTED)
def modify_inv_item(res :Response, id : int = Body(embed=True), value : str = Body(embed=True)):
    value_map : dict[str, str] = {}
    val_list : list[str] = value.split(';;')
    for i in range(0,len(val_list)-1,2):
        value_map[val_list[i]] = val_list[i+1]

    old_item = inventory.get_item_by_id(id)
    if(type(old_item) == None):
        res.status_code=status.HTTP_404_NOT_FOUND
        return
    else:
        for key,val in value_map.items():
            if key=='quantity':
                ret = inventory.modify_quantity(id, int(val))
    return ('success')


@app.delete('/inventory/{id}', status_code=status.HTTP_202_ACCEPTED)
def remove_item(id : int):
    return {}


########### CHECKLIST ###############

@app.get('/checklist', status_code=status.HTTP_200_OK)
def get_checklist():
    print('get checklist')
    items  = checklist.get_all_items()
    return items

@app.patch('/checklist', status_code=status.HTTP_201_CREATED)
def check_item(res : Response, id : int = Body(embed=True), exp_date : str = Body(default=None, embed=True), quantity : int = (Body(default=None, embed=True))):
    print('check item off checklist')
    inv_id : int = checklist.check_item(id, exp_date, quantity=quantity) 
    if (inv_id > 0):
        return "success"
    else:
        res.status_code = status.HTTP_304_NOT_MODIFIED
        return "fail"
    
@app.post('/checklist', status_code=status.HTTP_201_CREATED)
def add_checklist_item(res : Response, item : CheckListItem):
    print('add item to checklist')
    ret : int = checklist.add_new_checklist_item(item)
    if(ret > 0):
        return ret
    else:
        return "fail"
