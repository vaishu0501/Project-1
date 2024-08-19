import json
from datetime import datetime

#1)Initialization

#_init__ Method: This is the constructor method, called when an instance of FitnessTracker is created. 

# It initializes the object with a filename for data storage (tracker_data.json by default) and calls load_data() to load any previously saved data.
class FitnessTracker:
    def __init__(self, filename='tracker_data.json'):
        self.filename = filename
        self.load_data()
#2)Data Persistence

# load_data Method: Loads saved data from a JSON file. It initializes attributes like steps, calories_burned, exercise_sessions, etc., from the file.

# save_data Method: Saves the current state of the tracker to a JSON file. The json.dump function writes the dictionary data to the file in JSON format.    
    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.steps = data.get('steps', 0)
                self.calories_burned = data.get('calories_burned', 0)
                self.exercise_sessions = data.get('exercise_sessions', [])
                self.weight_records = data.get('weight_records', [])
                self.sleep_records = data.get('sleep_records', [])
                self.goals = data.get('goals', {})
        except FileNotFoundError:
            self.steps = 0
            self.calories_burned = 0
            self.exercise_sessions = []
            self.weight_records = []
            self.sleep_records = []
            self.goals = {}

    def save_data(self):
        data = {
            'steps': self.steps,
            'calories_burned': self.calories_burned,
            'exercise_sessions': self.exercise_sessions,
            'weight_records': self.weight_records,
            'sleep_records': self.sleep_records,
            'goals': self.goals
        }
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
#3) Tracking Methods

#add_steps Method: Adds a number of steps to the steps attribute, saves the updated data, and prints the updated step count.

#add_calories Method: Adds calories to the calories_burned attribute, saves the updated data, and prints the updated calories burned.

#add_exercise_session Method: Adds a new exercise session to exercise_sessions with details such as exercise name, duration, calories burned, and the current date and time. 

    def add_steps(self, steps):
        self.steps += steps
        self.save_data()
        print(f"Added {steps} steps. Total steps: {self.steps}")

    def add_calories(self, calories):
        self.calories_burned += calories
        self.save_data()
        print(f"Added {calories} calories. Total calories burned: {self.calories_burned}")

    def add_exercise_session(self, exercise_name, duration, calories_burned):
        session = {
            "exercise_name": exercise_name,
            "duration": duration,
            "calories_burned": calories_burned,
            "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.exercise_sessions.append(session)
        self.add_calories(calories_burned)
        print(f"Added exercise session: {exercise_name}, Duration: {duration} minutes, Calories burned: {calories_burned}")

#4)Weight and Sleep Tracking

# dd_weight_record Method: Adds a weight record to weight_records with the weight and the current date. Saves the data and prints a confirmation message.

#add_sleep_record Method: Adds a sleep record to sleep_records with the number of hours slept and the current date. Saves the data and prints a confirmation message.
    
    def add_weight_record(self, weight):
        record = {
            "weight": weight,
            "date": datetime.now().strftime('%Y-%m-%d')
        }
        self.weight_records.append(record)
        self.save_data()
        print(f"Added weight record: {weight}kg")

    def add_sleep_record(self, hours_slept):
        record = {
            "hours_slept": hours_slept,
            "date": datetime.now().strftime('%Y-%m-%d')
        }
        self.sleep_records.append(record)
        self.save_data()
        print(f"Added sleep record: {hours_slept} hours")
#5)Goal Management

#set_goal Method: Creates a new goal with a specified goal_name and target_value. Initializes the current_value to 0 and saves the updated goals.

#update_goal Method: Updates the current_value for an existing goal. If the updated current_value meets or exceeds the target_value, it prints a congratulatory message. Saves the updated goals.
    
    def set_goal(self, goal_name, target_value):
        self.goals[goal_name] = {
            "target_value": target_value,
            "current_value": 0
        }
        self.save_data()
        print(f"Set new goal: {goal_name} with target value {target_value}")

    def update_goal(self, goal_name, value):
        if goal_name in self.goals:
            self.goals[goal_name]["current_value"] += value
            if self.goals[goal_name]["current_value"] >= self.goals[goal_name]["target_value"]:
                print(f"Congratulations! You've achieved your goal: {goal_name}")
            self.save_data()
        else:
            print(f"Goal '{goal_name}' not found")
#6) Summary Report

#get_summary Method: Prints a comprehensive summary of all tracked data:

#Total steps and calories burned.

#Details of all exercise sessions, weight records, and sleep records.

#Status of all goals with their target values, current values, and whether they are achieved or not.
 
    def get_summary(self):
        print(f"Total steps: {self.steps}")
        print(f"Total calories burned: {self.calories_burned}")
        print("Exercise sessions:")
        for session in self.exercise_sessions:
            print(f" - {session['exercise_name']}: {session['duration']} minutes, {session['calories_burned']} calories on {session['date']}")
        print("Weight records:")
        for record in self.weight_records:
            print(f" - {record['weight']}kg on {record['date']}")
        print("Sleep records:")
        for record in self.sleep_records:
            print(f" - {record['hours_slept']} hours on {record['date']}")
        print("Goals:")
        for goal_name, goal in self.goals.items():
            status = "Achieved" if goal["current_value"] >= goal["target_value"] else "Not achieved"
            print(f" - {goal_name}: Target {goal['target_value']}, Current {goal['current_value']} ({status})")

# Example usage
if __name__ == "__main__":
    tracker = FitnessTracker()
    tracker.add_steps(5000)
    tracker.add_exercise_session("Jogging", 30, 300)
    tracker.add_weight_record(70)
    tracker.add_sleep_record(8)
    tracker.set_goal("Daily Steps", 10000)
    tracker.update_goal("Daily Steps", 5000)
    tracker.get_summary()
