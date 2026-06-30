from urlextract import URLExtract
extract= URLExtract()

from wordcloud import WordCloud
import pandas as pd
from collections import Counter

def fetch_data(selected_user,df):
    if selected_user != "Overall":
        df = df[df["user"] == selected_user]
    # fetch num of messages
    num_messages =df.shape[0]

    #fetch num of words
    words=[]
    for message in df['message']:
        words.extend(message.split())

    #fetch num of media messages
    num_media_messages= df[df['message']== '<Media omitted>\n'].shape[0]

    #fetch number of links
    links = []

    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words), num_media_messages, len(links)

def most_busy_user(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(columns={'count': 'percent'})
    return x,df

def create_wordcloud(selected_user,df):
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    #     # fetch no. of messages
    #     num_messages = df.shape[0]
    #
    #     # number of words
    #     words = []
    #     for message in df['message']:
    #         words.extend(message.split())
    #
    #     return num_messages,len(words)
    #
    # else:
    #
    #     new_df= df[df["user"]==  selected_user ]
    #     num_messages = new_df.shape[0]                 ## shape[0] mean no. of row in the selected user dataframe
    #     words = []
    #     for message in new_df['message']:
    #         words.extend(message.split())
    #
    #     return num_messages,len(words)