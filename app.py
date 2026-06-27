from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Ticket Booking System"

@app.route('/health')
def health():
    return "Application is running fine"

@app.route('/book/<movie>')
def book(movie):
    return f"Ticket booked successfully for {movie}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)