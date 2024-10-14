import csv
from datetime import datetime, timedelta

def generate_sprint_iterations(start_date, num_iterations):
    iterations = []
    current_date = start_date
    current_month = start_date.month
    iteration_number = 1

    for _ in range(num_iterations):
        end_date = current_date + timedelta(days=13)  # Two weeks minus one day
        
        # Reset iteration number if we've moved to a new month
        if current_date.month != current_month:
            current_month = current_date.month
            iteration_number = 1
        
        name = f"2025-{current_date.strftime('%m')}-{iteration_number:02d}"
        
        iterations.append({
            'Name': name,
            'Start Date': current_date.strftime("%Y-%m-%d"),
            'End Date': end_date.strftime("%Y-%m-%d")
        })
        
        current_date = end_date + timedelta(days=1)  # Start next sprint on the following day
        iteration_number += 1

    return iterations

def save_to_csv(iterations, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Start Date', 'End Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for iteration in iterations:
            writer.writerow(iteration)

# Set the start date and number of iterations
start_date = datetime(2025, 1, 7)
num_iterations = 25  # This will cover approximately one year

# Generate sprint iterations
sprint_iterations = generate_sprint_iterations(start_date, num_iterations)

# Save to CSV file
save_to_csv(sprint_iterations, 'iterations.csv')

print(f"Sprint iterations have been saved to 'sprint_iterations.csv'")

# Print the first few iterations for verification
print("\nFirst few iterations:")
for iteration in sprint_iterations[:5]:
    print(iteration)