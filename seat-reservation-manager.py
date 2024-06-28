class SeatManager:

    def __init__(self, n: int):
        self.seats = 1
        self.free = []

    def reserve(self) -> int:
        if len(self.free) > 0 and self.free[0] < self.seats:
            return self.free.pop(0)
        else:
            self.seats +=1 
            return self.seats - 1

    def unreserve(self, seatNumber: int) -> None:
        self.free.append(seatNumber)
        self.free.sort()


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)