### Author: Soulacex ###

import datetime

# Dictionary to store the schedule
schedule = {}

def add_task(name, start, end):
  # Convert start and end time to datetime objects
  start_time = datetime.datetime.strptime(start, "%Y-%m-%d %H:%M")
  end_time = datetime.datetime.strptime(end, "%Y-%m-%d %H:%M")

  # Add the task to the schedule
  schedule[name] = (start_time, end_time)

def view_schedule(day=None):
  if day is not None:
    # Convert day to a datetime object
    day = datetime.datetime.strptime(day, "%Y-%m-%d").date()

  for task, (start_time, end_time) in schedule.items():
    if day is None or start_time.date() == day:
      # Format the start and end time for display
      start = start_time.strftime("%m/%d/%Y %I:%M %p")
      end = end_time.strftime("%m/%d/%Y %I:%M %p")

      print(f"{task}: {start} - {end}")

def remove_task(name):
  # Remove the task from the schedule
  del schedule[name]

# Test the functions
add_task("Meeting with John", "2022-01-01 10:00", "2022-01-01 11:00")
add_task("Lunch with Mary", "2022-01-01 12:00", "2022-01-01 13:00")
add_task("Call with Jane", "2022-01-02 14:00", "2022-01-02 15:00")

print("Full schedule:")
view_schedule()

print("\nSchedule for 2022-01-01:")
view_schedule("2022-01-01")

remove_task("Meeting with John")

print("\nFull schedule after removing task:")
view_schedule()

