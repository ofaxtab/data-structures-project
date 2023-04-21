"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from unittest import TestCase

from src.stack import Node, Stack


class NodeTest(TestCase):
    def test_creation(self):
        n1 = Node(5, None)
        n2 = Node('a', n1)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')
        self.assertIsInstance(n2.next_node, Node)
        self.assertIsInstance(n1, Node)


class StackTest(TestCase):
    def test_creation(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(stack.top.data, 'data3')
        self.assertEqual(stack.top.next_node.data, 'data2')
        self.assertEqual(stack.top.next_node.next_node.data, 'data1')
        with self.assertRaises(AttributeError):
            stack.top.next_node.next_node.next_node.data

    def test_stack_pop(self):
        stack = Stack()
        stack.push('data1')
        self.assertEqual(stack.pop(), 'data1')
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(stack.pop(), 'data3')
        self.assertEqual(stack.pop(), 'data2')
        self.assertEqual(stack.pop(), 'data1')
        self.assertIs(stack.pop(), None)

