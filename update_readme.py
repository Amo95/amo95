import datetime

# Define your start date
start_date = datetime.date(2020, 9, 15)  # Replace with your actual start date

current_date = datetime.date.today()

if current_date.month < start_date.month or (current_date.month == start_date.month and current_date.day < start_date.day):
    years_of_experience = current_date.year - start_date.year - 1
else:
    years_of_experience = current_date.year - start_date.year

# Read the README file
with open("README.md", "r") as f:
    readme_content = f.read()

# Replace the placeholder
readme_content = readme_content.replace("{{YEARS_OF_EXPERIENCE}}", str(years_of_experience))

# Write back to the README file
with open("README.md", "w") as f:
    f.write(readme_content)
