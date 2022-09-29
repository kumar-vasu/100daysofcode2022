class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        self.results = []
 
        
        def NChooseK(numbers, n, k,maximum=float('inf')):
            results = []
            def nchoosek(start=0, cumulative=0, summation=0):
                if summation >= maximum:
                    return 
                if cumulative + (n-start) < k:
                    return 
                if cumulative == k:
                    results.append(summation)
                    return 
                nchoosek(start+1, cumulative, summation)
                nchoosek(start+1, cumulative+1, summation+numbers[start])
                return 
            nchoosek()
            return results
            
            
        for numHour in range(min(turnedOn, 4)+1):
            numMin = turnedOn - numHour
            hours = NChooseK([8,4,2,1], 4, numHour,12)
            minutes = NChooseK([32,16,8,4,2,1], 6, numMin,60)
            for hour in hours:
                for minute in minutes:
                    strHour = str(hour)
                    if minute < 10:
                        strMin = "0" + str(minute)
                    else:
                        strMin = str(minute)
                    self.results.append( strHour + ":" + strMin )
        return self.results