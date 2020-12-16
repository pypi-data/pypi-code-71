import unittest
import pathlib
import datetime

from pytodotxt import Task

from pter import utils


class FakeSource:
    def __init__(self, tasks):
        self.tasks = tasks
        self.filename = pathlib.Path('/tmp/test.txt')


class TestSorting(unittest.TestCase):
    def testDueSorting(self):
        tasks = [Task(utils.dehumanize_dates("due in a week due:+1w id:1")),
                 Task(utils.dehumanize_dates("due tomorrow due:1 id:2")),
                 Task(utils.dehumanize_dates("due in a month due:+1m id:3")),
                 Task(utils.dehumanize_dates("(A) no due date id:4"))]

        tasks.sort(key=utils.sort_fnc)

        self.assertEqual(tasks[0].attr_id, ['2'])
        self.assertEqual(tasks[1].attr_id, ['1'])
        self.assertEqual(tasks[2].attr_id, ['3'])
        self.assertEqual(tasks[3].attr_id, ['4'])


