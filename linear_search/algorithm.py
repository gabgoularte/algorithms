import sys
sys.path.append('/Users/aluno/Documents/GC_IA_Dados/code/Scripts/algorithms/')
from random import randint
from models import Response


def linear_search(array: list, item: int) -> Response:
    response = Response()

    for index, element in enumerate(array):
        if element == item:
            response.found = True
            response.index = index
            response.operations += 1
            return response
        
        else:
            response.operations += 1
    return response