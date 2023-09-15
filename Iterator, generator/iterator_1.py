class FlatIterator:

    def __init__(self, list_of_list):

        self.list = list_of_list
        self.len_list = len(list_of_list)
        self.cursor_list = -1

    def __iter__(self):

        self.cursor_list += 1
        self.element_cursor_list = 0
        return self

    def __next__(self):

        if self.element_cursor_list == len(self.list[self.cursor_list]):
            iter(self)
        if self.cursor_list == self.len_list:
            raise StopIteration
        self.element_cursor_list += 1
        result = self.list[self.cursor_list][self.element_cursor_list - 1]
        return result

def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
