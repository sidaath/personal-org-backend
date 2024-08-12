from pydantic import BaseModel
from typing import Optional, List


class InventoryItem(BaseModel):
    id : int
    itemName : str
    size: int
    units : str
    quantity : int
    expDate : str

    def setExpDate(self, newExpDate : str):
        self.expDate = newExpDate

    def decrement(self):
        self.quantity = self.quantity - 1
    
    def increment(self):
        self.quantity = self.quantity + 1
        

class CheckListItem(BaseModel):
    id : int
    itemName : str
    size : int
    units : str
    quantity : int
