from flask import Flask, jsonify

# Initialize application
app = Flask(__name__)

# Dictionary of video games, release dates, and publishers
data = [
    {"game name":"Splatoon 3", "release date":2023, "publisher":"Nintendo"},
    {"game name":"Pokemon: Legends Z-A", "release date":2025, "publisher":"Nintendo"},
    {"game name":"Sonic Racing CrossWorlds", "release date":2025, "publisher":"SEGA"}
]

@app.route("/")
def index():
    return '''
    <h1> Navigate to one of these pages </h1>
    <ul>
        <li><a href = "/home">/home</a></li>
        <li><a href = "/data">/data</a></li>
    </ul>
    '''

# Takes you to the welcome page
@app.route("/home")
def home():
    return jsonify({"greeting": "Hello, and welcome to the greetings page!"}), 200

# Takes you to the data page
@app.route("/data")
def get_data():
    return jsonify(data), 200

# Run main program
if __name__ == "__main__":
    app.run()