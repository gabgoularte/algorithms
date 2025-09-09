from binary_search_algorithm import binary_search


def test_binary_search():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert binary_search(array, 5) == 4
    assert binary_search(array, 10) is None
    assert binary_search([], 0) is None
    assert binary_search([1], 1) == 0

    print("All tests passed.")

if __name__ == "__main__":
    test_binary_search()
