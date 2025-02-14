class Node:
    """Класс узла двусвязного списка."""

    def __init__(self, data):
        """
        Конструктор узла двусвязного списка.

        :param data: Данные, хранящиеся в узле.
        """
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    """Класс двусвязного списка."""

    def __init__(self):
        """
        Конструктор двусвязного списка.

        :ivar head: Указатель на первый элемент списка.
        :ivar tail: Указатель на последний элемент списка.
        """
        self.head = None
        self.tail = None

    def insert(self, new_data):
        """
        Вставка нового узла в начало списка.

        :param new_data: Данные для вставки.
        """
        new_node = Node(new_data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def print_ll(self):
        """
        Печать списка от головы к хвосту.
        """
        current = self.head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


class DoubleLinkedList(LinkedList):
    """Класс-наследник двусвязного списка с расширенной функциональностью."""

    def print_ll_from_tail(self):
        """
        Печать списка в обратном порядке (от хвоста к голове).
        """
        current = self.tail
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

    def insert_at_index(self, index, data):
        """
        Вставка элемента по указанному индексу.

        :param index: Индекс для вставки.
        :param data: Данные для вставки.
        :raises: IndexError, если индекс выходит за пределы списка.
        """
        if index < 0:
            raise IndexError("Индекс не может быть отрицательным.")

        new_node = Node(data)
        if index == 0:
            self.insert(data)
            return

        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Индекс выходит за пределы списка.")
            current = current.next

        if current is None:
            raise IndexError("Индекс выходит за пределы списка.")

        new_node.next = current.next
        if current.next is not None:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current

    def remove_node_index(self, index):
        """
        Удаление элемента по указанному индексу.

        :param index: Индекс для удаления.
        :raises: IndexError, если индекс выходит за пределы списка.
        """
        if index < 0 or self.head is None:
            raise IndexError("Индекс выходит за пределы списка.")

        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return

        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Индекс выходит за пределы списка.")
            current = current.next

        if current is None:
            raise IndexError("Индекс выходит за пределы списка.")

        if current.prev is not None:
            current.prev.next = current.next
        if current.next is not None:
            current.next.prev = current.prev

    def remove_node_data(self, data):
        """
        Удаление элемента по данным узла.

        :param data: Данные для удаления.
        :raises: ValueError, если элемент не найден.
        """
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                return
            current = current.next
        raise ValueError("Элемент не найден.")

    def len_ll(self):
        """
        Получение длины списка.

        :return: Длина списка.
        """
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def contains_from_head(self, data):
        """
        Проверка наличия элемента с головы списка.

        :param data: Данные для поиска.
        :return: True, если элемент найден, иначе False.
        """
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def contains_from_tail(self, data):
        """
        Проверка наличия элемента с хвоста списка.

        :param data: Данные для поиска.
        :return: True, если элемент найден, иначе False.
        """
        current = self.tail
        while current is not None:
            if current.data == data:
                return True
            current = current.prev
        return False

    def contains_from(self, data, from_head=True):
        """
        Проверка наличия элемента с начала или с хвоста списка.

        :param data: Данные для поиска.
        :param from_head: Если True, поиск с головы, иначе с хвоста.
        :return: True, если элемент найден, иначе False.
        """
        if from_head:
            return self.contains_from_head(data)
        else:
            return self.contains_from_tail(data)