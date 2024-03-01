# twitter_analysis_v2
Final Project - Twitter Insight Engine using Kubernetes

# Folder Analysis

This repository contains scripts for analyzing Twitter data stored in MongoDB. The analysis includes various visualizations and insights derived from the tweet data.

## Folder Structure

- **data/**: Contains Excel files with tweet data.
- **analysis/**: Contains scripts for data processing, analysis, and visualization.
- **dockerfile**: Dockerfile for containerizing the application.
- **server.py**: Flask server script to expose APIs for data analysis.
- **database.py**: Script for interacting with MongoDB.
- **tweet_analysis.py**: Script for performing tweet analysis.
- **README.md**: This file, providing an overview of the repository.

## Setup and Dependencies

To run the scripts in this repository, you need to have the following dependencies installed:

- Python 3.x
- pandas
- pymongo
- Flask
- NLTK
- Matplotlib
- WordCloud

You can install the dependencies using pip:
pip install pandas pymongo Flask nltk matplotlib wordcloud


Additionally, you need to download the NLTK data. Run Python and execute the following commands:

```python
import nltk
nltk.download('vader_lexicon')
```

Usage

    Ensure that you have MongoDB running.
    Place your tweet data in the data/ directory.
    Run the Flask server using the following command:

python server.py

    Once the server is running, you can access the following endpoints:
        /health: Check the health status of the server.
        /analysis: Get all analysis of tweet data.
        /analysis-by-input?input_text=<author_name>: Get analysis for tweets by a specific author.

Data Processing and Analysis

    The data_processing.py script contains functions for processing tweet data and inserting it into MongoDB.
    The tweet_analysis.py script contains functions for performing various analyses on tweet data, including plotting tweets by day of the week, hour of the day, sentiment analysis, word clouds, etc.

Docker

A Dockerfile is provided for containerizing the application. You can build the Docker image using the following command:

docker build -t tweet-analysis .

You can then run the Docker container using:

docker run -p 9000:9000 tweet-analysis


# API Folder

This folder contains scripts for a Flask API that interacts with Twitter's API to post tweets.

## Folder Structure

- **dockerfile**: Dockerfile for containerizing the API.
- **tweet.py**: Flask server script to handle tweet requests.

## Usage

To run the Flask API, you can use Docker. Make sure you have Docker installed on your system.

1. Navigate to the `api/` directory.
2. Build the Docker image using the following command:

docker build -t tweet-api .


3. Once the image is built, you can run the Docker container using:


4. The Flask server will be accessible at `http://localhost:3000`.

## Dependencies

The API requires the following Python packages:

- requests
- requests_oauthlib
- Flask

These dependencies are installed automatically when building the Docker image.

## Endpoints

The API exposes the following endpoints:

- `/health`: Check the health status of the API.
- `/tweet`: Make a tweet request by providing the tweet content in the request payload.

## Authorization

The API uses OAuth1 authentication to interact with the Twitter API. You need to provide your Twitter API credentials in the `tweet.py` script:

- Consumer Key (`consumer_key`)
- Consumer Secret (`consumer_secret`)
- Access Token (`access_token`)
- Access Token Secret (`access_token_secret`)

Make sure to keep your credentials secure and avoid exposing them publicly.


# App Folder

This folder contains a Flask application for interacting with other services and rendering HTML templates.

## Folder Structure

- **static/**: Contains CSS files for styling the HTML templates.
- **templates/**: Contains HTML templates for rendering the web pages.
- **app.py**: Flask server script to handle requests and render templates.
- **Dockerfile**: Dockerfile for containerizing the Flask application.

## Usage

To run the Flask application, follow these steps:

1. Ensure that you have all the necessary dependencies installed.
2. Navigate to the `app/` directory.
3. Build the Docker image using the following command:

docker build -t flask-app .


4. Once the image is built, you can run the Docker container using:


5. The Flask application will be accessible at `http://localhost:5000`.

## Dependencies

The Flask application requires the following Python packages:

- Flask
- requests

These dependencies are installed automatically when building the Docker image.

## Endpoints

The Flask application exposes the following endpoints:

- `/`: Renders the index page with a form to input destination and text.
- `/csv`: Renders the analysis page for CSV data.
- `/api`: Makes a tweet request using input text and renders the result page.
- `/all-analysis`: Renders the analysis page for all data.

## Templates

The application uses the following HTML templates:

- **index.html**: Form for inputting destination and text.
- **analysis.html**: Page for displaying analysis plots.
- **result.html**: Page for displaying tweet result.
- **error.html**: Page for displaying error messages.

## Static Files

The `static/` directory contains CSS files for styling the HTML templates.

## Python Script

The `app.py` script contains the Flask application logic for handling requests and rendering templates.

## License

This project is licensed under the [MIT License](LICENSE).

