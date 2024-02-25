from flask import Flask, jsonify

from analysis.analysis import getAllAnalysis

app = Flask(__name__)

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
def hello():
    analysis = getAllAnalysis()
    return analysis

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
