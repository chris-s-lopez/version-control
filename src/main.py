from datetime import datetime

# Get current date and time
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

# Write to version.md
with open("data/version.md", "w") as file:
    file.write(f"Current Date and Time: {formatted_date}")
