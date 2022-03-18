from flask import Flask
import datetime
import json

app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.utcnow()
    value = {"today" : now.strftime('%Y-%m-%d')}
    return json.dumps(value)
    
if __name__ == '__main__':
    app.run()
