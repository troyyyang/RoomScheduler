from models import *
from view import *
from datetime import *
import heapq

class MinStandController:

    def __init__(self):
        self.cal = Calendar()
        self.view = CommandLineView(self.cal)

    def generate_schedule(self, rooms, meetings):
        for room in rooms:
            self.cal.add_room(room)
        meetings.sort(reverse=True)

        rooms.sort()
        for meeting in meetings:

            print("Assigning meeting " + meeting.get_name())
            left = 0
            right = len(rooms)-1
            # print("Right starts as " + str(right))
            # print("Left starts as " + str(left))
            while(left + 1 < right):

                mid = left + (right-left)//2
                if (mid == 0):
                    break
                if (mid > 75):
                    break
                if (rooms[mid].get_num_chairs() >= meeting.get_num_people()):
                    right = mid
                    # print( "right " + str(right))
                else:
                    left = mid
            #post processing
            added = False
            while (right < len(rooms)):
                if (self.cal.add_meeting(meeting, rooms[right])):
                    # print("Added meeting " + meeting.get_name() + " to room " + rooms[right].get_name())
                    added = True
                    break
                else:
                    right+=1
            if not added:
                while (left >= 0):
                    if (self.cal.add_meeting(meeting, rooms[right])):
                        added = True
                        break
                    else:
                        left-=1
            if not added:
                #no rooms
                print("No available rooms at this time")
                return 0



mc = MinStandController()
a = Room("a", 2)
b = Room("b", 4)
c = Room("c", 6)
d = Room("d", 8)
e = Room("e", 10)

m1 = Meeting(datetime(2018, 8, 18, 9), datetime(2018, 8, 18, 12), 3, "project")
m2 = Meeting(datetime(2018, 8, 18, 9), datetime(2018, 8, 18, 11), 4, "project2")
m3 = Meeting(datetime(2018, 8, 18, 9), datetime(2018, 8, 18, 10), 7, "project3")

mc.generate_schedule([c, d, a, e, b], [m3, m1, m2])
mc.view.display()
