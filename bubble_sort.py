def bubble_sort(array,comp_func):
    """
    """
    print("bubble sort")
    n = len(array)
    swapped = False
    for i in range(n):
        for j in range(n-1, i, -1):
            if comp_func(array[j-1], array[j]):
                array[j], array[j-1] = array[j-1], array[j]
                swapped = True
        if not swapped:
            break
    print(array)

# 一度も交換が行われなかった場合、ソートが完了しているため、処理を終了することで計算量を削減できる

# lambda関数の定義
assending = lambda x,y : x > y
descending = lambda x,y : x < y
custom = lambda x,y : x % 2 > y % 2 or (x % 2 == y % 2 and x > y)

if __name__ == "__main__":
    # doctestでのテスト
    import doctest
    doctest.testmod()
    #　動作確認
    bubble_sort([5,2,4,6,1,3],assending)
    bubble_sort([5,2,4,6,1,3],descending)
    bubble_sort([5,2,4,6,1,3],custom)
    