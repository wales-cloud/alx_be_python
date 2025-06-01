#!/usr/bin/env python3
"""
Personal Daily Reminder
"""

# Prompt for input
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Match case for priority
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

# Add time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Output the final reminder
print(f"\nReminder: {message}")
