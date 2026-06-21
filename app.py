from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
      <body style="font-family: sans-serif; text-align: center; padding: 60px;">
        <h1>🐳 Hello from Docker!</h1>
        <p>This Python app is running inside a Docker container.</p>
      </body>
    </html>
    """

@app.route('/greet/<name>')
def greet(name):
    return "<h2>Hello, {name}! Greetings from inside Docker 🐳</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)