from urlextract import URLExtract
import pandas as pd
from collections import Counter

extractor = URLExtract()

def fetch_stats(selected_user, df):
    """Calculates core KPIs: total messages, words, media, and links."""
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]
    words = []
    for message in df['message']:
        words.extend(message.split())

    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    links = []
    for message in df['message']:
        links.extend(extractor.find_urls(message))

    return num_messages, len(words), num_media_messages, len(links)

def most_busy_users(df):
    """Returns the top contributors and their percentage share in a group."""
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'user': 'percent'})
    return x, df

def most_common_words(selected_user, df):
    """Finds the most frequently used words, ignoring standard stop words."""
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    stop_words = ['the', 'is', 'a', 'to', 'and', 'in', 'of', 'i', 'it', 'for', 'you', 'my', 'that']
    
    words = []
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df