from pydantic import BaseModel

class InventoryItem(BaseModel):
    id : int
    itemName : str
    size: int
    units : str
    quantity : int
    expDate : str | None
    price : int | None

    def setExpDate(self, newExpDate : str):
        self.expDate = newExpDate

    def decrement(self):
        self.quantity = self.quantity - 1
    
    def increment(self):
        self.quantity = self.quantity + 1