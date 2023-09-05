class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.len_list_of_list = len(list_of_list)

    def __iter__(self):
        self.cursor = 0
        self.counter = -1
        return self

    def __next__(self):
        self.counter += 1
        if len(self.list_of_list[self.cursor]) == self.counter:
            self.counter = 0
            self.cursor += 1
            if self.cursor == self.len_list_of_list:
                raise StopIteration
        return self.list_of_list[self.cursor][self.counter]

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