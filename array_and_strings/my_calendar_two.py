class MyCalendarTwo(object):
    def __init__(self):
        self.double_book_set = set([])
        self.all_book_set= set([])

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        
        if not start or not end or not self.can_book(start, end):
            return False

        self.add_event(start, end)
        return True

    def add_event(self, start, end):
        for booked_event in self.all_book_set:
            if self.check_if_overlapped(start, end, booked_event):
                double_booked_interval = self.get_double_booking_interval(start,
                        end, booked_event)
                self.double_book_set.add(double_booked_interval)
        self.all_book_set.add((start, end))

    def can_book(self, start, end):
        for double_booked_interval in self.double_book_set:
            if self.check_if_overlapped(start, end, double_booked_interval):
                return False
        return True
    
    def check_if_overlapped(self, start, end, interval):
        start_time, end_time = 0, 1
        if end <= interval[start_time] or interval[end_time] <= start:
            return False
        return True
    
    def get_double_booking_interval(self, start, end, interval):
        start_time, end_time = 0, 1
        return (max(start, interval[start_time]), min(end, interval[end_time]))