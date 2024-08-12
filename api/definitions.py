from pydantic import BaseModel
from typing import Optional, List


class InventoryItem(BaseModel):
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
        

class Inventory(BaseModel):
    invList : Optional[List[InventoryItem]] = []

    def addItem(self, item : InventoryItem):
        self.invList.append(item)

# class WishListItem(BaseModel):
#     itemName : str
#     size : int
#     units : str
#     quantity : int


# class WishList(BaseModel):
#     wishList : List[WishListItem]

#     def addItem(self, item):
#         self.wishList.append(item)


