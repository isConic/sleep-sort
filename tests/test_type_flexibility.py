from sleep_sort import  sleep_sort
import unittest
import itertools

VERBOSE = True

class TestTypeFlexibility(unittest.TestCase):

    def __permute_and_try(self, numbers, special_message = ""):
        test_cases = list(itertools.permutations(numbers))
        for case in test_cases:

            if VERBOSE == True:
                print(special_message ,case , numbers)

            sleep_sorted_case = sleep_sort(case)
            assert sleep_sorted_case == numbers

    def test_integers(self):
        numbers = sorted([1,2,3,4,5])
        self.__permute_and_try(numbers)

    def test_floats(self):
        numbers = sorted([1.0,2.0,3.0,4.0,5.0])
        self.__permute_and_try(numbers)