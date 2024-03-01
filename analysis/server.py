import logging

from database import MongoDB
from flask import Flask, jsonify, request

from data_processing import insert_csv_to_mongodb
from tweet_analysis import getAllAnalysis, getAnalysisByInput

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Connect to MongoDB
db = MongoDB(db_name="Tweets_Dataset")

# Read CSV and insert data into MongoDB
csv_file = 'data/tweets.csv'
collection_name = "tweets"
insert_csv_to_mongodb(csv_file, db, collection_name)

health_status = True

@app.route('/health')
def health():
    logging.info("check health!")
    if health_status:
        resp = jsonify(health="healthy")
        resp.status_code = 200
    else:
        resp = jsonify(health="unhealthy")
        resp.status_code = 500
    return resp

@app.route('/analysis', methods=['GET'])
def analyze_data():
    logging.info("Get all analysis")
    try:
        plot_paths = getAllAnalysis(db)
        serialized_plots = {}
        for plot_name, plot_data in plot_paths.items():
            serialized_plots[plot_name] = plot_data
        return jsonify(serialized_plots)
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/analysis-by-input', methods=['GET'])
def analyze_data_by_input():
    logging.info("Get all by input")
    try:
        input_text = request.args.get('input_text', '')
        plot_paths = getAnalysisByInput(input_text, db) 
        serialized_plots = {}
        for plot_name, plot_data in plot_paths.items():
            serialized_plots[plot_name] = plot_data
        return jsonify(serialized_plots)
    except Exception as e:
        logging.error("Error occurred:", e)
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
