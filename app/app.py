from flask import Flask, render_template, request, redirect, url_for

# from api.tweet import tweet

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
    input_text = request.args.get('input_text', '')  # Get input text from query parameters
    print(f'CSV Button Clicked with input text: {input_text}')
    message = f'CSV Button Clicked with input text: {input_text}'
    return render_template('result.html', message=message)

@app.route('/api', methods=['GET'])
def api():
    input_text = request.args.get('input_text', '')  # Get input text from query parameters
    print(f'API Button Clicked with input text: {input_text}')
    message = f'API Button Clicked with input text: {input_text}'
    # newTweet = tweet(input_text)
    return render_template('result.html', message=message)


@app.route('/all-analysis')
def all_analysis():
    message = 'All Analysis Button Clicked'
    return render_template('result.html', message=message)

@app.route('/process_input', methods=['POST'])
def process_input():
    input_text = request.form['input_text']
    return redirect(url_for('index', input_text=input_text))

if __name__ == '__main__':
    app.run(debug=True)
