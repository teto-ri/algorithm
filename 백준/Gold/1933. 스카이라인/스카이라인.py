import sys
import heapq

input = sys.stdin.readline
building_num = int(input())
total_building = []
events = []

for i in range(building_num):
    start_x, height, end_x = map(int, input().split())
    total_building.append((start_x,height,end_x))
    events.append((start_x, -height, end_x))
    events.append((end_x, 0, 0))

events.sort()

skyline = []
prev_height = 0
current_buildings = [(0, float('inf'))]

for event in events:
    while current_buildings and current_buildings[0][1] <= event[0]: 
        heapq.heappop(current_buildings)
    if event[1]: 
        heapq.heappush(current_buildings, (event[1], event[2]))
    if prev_height != -current_buildings[0][0]: 
        prev_height = -current_buildings[0][0]
        skyline.append((event[0], prev_height))

for i in skyline:
    print(i[0],i[1],end=" ")