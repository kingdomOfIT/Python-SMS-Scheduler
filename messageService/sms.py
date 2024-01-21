from twilio.rest import Client
import keys as keys

class SMS:
    client = Client(keys.account_id, keys.auth_token)

    def send_message(body, target_number):

        message = SMS.client.messages.create(
            body=body,
            from_=keys.twilio_number,
            to=target_number
        )

        print(message.body)