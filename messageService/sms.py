from twilio.rest import Client
import os

from dotenv import load_dotenv
load_dotenv()

# Access the environment variables
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_number = os.environ['TWILIO_NUMBER']
messaging_service_sid = os.environ['MESSAGING_SERVICE_ID']


class SMS:
    client = Client(account_sid, auth_token)

    def send_message(body, target_number, scheduleTime):

        message = SMS.client.messages.create(
            body=body,
            from_=twilio_number,
            to=target_number,
            messaging_service_sid=messaging_service_sid,
            send_at=scheduleTime,
            schedule_type='fixed'
        )
        print(message)