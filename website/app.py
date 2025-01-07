from flask import Flask, render_template
from mcrcon import MCRcon
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

RCON_HOST = os.getenv("RCON_HOST")
RCON_PASSWORD = os.getenv("RCON_PASSWORD")

def get_server_status():
    try:
        with MCRcon(RCON_HOST, RCON_PASSWORD) as mcr:
            response = mcr.command("list")
            return "Online" if response else "Offline"
    except:
        return "Offline"

@app.route('/')
def index():
    status = get_server_status()
    return render_template('index.html', status=status)

@app.route('/map')
def map():
    return render_template('page/map.html')

@app.route('/docs')
def docs():
    return render_template('page/docs.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')