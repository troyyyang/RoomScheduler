from models import *
from controller import *
from view import *
from datetime import datetime
import unittest


class TestMinStandController:
    def test_generate_schedule(self):
        mc = MinStandController()
        a = Room("a", 2)
        b = Room("b", 4)
        c = Room("c", 6)
        d = Room("d", 8)
        e = Room("e", 10)

        m1 = Meeting(
            datetime(2018, 8, 18, 9), datetime(2018, 8, 18, 12), 3, "project")
        m2 = Meeting(
            datetime(2018, 8, 18, 9), datetime(2018, 8, 18, 11), 4, "project2")
        m3 = Meeting(
            datetime(2018, 8, 18, 9), datetime(2018, 8, 18, 10), 7, "project3")

        mc.generate_schedule([c, d, a, e, b], [m3, m1, m2])
        mc.view.display()
