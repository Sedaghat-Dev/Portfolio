from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465  
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'Sedaghat.Dev.989@gmail.com'
app.config['MAIL_PASSWORD'] = 'ireislzuagbkrukd'  
# app.config['MAIL_DEFAULT_SENDER'] = 'Sedaghat.Dev.989@gmail.com'  

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Compose the email
    msg = Message(
        subject=f"New Contact Form Submission from {name}",
        recipients=['Sedaghat.Dev.989@gmail.com'],
        sender=email,
        body=f"Message from {name} ({email}):\n\n{message}",
    )

    try:
        # Try sending the email
        mail.send(msg)
        print("Email sent successfully.")  # Log email sent status

        # Return success message
        response = {'message': f"Thank you, {name}! Your message has been sent."}
    except Exception as e:
        # Log the error in case something goes wrong
        print(f"Error: {str(e)}")
        response = {'message': f"Something went wrong: {str(e)}"}

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
