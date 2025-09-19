from random import randint
from algorithm import linear_search


FLAGS = (1000, 5000, 10000, 50000, 100000, 500000, 1000000)
NUMBER_OF_TESTS = 100

def test_binary_search():

    for flag in FLAGS:
        array = [i for i in range(flag+1)]
        total_results = 0
        
        for i in range(NUMBER_OF_TESTS):
            item = randint(1, flag)
            result = linear_search(array, item)
            total_results += result.operations

        med = total_results // NUMBER_OF_TESTS
        
        with open("output.txt", "a") as file:
            file.write(f"Array size: {flag}, Average operations: {med}\n")

test_binary_search()
