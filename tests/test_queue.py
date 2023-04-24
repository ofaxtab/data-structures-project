"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from unittest import TestCase

from src.queue import Node, Queue


class NodeTest(TestCase):
    def test_creation(self):
        n1 = Node(5, None)
        n2 = Node('a', n1)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')
        self.assertIsInstance(n2.next_node, Node)
        self.assertIsInstance(n1, Node)


class QueueTest(TestCase):

    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')

    def test_queue_creation(self):
        self.assertIsInstance(self.queue, Queue)

        self.assertEqual(self.queue.head.data, 'data1')
        self.assertEqual(self.queue.head.next_node.data, 'data2')
        self.assertEqual(self.queue.tail.data, 'data3')
        self.assertIs(self.queue.tail.next_node, None)

        with self.assertRaises(AttributeError) as err:
            self.queue.tail.next_node.data
        self.assertEqual(err.exception.args[0], "'NoneType' object has no attribute 'data'")

    def test_queue_deque(self):
        self.assertEqual(self.queue.dequeue(), 'data1')
        self.assertEqual(self.queue.dequeue(), 'data2')
        self.assertEqual(self.queue.dequeue(), 'data3')
        self.assertIs(self.queue.dequeue(), None)

    def test_str(self):
        self.assertEqual(str(self.queue), "data1\ndata2\ndata3")
        self.queue = Queue()
        self.assertEqual(str(self.queue), '')
