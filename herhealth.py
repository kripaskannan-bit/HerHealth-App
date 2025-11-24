Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import datetime

class HealthTracker:
    """
    A simple class to track menstrual cycle history and basic health metrics.
    """
    def _init_(self):
        # Initialize the history lists as empty when a new object is created
        self.cycle_history = []
        self.vitals_history = []
        print("HealthTracker initialized. Welcome!")

    # --- Period Logging Methods ---

    def log_period(self):
        needed_fmt = "%Y-%m-%d"
        user_input = input("Enter period start date (YYYY-MM-DD please, trust me): ")

        try:
            # Parses the string into a datetime object, then converts to a date object
            parsed_date = datetime.datetime.strptime(user_input, needed_fmt).date() 

            if parsed_date not in self.cycle_history:
                self.cycle_history.append(parsed_date)
                self.cycle_history.sort() # Keeps dates in chronological order
                print("Got it. Logged your start date:", parsed_date)
            else:
                print("Pretty sure that date’s already saved. Not adding it again.")

        except ValueError:
            print("❌ Nope. That doesn’t look like a valid YYYY-MM-DD date. Try again?")

    def view_cycle_history(self):
        if len(self.cycle_history) == 0:
            print("No cycle data yet. Try logging a date using option 1.")
            return

        print("\nPeriod Start Dates (in order):")
        for d in self.cycle_history:
            print("  →", d)
        print("-------------------------------")

    def calculate_average_cycle(self):
        if len(self.cycle_history) < 2:
            print("⚠ Not enough data yet to figure out an average cycle length.")
            return

        diffs = []
        # Loop starts from the second element (index 1)
        for index in range(1, len(self.cycle_history)):
            prev = self.cycle_history[index - 1]
            curr = self.cycle_history[index]
            
            # Calculate the number of days between the two dates
            days_between = (curr - prev).days 
            diffs.append(days_between)

        total_days = sum(diffs)
        avg = total_days / len(diffs)

        print(f"Your rough average cycle length (not exact science): {round(avg, 1)} days.")

    # --- Vitals Logging Methods ---

    def add_health_metric(self):
        bp_val = input("Blood Pressure (e.g. 120/80): ")
        tmpr = input("Temperature (F): ")
        hr_val = input("Heart Rate (bpm): ")
        hg = input("Hemoglobin (g/dL): ")

        # Gets today's date
        today_stamp = datetime.date.today() 
... 
...         bundle = {
...             "date": today_stamp,
...             "blood_pressure": bp_val,
...             "temperature": tmpr,
...             "heart_rate": hr_val,
...             "hemoglobin": hg
...         }
... 
...         self.vitals_history.append(bundle)
...         print("Saved your vitals! Hopefully everything looks good.")
... 
...     def view_vitals(self):
...         if not self.vitals_history:
...             print("No vitals yet — go record at least one entry first.")
...             return
... 
...         print("\n**** Vitals Log ****")
...         for idx, record in enumerate(self.vitals_history, 1):
...             print(f"-- Entry {idx}:")
...             print(f"    Date: {record['date']}") 
...             print(f"    BP: {record['blood_pressure']}")
...             print(f"    Temp: {record['temperature']}")
...             print(f"    HR: {record['heart_rate']} bpm")
...             print(f"    Hb: {record['hemoglobin']} g/dL")
...         print("--------------------------")
... 
... # --- Example Usage ---
... 
... if _name_ == "_main_":
...     # Create an instance (object) of the HealthTracker class
...     tracker = HealthTracker()
...     
...     print("\n--- Testing Log Period ---")
...     tracker.log_period() 
...     tracker.view_cycle_history() 
... 
...     print("\n--- Testing Add Vitals ---")
...     tracker.add_health_metric()
