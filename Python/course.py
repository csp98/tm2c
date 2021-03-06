import db_connection


class Course:
    def __init__(self, course_name, start_time, end_time,
                 day, room_code):
        tmp = db_connection.DBConnection()
        self.course_name = course_name
        self.start_time = start_time
        self.end_time = end_time
        self.day = day.upper()
        self.room_code = room_code
        self.building_code = room_code[0]
        self.building_location = tmp.get_location(self.building_code)

    def to_s(self):
        return "*Course name*: {0}\n*Course day*: {1}\n*Course start time*: {2}\n*Course end time*: {3}\n*Course building*: {4}\n*Course room*: {5} \n".format(self.course_name,
                                                                                               self.day, self.start_time, self.end_time, self.building_code, self.room_code)


def take_me(code):
    tmp = db_connection.DBConnection()
    room_code = code[1:]
    for c in room_code:
        if c.isdigit():
            floor = c
            break
    building = code[0]
    location = tmp.get_location(building)
    return 'Go to building {} ({})'.format(building.upper(), location), 'Go to floor {}'.format(floor), 'Find room {}'.format(room_code)
    # return 'Go to building {0} ({1}).\n Go to floor {2}. Find room {3}.'.format(building.upper(), location, floor, room_code)

def get_day(day):
    if day==0:
        result='Monday'
    elif day==1:
        result='Tuesday'
    elif day==2:
        result='Wednesday'
    elif day==3:
        result='Thursday'
    elif day==4:
        result='Friday'
    elif day==5:
        result='Saturday'
    else:
        result='Sunday'
    return result
