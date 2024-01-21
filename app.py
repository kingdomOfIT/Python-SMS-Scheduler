from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime
from messageService.sms import SMS

app = Flask(__name__)
app.secret_key = 'tajnaa'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sms', methods=['GET', 'POST'])
def sms():
    if request.method == 'POST':
        # Access form data
        message_body = request.form['messageBody']
        phone_number = request.form['phoneNumber']
        date_time = request.form['dateTime']

        input_datetime = datetime.strptime(date_time, "%Y-%m-%dT%H:%M")

        # Extract individual components
        year = input_datetime.year
        month = input_datetime.month
        day = input_datetime.day
        hour = input_datetime.hour
        minute = input_datetime.minute
        second = input_datetime.second

        # Create the desired format for Twilio
        twilio_format = datetime(year, month, day, hour, minute, second)

        # Send message using twilio rest
        SMS.send_message(body= message_body, target_number=phone_number, scheduleTime=twilio_format)

        # Flash a success message
        flash('Message scheduled successfully!', 'success')

        # Redirect to the same page to avoid form resubmission on page refresh
        return redirect(url_for('sms'))

    return render_template('sms.html')

@app.route('/gmail')
def gmail():
    return render_template('gmail.html')

@app.route('/whatsapp')
def whatsapp():
    return render_template('whatsapp.html')

if __name__ == '__main__':
    app.run(debug=True)
