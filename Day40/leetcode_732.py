class MyCalendarThree(object):
    def __init__(self):
        self.tm = {}
    def book(self, start, end):
        self.tm[start] = self.tm.get(start, 0) + 1
        self.tm[end] = self.tm.get(end, 0) - 1
        count = mx = 0
        for val in sorted(self.tm):
            count += self.tm[val]
            mx = max(mx, count)
        return mx