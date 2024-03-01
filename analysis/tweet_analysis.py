import nltk
import base64
import numpy as np
import pandas as pd

from io import BytesIO
from nltk import sentiment
from wordcloud import WordCloud
from matplotlib import pyplot as plt

nltk.download('vader_lexicon')
analyzer = sentiment.SentimentIntensityAnalyzer()

def plot_tweets_by_day_of_week(df):
    df["day_of_week"] = df["date_time"].dt.dayofweek
    df["day_of_week"].value_counts(normalize=True).sort_index().plot(kind="bar")
    plt.title("Tweets by Day of Week")
    plt.xlabel("Day of Week")
    plt.ylabel("Number of Tweets")
    plt.xticks(range(7), ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], rotation=45)
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return "tweets_by_day_of_week", plot_data


def plot_tweets_by_hour_of_day(df):
    df["hour_of_day"] = df["date_time"].dt.hour
    df["hour_of_day"].value_counts(normalize=True).sort_index().plot(kind="bar")
    plt.title("Tweets by Hour of Day (UTC)")
    plt.xlabel("Hour of Day")
    plt.ylabel("Number of Tweets")
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return "plot_tweets_by_hour_of_day", plot_data


def plot_likes_by_condition_if_content_has_substrings(df, substring1: str, substring2: str):
    result = np.zeros((2, 2))
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            condition1 = df["content"].str.contains(substring1) == i
            condition2 = df["content"].str.contains(substring2) == j
            result[i, j] = df[condition1 & condition2]["number_of_likes"].mean()
    plt.imshow(result)
    plt.colorbar()
    plt.title("Average Likes by Condition")
    plt.xticks([0, 1], [f"Doesn't Contain '{substring2}'", f"Contains '{substring2}'"])
    plt.yticks([0, 1], [f"Doesn't Contain '{substring1}'", f"Contains '{substring1}'"])
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return "plot_likes_by_condition_if_content_has_substrings", plot_data


def plot_likes_by_average_sentiment_per_user(df):
    print("\nCalculating Sentiment...")
    df['sentiment'] = df['content'].apply(lambda text: 1 if analyzer.polarity_scores(text)['pos'] > 0 else 0)
    data = np.zeros((0, 2))
    max_sentiment = ('', 0.0, 0.0)
    min_sentiment = ('', 1.0, 0.0)
    for user in df["author"].unique():
        condition = df["author"] == user
        data = np.vstack([data, [df[condition]["sentiment"].mean(), df[condition]["number_of_likes"].mean()]])
        if data[-1, 0] > max_sentiment[1]:
            max_sentiment = (user, data[-1, 0], data[-1, 1])
        if data[-1, 0] < min_sentiment[1]:
            min_sentiment = (user, data[-1, 0], data[-1, 1])
    print(f"User: {max_sentiment[0]:<15}, Sentiment: {max_sentiment[1]:.3f}, Likes: {max_sentiment[2]:,.0f}")
    print(f"User: {min_sentiment[0]:<15}, Sentiment: {min_sentiment[1]:.3f}, Likes: {min_sentiment[2]:,.0f}")
    plt.scatter(data[:, 0], data[:, 1])
    plt.xlabel("Average Sentiment")
    plt.ylabel("Average Number of Likes")
    plt.title("Average Likes by Average Sentiment")
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return "plot_likes_by_average_sentiment_per_user", plot_data


def plot_likes_by_average_tweet_rate_per_user(df):
    print("\nCalculating Tweet Rate...")
    data = np.zeros((0, 2))
    max_tweet_rate = ('', 0.0, 0.0)
    min_tweet_rate = ('', 1.0, 0.0)
    for user in df["author"].unique():
        condition = df["author"] == user
        tweets_rate = df[condition].shape[0] / (
                df[condition]["date_time"].max() - df[condition]["date_time"].min()).days
        data = np.vstack([data, [tweets_rate, df[condition]["number_of_likes"].mean()]])
        if data[-1, 0] > max_tweet_rate[1]:
            max_tweet_rate = (user, data[-1, 0], data[-1, 1])
        if data[-1, 0] < min_tweet_rate[1]:
            min_tweet_rate = (user, data[-1, 0], data[-1, 1])
    print(f"User: {max_tweet_rate[0]:<15}, Tweet Rate: {max_tweet_rate[1]:.3f}, Likes: {max_tweet_rate[2]:,.0f}")
    print(f"User: {min_tweet_rate[0]:<15}, Tweet Rate: {min_tweet_rate[1]:.3f}, Likes: {min_tweet_rate[2]:,.0f}")
    plt.scatter(data[:, 0], data[:, 1])
    plt.xlabel("Average Tweet Rate")
    plt.ylabel("Average Number of Likes")
    plt.title("Average Likes by Average Tweet Rate")
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return "plot_likes_by_average_tweet_rate_per_user", plot_data


def plot_word_cloud(df):
    text = " ".join(df["content"])
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.imshow(wordcloud)
    plt.axis("off")
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return "plot_word_cloud", plot_data


def plot_sentiment_pie_chart(df):
    def _get_sentiment(text):
        scores = analyzer.polarity_scores(text)
        if scores['compound'] > 0.05:
            return "Positive"
        elif scores['compound'] < -0.05:
            return "Negative"
        else:
            return "Neutral"

    df['sentiment'] = df['content'].apply(_get_sentiment)

    df['sentiment'].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Sentiment Distribution")
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return "plot_sentiment_pie_chart", plot_data


def generate_analysis(dataset):
    original_df = pd.DataFrame(dataset)
    original_df["date_time"] = pd.to_datetime(original_df["date_time"], dayfirst=True)
    
    # Generate plots
    plots = [
        plot_tweets_by_day_of_week(original_df),
        plot_tweets_by_hour_of_day(original_df),
        plot_likes_by_condition_if_content_has_substrings(original_df, "#", "http"),
        plot_likes_by_average_sentiment_per_user(original_df),
        plot_likes_by_average_tweet_rate_per_user(original_df),
        plot_word_cloud(original_df),
        plot_sentiment_pie_chart(original_df),
    ]

    return {name: data for name, data in plots}

def getAllAnalysis(db):
    dataset = db.find_many("tweets",{})
    result = generate_analysis(dataset)
    return result

def getAnalysisByInput(data, db):
    dataset = db.find_many("tweets",{ "author" : data})
    result = generate_analysis(dataset)
    return result

