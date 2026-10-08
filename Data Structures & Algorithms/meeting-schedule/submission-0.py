"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i:i.start)

        for i in range(1, len(intervals)):
            m = intervals[i - 1]
            now = intervals[i]

            if now.start < m.end:
                return False
        else:
            return True        
      
            
