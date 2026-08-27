# Last updated: 27/08/2026, 17:49:31
1class Solution(object):
2    def carPooling(self, trips, capacity):
3        """
4        :type trips: List[List[int]]
5        :type capacity: int
6        :rtype: bool
7        """
8        curr_passenger_count=0
9        passenger_ride = [0]*1001
10        new_passenger_ride = [0]*1001
11
12        for passengers, start_destination, end_destination in trips:
13            passenger_ride[start_destination]+=passengers
14            passenger_ride[end_destination]-=passengers
15
16        for i in range(len(passenger_ride)):
17            curr_passenger_count+=passenger_ride[i]
18            new_passenger_ride[i]=curr_passenger_count 
19
20        if capacity >= (max(new_passenger_ride)):
21            return True
22        else:
23            return False        
24        
25
26
27
28        