from merge_sort import merge_sort


def test_empty():
    assert merge_sort([], 0) == -1


def test_1():
    a = [-67, -44, -2, 33, 45, 67, 134]
    assert merge_sort(a, 1) == -1


def test_0():
    a = [-67, -44, -2, 33, 45, 67, 134]
    assert merge_sort(a, 0) == -1


def test__1():
    a = [-67, -44, -2, 33, 45, 67, 134]
    assert merge_sort(a, -1) == -1


def test_2():
    a = [-67, -44, -2, 33, 45, 67, 134]
    assert merge_sort(a, 2) == -1


def test__2():
    a = [-67, -44, -2, 33, 45, 67, 134]
    assert merge_sort(a, -2) == 2


def test_134():
    a = [-67, -44, -2, 33, 45, 67, 134]
    assert merge_sort(a, 134) == 6


def test_67():
    a = [-67, -44, -2, 33, 45, 67, 134]
    assert merge_sort(a, 67) == 5


def test__67():
    a = [-67, -44, -2, 33, 45, 67, 134]
    assert merge_sort(a, -67) == 0


def test_first():
    a = [1, 1, 1, 2, 2, 2, 2, 2, 2]
    assert merge_sort(a, 2) == 3


def test_first1():
    a = [1, 1, 1, 2, 2, 2, 2, 2, 2]
    assert merge_sort(a, 1) == 0


def test_last():
    a = [1, 1, 1, 2, 2, 2, 2, 2, 2, 3]
    assert merge_sort(a, 3) == 9
