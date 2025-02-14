import unittest
from double_linked_list import DoubleLinkedList


class TestDoubleLinkedList(unittest.TestCase):
    """Тесты для класса DoubleLinkedList."""

    def setUp(self):
        self.dll = DoubleLinkedList()

    def test_insert_at_index(self):
        self.dll.insert(10)
        self.dll.insert_at_index(1, 20)
        self.assertEqual(self.dll.len_ll(), 2)

    def test_remove_node_index(self):
        self.dll.insert(10)
        self.dll.insert(20)
        self.dll.remove_node_index(1)
        self.assertEqual(self.dll.len_ll(), 1)

    def test_remove_node_data(self):
        self.dll.insert(10)
        self.dll.insert(20)
        self.dll.remove_node_data(20)
        self.assertEqual(self.dll.len_ll(), 1)

    def test_len_ll(self):
        self.dll.insert(10)
        self.dll.insert(20)
        self.assertEqual(self.dll.len_ll(), 2)

    def test_contains_from_head(self):
        self.dll.insert(10)
        self.dll.insert(20)
        self.assertTrue(self.dll.contains_from_head(20))

    def test_contains_from_tail(self):
        self.dll.insert(10)
        self.dll.insert(20)
        self.assertTrue(self.dll.contains_from_tail(10))


if __name__ == "__main__":
    unittest.main()