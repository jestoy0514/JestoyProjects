#!/usr/bin/env python3
#
# 100doors.py

# Create 100 doors with inital status of "close"
doors = {}
for num in range(1, 101):
    doors[num] = "close"

# Visit each door and change the status to open if close and close if open.
counter = 1
while counter <= 100:
    for num in range(counter, 101, counter):
        if doors[num] == "close":
            doors[num] = "open"
        else:
            doors[num] = "close"
    counter += 1

# Print status of the doors after visiting each door several times.
for num in doors:
    print("Door number %s is %s." % (str(num), doors[num]))
