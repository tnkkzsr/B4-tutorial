"""選択ソート"""


def select_sort(array):
    """
    配列に対して選択ソートを行う
    最小のやつを左に持っていくイメージ

    >>> select_sort([5,2,4,6,1,3])
    select sort
    [1, 2, 3, 4, 5, 6]
    >>> select_sort([31,41,59,26,41,58])
    select sort
    [26, 31, 41, 41, 58, 59]

    """
    print("select sort")
    for i in range(len(array)):
        min_index  = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    print(array)

# doctestでのテスト
if __name__ == "__main__":
    # doctestでのテスト
    import doctest
    doctest.testmod()
    #　動作確認
    select_sort([5,2,4,6,1,3])