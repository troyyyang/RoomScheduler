from models import *
from datetime import datetime
import unittest

class TestCalendar(unittest.TestCase):

    def test_add_room(self):
        c = Calendar()
        self.assertTrue(c.add_room("Curie", 6))
        self.assertFalse(c.add_room("Curie", 6))
        r = Room("Curie", 6)
        self.assertEqual(len(c.get_meetings().keys()), 1)
        self.assertEqual(len(c.get_meetings()[r]), 0)
        self.assertTrue(c.add_room("Turing", 12))
        self.assertEqual(len(c.get_meetings().keys()), 2)

    def test_add_meeting(self):
        c = Calendar()
        c.add_room("Curie", 6)
        c.add_room("Turing", 10)
        r = Room("Curie", 6)
        m = Meeting(datetime(2018, 8, 18, 9), datetime(2018, 8, 18, 10), 2, "project")
        self.assertTrue(c.add_meeting(m, r))
        n = Meeting(datetime(2018, 8, 18, 9, 30), datetime(2018, 8, 18, 10, 30), 2, "project2")
        self.assertFalse(c.add_meeting(n, r))
        l = Meeting(datetime(2018, 8, 18, 8, 30), datetime(2018, 8, 18, 9, 20), 2, "project3")
        self.assertFalse(c.add_meeting(l, r))
        k = Meeting(datetime(2018, 8, 18, 9, 30), datetime(2018, 8, 18, 10, 30), 2, "project4")
        self.assertFalse(c.add_meeting(l, r))
        j = Meeting(datetime(2018, 8, 18, 14, 30), datetime(2018, 8, 18, 15, 30), 2, "project5")
        self.assertTrue(c.add_meeting(j, r))
        self.assertEquals(len(c.get_meetings()[r]), 2)



    def test_check_time_conflicts(self):
        pass

if __name__ == '__main__':
    unittest.main()
