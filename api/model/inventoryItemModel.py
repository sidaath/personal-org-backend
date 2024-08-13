from pydantic import BaseModel
from model.constants import null_string

class InventoryItem(BaseModel):
    id : int
    itemName : str
    size: int
    units : str
    quantity : int
    expDate : str = null_string
    price : int | str = null_string

    def setExpDate(self, newExpDate : str):
        self.expDate = newExpDate

    def decrement(self):
        self.quantity = self.quantity - 1
    
    def increment(self):
        self.quantity = self.quantity + 1