import pytest

from sorting.Insertion import insertion_sort

# Test case: [8, 4, 23, 42, 16, 15]
def test_insertion_sort_sample_array():
    input_array = [8, 4, 23, 42, 16, 15]
    expected_sorted_array = [4, 8, 15, 16, 23, 42]
    sorted_array = insertion_sort(input_array)
    assert sorted_array == expected_sorted_array


def test_insertion_sort_reverse_sorted_array():
    input_array = [20, 18, 12, 8, 5, -2]
    expected_sorted_array = [-2, 5, 8, 12, 18, 20]
    sorted_array = insertion_sort(input_array)
    assert sorted_array == expected_sorted_array


def test_insertion_sort_few_uniques_array():
    input_array = [5, 12, 7, 5, 5, 7]
    expected_sorted_array = [5, 5, 5, 7, 7, 12]
    sorted_array = insertion_sort(input_array)
    assert sorted_array == expected_sorted_array


def test_insertion_sort_nearly_sorted_array():
    input_array = [2, 3, 5, 7, 13, 11]
    expected_sorted_array = [2, 3, 5, 7, 11, 13]
    sorted_array = insertion_sort(input_array)
    assert sorted_array == expected_sorted_array
