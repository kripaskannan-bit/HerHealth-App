# HerHealth-App
Herhealth:A Holistic Health Tracker – A simple, privacy-first Python terminal app to log period start dates, calculate average cycle length, and track daily vitals (BP, temp, HR, hemoglobin). No cloud, no accounts, no data leaves your device. Pure Python + datetime. Perfect for learning or personal use. Your body, your rules.

1. PROJECT OVERVIEW

The HealthTracker class handles two major tasks:

A. Menstrual Cycle Tracking

Logs period start dates in YYYY-MM-DD format

Stores all dates in a chronological list

Calculates the average cycle length

Displays recorded cycle history

B. Health Metrics Tracking

Records:

1. Blood Pressure

2. Temperature

3. Heart Rate

4. Hemoglobin

Adds today’s date to each entry

Stores all entries in a vitals dictionary

Displays complete health history

2. FEATURES

1. Log Period Start Date

Accepts input in YYYY-MM-DD

Checks for correct format

Stores unique dates

Displays confirmation

Sorts dates automatically


2. Calculate Average Cycle Length

Requires minimum two recorded dates

Calculates day differences between consecutive cycles

Outputs average cycle length in days


3. Add Daily Health Metrics

Requests BP, temperature, heart rate, hemoglobin

Automatically attaches today’s date

Stores each entry as a dictionary inside vitals_history


4. View Vitals History

Shows every logged entry

Displays date, BP, temperature, heart rate, hemoglobin

3. CODE STRUCTURE

Class HealthTracker

cycle_history: list of period start dates

vitals_history: list of vitals dictionary entries


Methods:

log_period(): Logs a period date

view_cycle_history(): Displays period dates

calculate_average_cycle(): Computes average cycle length

add_health_metric(): Adds vitals entry

view_vitals(): Displays vitals history


4. HOW THE PROGRAM WORKS

Initialization: The constructor init creates two empty lists: cycle_history and vitals_history.

Logging a Period: The program uses datetime.strptime() to convert the input string into a date object. Invalid formats produce an error message. If valid and not duplicate, the date is added and the list is sorted.

Calculating Average Cycle: The program finds the gap in days between every two consecutive dates and computes the average.

Adding Health Metrics: When the user enters vitals, a dictionary is created with keys: date, blood_pressure, temperature, heart_rate, hemoglobin. This dictionary is added to vitals_history.

Viewing Vitals: The program prints all vitals entries in a clean, readable format.


5. HOW TO RUN THE CODE

Important Corrections: Change init to init
Change name to name

Then run the file using:

python filename.py

The example section in the script will then allow you to:

Log a period

View cycle history

Add health metrics

View vitals history

6. SAMPLE INPUT AND OUTPUT

Example 1: Logging a Period
Input: 2025-11-20
Output: Got it. Logged your start date: 2025-11-20

Example 2: Adding Vitals
Input: BP: 120/80
Temperature: 98.4
HR: 73
Hemoglobin: 13.2
Output: Saved your vitals!

7. COMMON ISSUES

Issue 1: Program not running
Cause: name used instead of name

Issue 2: Constructor not working
Cause: init used instead of init

Issue 3: Wrong date input
Input must always be in YYYY-MM-DD format.

8. POSSIBLE FUTURE IMPROVEMENTS

Add next period prediction

Store data in a JSON file

Add graphs for vitals

Create a GUI using Tkinter

Export reports as PDF

Turn into a mobile app using Kivy

9. LICENSE

This project is free to use for learning, studying, and personal development.
