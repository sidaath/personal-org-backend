from pydantic import BaseModel

class CheckListItem(BaseModel):
    id : int
    itemName : str
    size : int
    units : str
    quantity : int
