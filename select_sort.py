"""選択ソート"""


def select_sort(array, comp_func):
    """
    配列に対して選択ソートを行う
    最小のやつを左に持っていくイメージ
    """
    print("select sort")
    for i in range(len(array)):
        min_index  = i
        for j in range(i+1, len(array)):
            if comp_func(array[min_index], array[j]):
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    print(array)


# Lambda関数の定義
assending = lambda x,y : x > y
descending = lambda x,y : x < y
custom = lambda x,y : x % 2 < y % 2 or (x % 2 == y % 2 and x > y)
# doctestでのテスト
if __name__ == "__main__":
    # doctestでのテスト
    import doctest
    doctest.testmod()
    #　動作確認
    select_sort([5,2,4,6,1,3],assending)
    select_sort([5,2,4,6,1,3],descending)
    select_sort([5,2,4,6,1,3],custom)