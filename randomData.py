import random
import csv

# Define the function to generate data with custom age-based break time logic
def generate_data(n):
    data = []
    for _ in range(n):
        period = random.choice(['Day', 'Night'])
        age = random.randint(10, 55)
        
        # Determine study time in minutes (1 to 120 minutes)
        study_time = random.randint(1, 120)
        
        # Determine break time in seconds per minute of study time
        if age <= 15:
            if period == 'Day':
                break_time = random.randint(10, 20)  # More breaks for younger ages during the day
            else:
                break_time = random.randint(20, 30)  # Even more breaks at night
        elif age <= 22:
            if period == 'Day':
                break_time = random.randint(5, 10)   # Fewer breaks for 16-22 during the day
            else:
                break_time = random.randint(10, 20)  # More breaks at night
        elif age <= 35:
            if period == 'Day':
                break_time = random.randint(2, 5)    # Very few breaks for 23-35 during the day
            else:
                break_time = random.randint(5, 10)   # Slightly more breaks at night
        else:  # Age 36-55
            if period == 'Day':
                break_time = random.randint(10, 20)  # More breaks for older ages during the day
            else:
                break_time = random.randint(20, 30)  # Even more breaks at night
        
        data.append([period, study_time, age, break_time])
    return data

# Generate 1000 rows of data
random_data = generate_data(5000)

# Write the data to a CSV file
with open('generated_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Period", "Total Hours", "Age", "BreakTime"])  # Write header
    writer.writerows(random_data)

print("Data generation complete. Check the 'generated_data.csv' file.")