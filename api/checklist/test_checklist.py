import unittest
from unittest.mock import patch
from api.model.checkListItemModel import CheckListItem
import api.checklist.checklist as checklist

test_checklist : list[CheckListItem] = []
test_checklist.append(CheckListItem(id=901, itemName="CHK 1", size=10, units="kg",quantity=1))
test_checklist.append(CheckListItem(id=902, itemName="CHK 2", size=10, units="L",quantity=12))
test_checklist.append(CheckListItem(id=903, itemName="CHK 3", size=10, units="ml",quantity=31))



class GetAllItems(unittest.TestCase):
    "Test get_checklist function"

    @patch('api.checklist.checklist.items2', test_checklist)
    def test_get_checklist(self):
        self.assertListEqual(checklist.get_all_items(), test_checklist, 'failed : get_all_items_() ')

    @patch('api.checklist.checklist.items2', [])
    def test_empty_checklist(self):
        self.assertListEqual(checklist.get_all_items(), [])


@patch('api.checklist.checklist.items2', test_checklist)
@patch('api.checklist.checklist.__CHK_ID__',100)
class AddNewChecklistItem(unittest.TestCase):
    "Test add_new_checklist_item function"

    def test_add_new_item(self):
        new_item = CheckListItem(id=1, itemName="T1", size=250,units='ml',quantity=10)
        ret : int = checklist.add_new_checklist_item(new_item)
        self.assertEqual(ret, 100)

        new_item2 = CheckListItem(id=1, itemName="T2", size=250,units='ml',quantity=10)
        ret2 : int = checklist.add_new_checklist_item(new_item2)
        self.assertEqual(ret2, 101)




@patch('api.checklist.checklist.items2', test_checklist)
@patch('api.checklist.checklist.__CHK_ID__', 200)
class CheckItem(unittest.TestCase):
    "test check_item function"

    def test_check_non_existent_item(self):
        return_val : int = checklist.check_item(1, '', None)
        self.assertEqual(return_val, -1)

    @patch('api.checklist.checklist.add_to_inv')
    def test_check_existing_item(self, mock_add_to_inv ):
        add_item : CheckListItem = CheckListItem(id=200,itemName='CH1',quantity=10,size=20,units='L')
        test_checklist.append(add_item)
        mock_add_to_inv.return_value = 20
        function_ret_val = checklist.check_item(200, '', 10)
        self.assertEqual(function_ret_val,20)


@patch('api.checklist.checklist.items2', test_checklist)
@patch('api.checklist.checklist.__CHK_ID__',300)
class RemoveChecklistItem(unittest.TestCase):
    "Test remove_checklist_item function"

    def test_remove_existing_item(self):
        init = test_checklist
        add_item = CheckListItem(id=300, itemName='rm1',quantity=10,size=200,units='L')
        test_checklist.append(add_item)
        res = checklist.remove_checklist_item(300)
        self.assertGreater(res, -1)

    def test_remove_non_existing_item(self):
        res : int= checklist.remove_checklist_item(300)
        self.assertEqual(res, -1)
