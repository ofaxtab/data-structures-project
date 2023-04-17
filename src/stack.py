class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node



class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.data = []
        self.top = None


    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        previous_data = None
        if len(self.data) > 0:
            previous_data = self.data[-1]
        self.data.append(Node(data, previous_data))
        self.top = self.data[-1]


    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        return self.data.pop()
