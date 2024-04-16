def bubble_sort(array):
    """
    配列に対してバブルソートを行う
    >>> bubble_sort([5,2,4,6,1,3])
    bubble sort
    [1, 2, 3, 4, 5, 6]
    >>> bubble_sort([31,41,59,26,41,58])
    bubble sort
    [26, 31, 41, 41, 58, 59]
    """
    print("bubble sort")
    n = len(array)
    swapped = False
    for i in range(n):
        for j in range(n-1, i, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                swapped = True
        if not swapped:
            break
    print(array)

# 一度も交換が行われなかった場合、ソートが完了しているため、処理を終了することで計算量を削減できる


if __name__ == "__main__":
    # doctestでのテスト
    import doctest
    doctest.testmod()
    #　動作確認
    bubble_sort([5,2,4,6,1,3])
    