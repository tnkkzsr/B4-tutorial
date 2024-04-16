"""
入力
1 行目にカードの枚数 N が与えられます。 2 行目に N 枚のカードが与えられます。各カードは絵柄と数字のペアを表す２文字であり、隣合うカードは１つの空白で区切られています。

出力
1 行目に、バブルソートによって整列されたカードを順番に出力してください。隣合うカードは１つの空白で区切ってください。
2 行目に、この出力が安定か否か（Stable またはNot stable）を出力してください。
3 行目に、選択ソートによって整列されたカードを順番に出力してください。隣合うカードは１つの空白で区切ってください。
4 行目に、この出力が安定か否か（Stable またはNot stable）を出力してください。
"""




def bubble_sort(cards):
    n = len(cards)
    swapped = False
    for i in range(n):
        for j in range(n-1, i, -1):
            if int(cards[j][1]) < int(cards[j-1][1]):
                cards[j], cards[j-1] = cards[j-1], cards[j]
                swapped = True
        if not swapped:
            break
    return cards

def select_sort(cards):
    for i in range(len(cards)):
        min_index  = i
        for j in range(i+1, len(cards)):
            if int(cards[j][1]) < int(cards[min_index][1]):
                min_index = j
        cards[i], cards[min_index] = cards[min_index], cards[i]
    return cards


def is_stable(original, sorted_cards):
    for i in range(len(original)):
        for j in range(i+1, len(original)):
            for a in range(1, len(original)):
                for b in range(a+1, len(original)):
                    if original[i][1] == original[j][1] and original[i] == sorted_cards[b] and original[j] == sorted_cards[a]:
                        return False
    return True

if __name__ == "__main__":
    n = int(input())
    cards = input().split()
    original = cards.copy()
    bubble_sorted = bubble_sort(cards.copy())
    print(" ".join(bubble_sorted))
    print("Stable" if is_stable(original, bubble_sorted) else "Not stable")
    select_sorted = select_sort(original.copy())
    print(" ".join(select_sorted))
    print("Stable" if is_stable(original, select_sorted) else "Not stable")
