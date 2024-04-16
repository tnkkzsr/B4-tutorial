"""ALDS1_1: 挿入ソート
配列に対して挿入ソートを行う
"""


def insertion_sort(arr: list[int]):
    """
    配列に対して挿入ソートを行う
    >>> insertion_sort([5,2,4,6,1,3])
    insert sort
    [1, 2, 3, 4, 5, 6]
    >>> insertion_sort([31,41,59,26,41,58])
    insert sort
    [26, 31, 41, 41, 58, 59]
    """
    print("insert sort")
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# doctestでのテスト
if __name__ == "__main__":
    # doctestでのテスト
    import doctest
    doctest.testmod()
    #　動作確認
    insertion_sort([5,2,4,6,1,3])
    






    