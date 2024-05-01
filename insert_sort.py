"""ALDS1_1: 挿入ソート
配列に対して挿入ソートを行う
"""


def insertion_sort(arr: list[int], comp_func):
    """
    配列に対して挿入ソートを行う
    
    """
    print("insert sort")
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and comp_func(arr[j], key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print(arr)
    
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
    insertion_sort([5,2,4,6,1,3],assending)
    insertion_sort([5,2,4,6,1,3],descending)
    insertion_sort([5,2,4,6,1,3],custom)
    






    