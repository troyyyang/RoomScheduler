False
class Meeting:
    def __init__(self, start_time, end_time, num_people, name ):
        self.__start_time = start_time
        self.__end_time = end_time
        self.__num_people = num_people
        self.__name = name

    def set_start_time(self, start_time):
        self.__start_time = start_time
    def set_end_time(self, end_time):
        self.__end_time = __end_time
    def set_num_people(self, num_people):
        self.__num_people = num_people
    def set_name(self, name):
        self.__name = name
    def get_start_time(self):
        return self.__start_time
    def get_end_time(self):
        return self.__end_time
    def get_num_people(self):
        return self.__num_people
    def get_name(self):
        return self.__name

    def __eq__(self, other):
        return (self.__name, self.__start_time, self.__end_time, other.__num_people) == (other.get_name(), other.get_start_time(), other.get_end_time(), other.get_num_people())
    def __ne__(self, other):
        return not(self == other)
    def __hash__(self):
        return hash((self.__name, self.__num_people, self.__start_time, self.__end_time))

class Room:
    def __init__(self, name, num_chairs):
        self.__name = name
        self.__num_chairs = num_chairs

    def set_name(self, name):
        self.__name = name
    def set_num_chairs(self, num_chairs):
        self.__num_chairs = num_chairs

    def get_name(self):
        return self.__name
    def get_num_chairs(self):
        return self.__num_chairs

    def __eq__(self, other):
        return (self.__name, self.__num_chairs) == (other.get_name(), other.get_num_chairs())
    def __ne__(self, other):
        return not(self == other)
    def __hash__(self):
        return hash((self.__name, self.__num_chairs))

class Calendar:
    def __init__(self):
        self.__meetings = {}

    def get_meetings(self):
        return self.__meetings
    def add_room(self, name, num_chairs):
        r = Room(name, num_chairs)
        if (r not in self.__meetings):
            self.__meetings[r] = set()
            return True
        return False

    def add_meeting(self, meeting, room):
        if (self._check_time_conflicts(meeting, room)):
            self.__meetings[room].add(meeting)
            return True
        else:
            return False

    def _check_time_conflicts(self, meeting, room):
        for mtg in self.__meetings[room]:
            if (meeting.get_start_time() < mtg.get_start_time()):
                if (meeting.get_end_time() > mtg.get_start_time()):
                    return False
            elif (meeting.get_start_time() > mtg.get_start_time()):
                if (mtg.get_end_time() > meeting.get_start_time()):
                    return False
            else:
                return false
        return True
