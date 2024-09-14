import unittest
from api.inventory.inventory import items, get_all_items, get_item_by_id, get_subset, add_item, remove_item
from api.model.inventoryItemModel import InventoryItem


class TestInv(unittest.TestCase):
    def test_get_all_items(self):
        self.assertListEqual(get_all_items(), items, 'failed : get_all_items_() ')

    def test_get_item_by_id(self):
        item : InventoryItem | None = get_item_by_id(items[1].id)
        self.assertEqual(item, items[1], 'failed : get_item_by_id()')

        idx_out_of_range : int = len(items) + 10
        item = get_item_by_id(idx_out_of_range)
        self.assertEqual(item, None)

    def test_get_subset(self):
        subset: list[InventoryItem] = get_subset(1,2)
        subset2 = items[1:2]
        self.assertListEqual(subset, subset2, 'failed : get_subset()')

        subset = get_subset(100, 200)
        subset2 = []
        self.assertListEqual(subset, subset2, 'failed : get_subset()')

    def test_add_item(self):
        newItem : InventoryItem = InventoryItem(id=0, itemName='Test add 1', size=10, units='kg', quantity=1, expDate='2024-11-29', price=None)
        res1 : int = add_item(newItem=newItem)

        newItem2 : InventoryItem = InventoryItem(id=0, itemName='Test add 2', size=20, units='kg', quantity=1, expDate='2024-11-31', price=None)
        res2 : int = add_item(newItem2)

        x = get_item_by_id(res1)
        self.assertEqual(x, newItem)

        y = get_item_by_id(res2)
        self.assertEqual(y, newItem2)

    def test_remove_item(self):
        tempItem : InventoryItem = InventoryItem(id=1, itemName='temp 1', size=10, units='kg', quantity=10, price=None, expDate=None)
        res = add_item(tempItem)
        self.assertNotEqual(res, None, 'faild : remove_item() at add_item()')

        item_in_list = get_item_by_id(res)
        self.assertEqual(item_in_list, tempItem, 'failed : remove_item() at get_item_by_id()')

        rem_res = remove_item(res)
        self.assertEqual(rem_res, 0, 'failed : remove_item() at remove_item')

        temp_items = [item for item in items if item.id != res]
        self.assertEqual(temp_items, items, 'failed : remove_item()')


if __name__ == "__name__":
    unittest.main()