from models import *


class CommandLineView:
    def __init__(self, Calendar):
        self.calendar = Calendar

    def display(self):
        schedule = self.calendar.get_meetings()
        for room in schedule:
            print("Room: " + room.get_name())
            for meeting in schedule[room]:
                print(meeting.get_name() + "\nstart time " +
                      str(meeting.get_start_time()) + "\nend time " +
                      str(meeting.get_end_time()) + "\nAttendees: " +
                      str(meeting.get_num_people()) + "\n")
