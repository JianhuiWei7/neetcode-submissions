class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleet = 0
        time_req = 0
        for pos, spe in cars:
            time = (target - pos) / spe
            if time > time_req:
                fleet += 1
                time_req = time
        return fleet