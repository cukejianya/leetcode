class MyCalendar(object):

    def __init__(self):
        self.calendar = []            

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.all_events:
            self.booked_time = [(start, end)]
            return True
        for booked_time in self.calendar:
            if booked_time[0] < start and start < booked_time[1]:
                return False
            if booked_time[0] < end and end < booked_time[1]:
                return False

        for booked_time in self.calendar:
            if booked_time[0] == end:
                booked_time[0] = start
                return True
            if booked_time[1] == start:
                booked_time[1] = end
                return True

        self.calendar.append((start, end))

        return True

        

                
            
