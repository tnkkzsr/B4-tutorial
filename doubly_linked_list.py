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
        return list


def execute_command(linked_list, commands):
    """
    コマンドを解析して実行する
    """
    for command in commands:
        command_list = command.split()
        command_type = command_list[0]
        value = command_list[1] if len(command_list) > 1 else None

        match command_type:
            case "insert":
                linked_list.insert(value)
            case "delete":
                linked_list.delete(value)
            case "deleteFirst":
                linked_list.delete_first()
            case "deleteLast":
                linked_list.delete_last()
            case _:
                raise ValueError("Invalid command type")


# 命令数を受け取る
n = int(input())
# 双方向連結リストを作成
linked_list = DoublyLinkedList()
# 命令を受け取り、処理を行う
commands = [input() for _ in range(n)]
execute_command(linked_list, commands)
linked_list.output()
