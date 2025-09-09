def binary_search(array: list, item: int) -> int | None:
    start = 0
    end = len(array) - 1
    
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == item:
            return mid
        if array[mid] > item:
            end = mid - 1
        else:
            start = mid + 1

    return None
