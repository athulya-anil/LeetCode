# Last updated: 31/10/2026, 19:07:04
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        curr_passenger_count=0
        passenger_ride = [0]*1001
        new_passenger_ride = [0]*1001

        for passengers, start_destination, end_destination in trips:
            passenger_ride[start_destination]+=passengers
            passenger_ride[end_destination]-=passengers

        for i in range(len(passenger_ride)):
            curr_passenger_count+=passenger_ride[i]
            new_passenger_ride[i]=curr_passenger_count 

        if capacity >= (max(new_passenger_ride)):
            return True
        else:
            return False        
        



        