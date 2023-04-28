
import random

# Define the individual's characteristics
age = 27
weight = 190

# Define the exercise categories and their corresponding reps and sets
exercises = {
    "Chest": {"reps": range(10, 15), "sets": range(3, 5)},
    "Back": {"reps": range(10, 15), "sets": range(3, 5)},
    "Legs": {"reps": range(12, 18), "sets": range(3, 5)},
    "Shoulders": {"reps": range(10, 15), "sets": range(3, 5)},
    "Biceps": {"reps": range(8, 12), "sets": range(3, 5)},
    "Triceps": {"reps": range(8, 12), "sets": range(3, 5)},
    "Abs": {"reps": range(15, 25), "sets": range(3, 5)},
}

# Generate a workout plan
workout_plan = {}
for category, details in exercises.items():
    reps = random.choice(details["reps"])
    sets = random.choice(details["sets"])
    workout_plan[category] = {"reps": reps, "sets": sets}

# Print the workout plan
print(f"Workout plan for a {age}-year-old, {weight}-pound man:\n")
for category, details in workout_plan.items():
    print(f"{category}: {details['reps']} reps x {details['sets']} sets")
