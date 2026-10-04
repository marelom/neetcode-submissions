class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        step_list = []

        cars = sorted(zip(position, speed))
        for v in cars:
            steps = (target - v[0]) / v[1]
            if steps in step_list:
                continue
            else:    
                step_list.append(steps)
            one_list = []
            thing = len(step_list)
            for i in range(thing - 1):
                next_pos = step_list[i + 1]
                v = step_list[i]
                if v < next_pos:
                    while len(step_list) >= 2 and step_list[-2] <= step_list[-1]:
                        step_list.pop(-2)
                    
        return len(step_list)
            