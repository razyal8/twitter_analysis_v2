from flask import Flask, render_template, request, redirect, url_for
import requests
import logging
import json

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        destination = request.form['destination']
        print(f'{destination.capitalize()} Button Clicked')
        if destination in ['csv', 'api']:  # If destination is csv or api, redirect to respective route
            input_text = request.form['input_text']
            return redirect(url_for(destination, input_text=input_text))
        else:
            return redirect(url_for(destination))
    return render_template('index.html')

@app.route('/csv', methods=['GET'])
def csv():
    try:
        logging.info('some of the analysis')
        input_text = request.args.get('input_text', '') 
        logging.info(f'input for analysis {input_text}')

        url = "http://10.100.90.191:9000/health"
        response = requests.get(url)
        response.raise_for_status()
        plot_paths = response.json()
        return render_template('analysis.html', plot_paths=plot_paths)
    except requests.RequestException as e:
        logging.error("Request Error:", e)
        return render_template('error.html', message="Error occurred while fetching data from the server.")
    except Exception as e:
        logging.error("Error occurred:", e)
        return render_template('error.html', message=str(e))

@app.route('/api', methods=['GET'])
def api():
    input_text = request.args.get('input_text', '')  # Get input text from query parameters
    print('Started')
    logging.info(f'API Button Clicked with input text: {input_text}')
    payload = {"payload": input_text}
    headers = {"Content-Type": "application/json"}  # Specify JSON content type

    # Make a POST request to the Flask app service   
    try:
        logging.info(f'make request {payload}')
        url = "http://tweet-service:3000/tweet"
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        logging.info("Request to Flask app service successful!")
        logging.info(response)
        return render_template('result.html', message=response.json())
    except Exception as e:
        logging.error("Error occurred:", e)
        return render_template('result.html', message=e)


@app.route('/all-analysis')
def all_analysis():
    try:
        logging.info('all-analysis')
        url = "http://10.100.90.191:9000/analysis"
        response = requests.get(url)
        response.raise_for_status()
        plot_paths = response.json()
        return render_template('analysis.html', plot_paths=plot_paths)
    except requests.RequestException as e:
        logging.error("Request Error:", e)
        return render_template('error.html', message="Error occurred while fetching data from the server.")
    except Exception as e:
        logging.error("Error occurred:", e)
        return render_template('error.html', message=str(e))
 
if __name__ == '__main__':
    app.run(debug=True)
