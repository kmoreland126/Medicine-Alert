# App Used to remind user to take their medication at certain times when traveling through time zones.
# Created by Kate Moreland. Started on 9/30/24.

# Importing necessary libraries
from datetime import datetime
# downloading pytz library using pip install pytz
from zoneinfo import ZoneInfo

# Taking the input (Meds Name, Time, Time Zone) from the user
def get_medication_details():

    #Ask for medication name
    meds_name = input("Enter the medication name: ")

    #Ask for time they take the medication
    meds_time = input("Enter the time you take the medication (HH:MM in 24-hour format): ")

    #Ask for the time zone they are currently in
    time_zone = input("Enter the time zone you are currently in (e.g. America/Chicago): ")

    travel_time_zone = input("Enter the time zone you are traveling to (e.g. America/Chicago): ")

    try:

        #Parse the time input
        meds_time_obj = datetime.strptime(meds_time, "%H:%M")

        #Add the timezone to the time
        meds_with_zone = meds_time_obj.replace(tzinfo=ZoneInfo(time_zone))

        return meds_name, meds_with_zone, travel_time_zone
    except Exception as e:
        print("An error occurred: {e}. Check your input and try again.")
        return None

# Converting that time to the deserved time zone
def convert_time_zone(meds_with_zone, travel_time_zone):

    try:
        #Convert the time to the new time zone
        new_time = meds_with_zone.astimezone(ZoneInfo(travel_time_zone))
        return new_time
    except Exception as e:
        print("An error occurred: {e}. Check your input and try again.")

# Showing the output to the user
def show_output(meds_name, meds_with_zone, new_time):

    print(f"Medication Name: {meds_name}")
    print(f"Current Time: {meds_with_zone}")
    print(f"New Time: {new_time}")

# Main execution
if __name__ == "__main__":
    # Call the function to get input
    medications = []

    # Allows for multiple medications to be entered
    while True:
        details = get_medication_details()
        if details:
            medications.append(details)

        another = input("Do you want to add another medication? (yes/no): ").strip().lower()
        if another != 'yes':
            break

    for meds_name, meds_with_zone, travel_time_zone in medications:
        new_time = convert_time_zone(meds_with_zone, travel_time_zone)
        if new_time:
            show_output(meds_name, meds_with_zone, new_time)