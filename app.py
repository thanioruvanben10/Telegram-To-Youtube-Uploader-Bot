from flask import Flask
app = Flask(name)

@app.route('/')
def hello_world():
    return 'Thani Oruvan'

if name == "main":
    app.run()
