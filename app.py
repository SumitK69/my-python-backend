from flask import Flask, jsonify
import yfinance as yf
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/', methods=['GET'])
def home():
    return jsonify(message = "home page")


@app.route('/hist', methods=['GET'])
def hello():
    msft = yf.Ticker("TCS.NS")
    hist = msft.history(period="1d", interval="1m")
    hist.index = hist.index.tz_localize(None)
    hist_dict = hist.reset_index().to_dict(orient='records')
    print(hist)
    return jsonify(hist_dict)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
