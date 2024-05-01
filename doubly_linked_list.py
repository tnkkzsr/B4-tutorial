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
        self._length = 0
        
    def __len__(self):
        return self._length

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
        self._length += 1
            
    def append(self, value):
        """ リストの末尾に新しいノードを追加する """
        new_node = DoublyLinkedNode(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._length += 1

    
            
            
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
        self._length -= 1

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
        self._length -= 1
        
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
        self._length -= 1
        
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
        
    def insert_sort(self):
        """
        挿入ソートを行う
        """
        if not self.head or not self.head.next:
            return  # リストが空または一要素のみの場合はソート不要
    
        sorted_tail = self.head  # ソート済み部分の最後のノードを追跡
        current = self.head.next  # 最初のソート対象ノード
        sorted_length = 1  # ソート済み部分の長さ
        
        # リストの終端まで繰り返す
        while current:
            next_current = current.next  # 現在のノードの次のノードを保存
            
            # 現在のノードがソート済み部分の最後のノードより大きいかどうか
            if not current.value < sorted_tail.value:
                sorted_tail = current  # 現在のノードをソート済みとして扱い、次へ進む
                current = next_current
                sorted_length += 1
                continue
            
            if sorted_length == len(self):
                break

            # ソート済み部分内で現在のノードより大きい最初のノードを見つける
            position = sorted_tail
            while position and position.value > current.value:
                position = position.prev  # 適切な挿入位置を探すため後方へ移動

            # 現在のノードを一旦リストから外し、見つけた位置の後ろに挿入
            self.remove_node(current)
            self.insert_after(position, current)

            current = next_current  # 次のノードへ進む
            
    def remove_node(self,node):
        """指定されたノードを削除する"""
        if node.next: 
            node.next.prev = node.prev # ノードの次のノードのprevを更新
        if node.prev: 
            node.prev.next = node.next # ノードの前のノードのnextを更新
        if node == self.head:
            self.head = node.next # ノードが先頭の場合、headを更新
            if self.head:
                self.head.prev = None
        if node == self.tail:
            self.tail = node.prev # ノードが末尾の場合、tailを更新
            if self.tail:
                self.tail.next = None
        node.next = None
        node.prev = None
        self._length -= 1
            
    def insert_after(self, position, node):
        """指定された位置の後ろにノードを挿入する"""
        if position is None:
            # リストの先頭に挿入
            node.next = self.head
            node.prev = None
            if self.head:
                self.head.prev = node
            self.head = node
            if self.tail is None:
                self.tail = node  # リストが空だった場合
        else:
            # position の後ろに挿入
            node.next = position.next
            node.prev = position
            if position.next:
                position.next.prev = node
            position.next = node
            if position == self.tail:
                self.tail = node  # 新しい末尾ノードとして更新
        self._length += 1

    def bubble_sort(self):
        """
        バブルソートを使用してリストをソートする
        """
        if not self.head or not self.head.next:
            return

        for _ in range(len(self)- 1):
            current = self.head
            swapped = False
            for _ in range(len(self) - 1):
                if current.value > current.next.value:
                    self._swap_nodes(current, current.next)
                    swapped = True
                else:
                    current = current.next
            if not swapped:
                break


    def _swap_nodes(self, node1, node2):
        """
        二つの隣接ノードの位置を交換する
        """
        if node1.prev: 
            node1.prev.next = node2
        if node2.next:
            node2.next.prev = node1
        node1.next = node2.next
        node2.prev = node1.prev

        node2.next = node1
        node1.prev = node2

        # ヘッドとテイルの更新を確認する
        if node2.prev is None:
            self.head = node2
        if node1.next is None:
            self.tail = node1

    

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

  

def test_doubly_linked_list_bubble_sort():
    # インスタンスの作成
    dll = DoublyLinkedList()

    # テストケース 1: 通常のケース
    elements = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    for elem in elements:
        dll.insert(elem)
    dll.bubble_sort()
    dll.output()



# test_doubly_linked_list_bubble_sort()

test_doubly_linked_list_sort()

# dll = DoublyLinkedList()
# elements = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# for elem in elements:
#     dll.insert(elem)
# dll.bubble_sort()
# dll.output()


