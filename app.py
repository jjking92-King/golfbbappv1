# app.py
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page (the root URL '/')
@app.route('/')
def index():
    # Flask looks for templates inside the 'templates' directory
    # and renders your HTML file.
    return render_template('golfbattlebuddyv1.html')

# This block is used for local testing. 
# Cloud Run automatically sets the correct port (8080) for deployment.
if __name__ == '__main__':
    # Run the application on all interfaces (0.0.0.0) and a default port (8080)
    # which is standard for containerized apps like Cloud Run.
    app.run(debug=True, host='0.0.0.0', port=8080)

