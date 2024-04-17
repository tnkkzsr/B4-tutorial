"""問題3における双方向連結リストの実装"""


class DoublyLinkedNode:
    """
    双方向連結リストのノードを表すクラス
    """

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    双方向連結リストを表すクラス
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        """
        リストの先頭にノードを挿入する
        """
        # 新しいノードを作成
        new_node = DoublyLinkedNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def bubble_sort(self):
        """
        バブルソートを行う
        """

        start = None # ソートされた範囲の開始点

        while start != self.tail:
            swapped = False
            current = self.tail
            while current.prev != start:
                next_node = current.prev
                if current.value < next_node.value:
                    current.value , next_node.value  = next_node.value , current.value
                    swapped = True
                current = next_node
            if not swapped:
                break
            start = current




    def insert_sort(self):
        """
        挿入ソートを行う
        """
        if not self.head or not self.head.next:
            return
        
        sorted_tail = self.head
        current = self.head.next

        # currentは二番目の要素から後ろにずらしていって無くなったら終わり
        while current:
            #次のcurrentを先に設定しておく
            next_current = current.next

            #ソート済みの末尾 より currentが小さい時
            if current.value < sorted_tail.value:
                #ソート済みの末尾をpositionに格納
                position = sorted_tail
                # currentがpositionより大きくなるまでpositionを前にずらす
                while position and position.value > current.value:
                    position = position.prev
                
                #currentを取り出す
                if current.next:
                    current.next.prev = current.prev
                current.prev.next = current.next

                # positionがある場合、positionの後ろに入れる
                if position:
                    current.prev = position
                    current.next = position.next
                    if position.next:
                        position.next.prev = current
                    position.next = current
                # positionがない=先頭にcurrentをいれる
                else:
                    current.next = self.head
                    current.prev = None
                    self.head.prev = current 
                    self.head  =current
            
            else:
                sorted_tail  =current
            current = next_current

    def delete(self, value):
        """
        特定の値を持つ最初のノードを削除する。
        """
        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                # 先頭のノードの場合
                if current_node.prev is None:
                    self.head = current_node.next
                    if self.head is not None:
                        self.head.prev = None
                    else:  # リストが空になる場合
                        self.tail = None

                # 末尾のノードの場合
                elif current_node.next is None:
                    self.tail = current_node.prev
                    self.tail.next = None

                # それ以外の場合
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                break
            current_node = current_node.next

    def delete_first(self):
        """
        リストの先頭のノードを削除する
        """
        if self.head.next is None:  # 削除後のリストが空になる場合
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_last(self):
        """
        リストの末尾のノードを削除する。
        """
        if self.tail.prev is None:  # 削除後のリストが空になる場合
            self.head = None

            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def output(self):
        """
        リストの全要素を出力して、listで返す
        """
        list = []
        current_node = self.head
        while current_node is not None:
            list.append(str(current_node.value))
            current_node = current_node.next
        print(" ".join(list))
        


# def execute_command(linked_list, commands):
#     """
#     コマンドを解析して実行する
#     """
#     for command in commands:
#         command_list = command.split()
#         command_type = command_list[0]
#         value = command_list[1] if len(command_list) > 1 else None

#         match command_type:
#             case "insert":
#                 linked_list.insert(value)
#             case "delete":
#                 linked_list.delete(value)
#             case "deleteFirst":
#                 linked_list.delete_first()
#             case "deleteLast":
#                 linked_list.delete_last()
#             case _:
#                 raise ValueError("Invalid command type")

def test_doubly_linked_list_sort():
    # テストケース 1: 通常のケース
    dll = DoublyLinkedList()
    elements = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    for elem in elements:
        dll.insert(elem)
    dll.insert_sort()
    dll.output()

    # テストケース 2: 空のリスト
    dll_empty = DoublyLinkedList()
    dll_empty.insert_sort()
    dll_empty.output()

    # テストケース 3: 既にソート済みのリスト
    dll_sorted = DoublyLinkedList()
    for elem in sorted(elements):
        dll_sorted.insert(elem)
    dll_sorted.insert_sort()
    dll_sorted.output()

    # テストケース 4: 逆順リスト
    dll_reverse = DoublyLinkedList()
    for elem in sorted(elements, reverse=True):
        dll_reverse.insert(elem)
    dll_reverse.insert_sort()
    dll_reverse.output()

def test_doubly_linked_list_bubble_sort():
    # インスタンスの作成
    dll = DoublyLinkedList()

    # テストケース 1: 通常のケース
    elements = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    for elem in elements:
        dll.insert(elem)
    dll.bubble_sort()
    dll.output()

    # テストケース 2: 空のリスト
    dll_empty = DoublyLinkedList()
    dll_empty.bubble_sort()
    dll_empty.output()

    # テストケース 3: 既にソート済みのリスト
    dll_sorted = DoublyLinkedList()
    sorted_elements = sorted(elements)
    for elem in reversed(sorted_elements):  # 逆順に挿入してからソートする
        dll_sorted.insert(elem)
    dll_sorted.bubble_sort()
    dll_sorted.output()

    # テストケース 4: 逆順リスト
    dll_reverse = DoublyLinkedList()
    for elem in elements:
        dll_reverse.insert(elem)  # 先頭に挿入するため、自然と逆順になる
    dll_reverse.bubble_sort()
    dll_reverse.output()


test_doubly_linked_list_bubble_sort()

test_doubly_linked_list_sort()
