import sys
sys.path.append('/Users/aluno/Documents/GC_IA_Dados/code/Scripts/algorithms/')
from models import Response


def binary_search(array: list, item: int) -> Response:
    response = Response()
    
    start = 0
    end = len(array) - 1
    
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == item:
            response.find = True 
            response.index = mid
            response.operations += 1

            return response
        if array[mid] > item:
            end = mid - 1
        else:
            start = mid + 1

        response.operations += 1
    return response