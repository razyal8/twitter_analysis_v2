import logging

from flask import Flask, jsonify, request
from requests_oauthlib import OAuth1Session

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

health_status = True

@app.route('/health')
def health():
    logging.info("im health?")
    if health_status:
        resp = jsonify(health="healthy")
        resp.status_code = 200
    else:
        resp = jsonify(health="unhealthy")
        resp.status_code = 500

    return resp

@app.route('/tweet', methods=['POST'])
def tweet():
    logging.info("Make a tweet request!")
    payload = request.json.get('payload')
    consumer_key = "xxyr0MzwRhBt6aH98g7GVWssE"
    consumer_secret = "GDCvubUkKour4cMwW63z08dE9ctGfZcVCxTjPPRLcP9Mzm9SCL"
    access_token = "1756283592768978945-YPz0POxt2s8AX9DUJzZJXP98hwQfdX"
    access_token_secret = "WeltERe3hm08gBphPf9EzETCYoBjEsJEAbfIErzljkSWm"

    # Get request token
    request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except Exception as e:
        message = "There may have been an issue with the consumer_key or consumer_secret you entered."
        logging.error(message, e)
        return jsonify(message), 500

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    print("Please go here and authorize: %s" % authorization_url)

    # Get the access token
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
    )

    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    # Making the request
    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json={"text": f'{payload}'},
    )

    if response.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    logging.info("Tweet successful!")

    return jsonify({'status': 'Tweet successful!'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
