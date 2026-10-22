class TimeMap:

    def __init__(self):
        self.my_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.my_dict:
            self.my_dict[key] = {}

        self.my_dict[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        true_timestamp = None

        if key not in self.my_dict:
            return ""

        left = 0
        thing = list(self.my_dict[key].keys())
        right = len(thing) - 1 
        while left < right: 
            mid = (left + right) // 2
            if thing[mid] > timestamp:
                right = mid - 1
            else:
                left = mid + 1  
                if thing[left] > timestamp:
                    left = mid
                    break 
                        
        true_timestamp = thing[left]       

        if true_timestamp <= timestamp:
            return self.my_dict[key][true_timestamp] 
        else:
            return ""           
   