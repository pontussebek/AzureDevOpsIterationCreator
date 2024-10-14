# To Run

## step 1
Create a year root iteration called for example 2025, set the root_iteration var in loaditerationsIntoAzureDevOps.py

## step 2
Create a environmentvar.py file with these vars 

# Azure devops parameters
organization = "YOUR_ORGANIZATION_NAME"
project = "YOUR_PROJECT_NAME"

# Personal Access Token (PAT)
pat = "YOUR_PERSONAL_ACCESS_TOKEN"


## step 3
Generate csv file with examples

## step 4
load iterations py

# Testing with rest client extension for vscode 
create a .vscode folder with a settings.json file in it.

{
    "rest-client.environmentVariables": {
        "defaultEnvironment": {
            "organization": "YOUR_ORGANIZATION_NAME",
            "token": "YOUR_PERSONAL_ACCESS_TOKEN as base64",
            "project": "YOUR_PROJECT_NAME"
        }
    }
}