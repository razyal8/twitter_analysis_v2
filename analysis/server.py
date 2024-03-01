import logging
from flask import Flask, jsonify
import matplotlib.pyplot as plt
import io
import base64

from tweet_analysis import getAllAnalysis
from data_processing import insert_csv_to_mongodb
from database import MongoDB

logging.basicConfig(level=logging.INFO)  # Set logging level to INFO

app = Flask(__name__)

# Connect to MongoDB
db = MongoDB(db_name="test_tweets")

# Read CSV and insert data into MongoDB
csv_file = 'data/tweets.csv'
collection_name = "tweetstest"
insert_csv_to_mongodb(csv_file, db, collection_name)

health_status = True

@app.route('/health')
def health():
    if health_status:
        resp = jsonify(health="healthy")
        resp.status_code = 200
    else:
        resp = jsonify(health="unhealthy")
        resp.status_code = 500

    return resp

@app.route('/analysis', methods=['GET'])
def analyze_data():
    try:
        plot_paths = getAllAnalysis(db)
        serialized_plots = {}
        for plot_name, plot_data in plot_paths.items():
            # Plot data is already in Base64 format
            serialized_plots[plot_name] = plot_data
        return jsonify(serialized_plots)
    except Exception as e:
        logging.error("Error occurred:", e)
        return jsonify(error=str(e)), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
