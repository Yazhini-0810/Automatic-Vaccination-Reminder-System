"""
Automatic Vaccination Reminder System

Author: Yazhini B

Description:
A Python-based application that automates vaccination reminders
by sending email notifications using SMTP. The system stores
vaccination details, schedules reminders, and provides
educational information about vaccines.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import time


# Function to collect vaccination details
def get_vaccination_details():
    details = {}

    print("Enter the vaccination details.")

    details['child_name'] = input("Enter the child's name: ")
    details['age'] = input("Enter the child's age: ")
    details['gender'] = input("Enter the child's gender: ")
    details['vaccination_date'] = input("Enter the vaccination date (YYYY-MM-DD): ")
    details['vaccine_name'] = input("Enter the vaccine name: ")
    details['vaccination_centre'] = input("Enter the vaccination centre: ")
    details['parents_phone'] = input("Enter the parents' phone number: ")
    details['email'] = input("Enter the parents' email address: ")
    details['acknowledgement'] = input("Do the parents acknowledge this vaccination? (yes/no): ")
    details['notification_mode'] = input("Enter notification mode (email/sms): ").lower()

    return details


# Function to send email notification
def send_email(subject, body, to_email):

    # Replace with your own email credentials before running
    from_email = "your_email@gmail.com"
    from_password = "YOUR_APP_PASSWORD"

    msg = MIMEMultipart()

    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        server.login(from_email, from_password)

        server.sendmail(from_email, to_email, msg.as_string())

        server.quit()

        print(f"Email sent successfully to {to_email}")

    except Exception as e:
        print(f"Failed to send email: {e}")


# Function to provide educational information about vaccines
def get_educational_info(vaccine):

    educational_info = {

        "HepB":
            "Hepatitis B is a serious liver infection caused by the Hepatitis B virus. "
            "The HepB vaccine protects against this disease.",

        "DTaP":
            "DTaP vaccine protects against Diphtheria, Tetanus, and Pertussis "
            "(Whooping Cough)."

    }

    return educational_info.get(vaccine, "Educational information not available.")


# Function to send vaccination reminder
def send_vaccination_reminder(details):

    subject = f"Reminder: {details['vaccine_name']} Vaccination"

    educational_info = get_educational_info(details['vaccine_name'])

    body = f"""
Dear Parent,

This is a reminder for your child's upcoming vaccination.

Child Name          : {details['child_name']}
Age                 : {details['age']}
Gender              : {details['gender']}
Vaccination Date    : {details['vaccination_date']}
Vaccine             : {details['vaccine_name']}
Vaccination Centre  : {details['vaccination_centre']}
Parent Phone        : {details['parents_phone']}
Acknowledgement     : {details['acknowledgement']}

Educational Information:
{educational_info}

Thank you.

Stay Safe!
"""

    if details['notification_mode'] == "email":
        send_email(subject, body, details['email'])

    elif details['notification_mode'] == "sms":
        print("SMS functionality is not implemented.")
        print("Future enhancement: Integrate Twilio API for SMS reminders.")

    else:
        print("Invalid notification mode selected.")

    print(body)


# Main Function
def main():

    vaccination_details = get_vaccination_details()

    if vaccination_details:

        print("Vaccination details recorded successfully.")
        print("Waiting until 01:45 AM to send reminder...")

        while True:

            current_time = datetime.datetime.now().strftime("%H:%M")

            if current_time == "01:45":

                send_vaccination_reminder(vaccination_details)

                break

            time.sleep(60)

    else:

        print("No vaccination details entered.")


if __name__ == "__main__":
    main()