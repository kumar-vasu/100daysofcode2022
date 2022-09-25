class Solution:
    def dayOfYear(self, date: str) -> int:
        date = date.split("-")
        days = int(date[2])
        year = int(date[0])
        months = {1:0,
                 2:31,
                 4:31,
                 5:30,
                 6:31,
                 7:30,
                 8:31,
                 9:31,
                 10:30,
                 11:31,
                 12:30}
        
        for month in range(1, int(date[1])+1):
            if month == 3:
                if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                    days += 29
                else:
                    days += 28
            else:
                days += months[month]
            #print(days)
            
        return days