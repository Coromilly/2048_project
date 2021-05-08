import unittest
from logic import get_number_from_index, get_empty_list, get_index_from_number
from logic import is_zero_in_mas, move_left, move_right, move_up, move_down, can_move


class Tests2048(unittest.TestCase):

    def test_get_number_from_index_1(self):
        self.assertEqual(get_number_from_index(1, 2), 7)
        self.assertEqual(get_number_from_index(3, 3), 16)

    def test_get_empty_list_1(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_get_empty_list_2(self):
        a = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [1, 2, 3, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_get_empty_list_3(self):
        a = []
        mas = [
            [1, 2, 3, 4],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_get_index_from_number(self):
        self.assertEqual(get_index_from_number(7), (1, 2))
        self.assertEqual(get_index_from_number(16), (3, 3))
        self.assertEqual(get_index_from_number(1), (0, 0))

    def test_is_zero_in_mas_1(self):
        mas = [
            [1, 2, 3, 4],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        self.assertEqual(is_zero_in_mas(mas), False)

    def test_is_zero_in_mas_2(self):
        mas = [
            [1, 2, 3, 4],
            [1, 0, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        self.assertEqual(is_zero_in_mas(mas), True)

    def test_is_zero_in_mas_3(self):
        mas = [
            [0, 2, 3, 4],
            [1, 1, 1, 0],
            [1, 0, 1, 1],
            [0, 0, 0, 1]
        ]
        self.assertEqual(is_zero_in_mas(mas), True)

    def test_move_left_1(self):
        mas = [
            [2, 2, 0, 0],
            [0, 4, 4, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        rezult = [
            [4, 0, 0, 0],
            [8, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_left(mas), (rezult, 12))

    def test_move_left_2(self):
        mas = [
            [2, 4, 4, 2],
            [4, 0, 0, 2],
            [0, 0, 0, 0],
            [8, 8, 4, 4]
        ]
        rezult = [
            [2, 8, 2, 0],
            [4, 2, 0, 0],
            [0, 0, 0, 0],
            [16, 8, 0, 0]
        ]
        self.assertEqual(move_left(mas), (rezult, 32))

    def test_move_right_1(self):
        mas = [
            [2, 2, 0, 0],
            [0, 4, 4, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        rezult = [
            [0, 0, 0, 4],
            [0, 0, 0, 8],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_right(mas), (rezult, 12))

    def test_move_right_2(self):
        mas = [
            [2, 4, 4, 2],
            [4, 0, 0, 2],
            [0, 0, 0, 0],
            [8, 8, 4, 4]
        ]
        rezult = [
            [0, 2, 8, 2],
            [0, 0, 4, 2],
            [0, 0, 0, 0],
            [0, 0, 16, 8]
        ]
        self.assertEqual(move_right(mas), (rezult, 32))

    def test_move_up(self):
        mas = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0]
        ]
        rezult = [
            [4, 8, 4, 2],
            [8, 0, 0, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_up(mas), (rezult, 24))

    def test_move_down(self):
        mas = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0]
        ]
        rezult = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 0, 0, 2],
            [8, 8, 4, 4]
        ]
        self.assertEqual(move_down(mas), (rezult, 24))

    def test_can_move_1(self):
        mas = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0]
        ]
        self.assertEqual(can_move(mas), True)

    def test_can_move_2(self):
        mas = [
            [2, 4, 8, 2],
            [9, 7, 11, 10],
            [11, 13, 12, 51],
            [54, 48, 73, 22]
        ]
        self.assertEqual(can_move(mas), False)


if __name__ == 'main':
    unittest.main()
