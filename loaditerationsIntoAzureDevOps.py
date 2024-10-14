import csv
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import environmentvars

# Azure DevOps organization, project, and root iteration
root_iteration = "2025"

# Azure DevOps API URL
url = f'https://dev.azure.com/{environmentvars.organization}/{environmentvars.project}/_apis/wit/classificationnodes/iterations/{root_iteration}?api-version=5.0'

# Function to create an iteration
def create_iteration(name, start_date, end_date):
    iteration_data = {
        "name": name,
        "attributes": {
            "startDate": start_date,
            "finishDate": end_date
        }
    }

    # POST request to create iteration
    response = requests.post(
        url,
        json=iteration_data,
        auth=HTTPBasicAuth('', environmentvars.pat)
    )

    if response.status_code == 200 or response.status_code == 201:
        print(f"Iteration '{name}' created successfully.")
    else:
        print(f"Failed to create iteration '{name}': {response.status_code}, {response.text}")

# Read the CSV file and create iterations
csv_file = 'iterations.csv'

with open(csv_file, newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['Name']
        start_date = datetime.strptime(row['Start Date'], '%Y-%m-%d').isoformat()
        end_date = datetime.strptime(row['End Date'], '%Y-%m-%d').isoformat()
        create_iteration(name, start_date, end_date)