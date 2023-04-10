import streamlit as st
import snscrape.modules.twitter as sntwitter
import pandas as pd
import pymongo

def push_to_mongo(pd_tweets):
    client = pymongo.MongoClient("mongodb+srv://username:password@cluster0.gkstsrk.mongodb.net/?retryWrites=true&w=majority")
    dv = client.e12
    collection=dv.tweets
    push_status = collection.insert_many(pd_tweets.to_dict('records'))
    return push_status

def get_search_word(word):
    if word and word[0] == "#":
        return word[1:]
    else:
        return word


def get_date_input():
    start_date = st.date_input('From', key='start_date_{}')
    end_date = st.date_input('To', key='end_date_{}')
    if (start_date  and end_date) and (start_date <= end_date):
        return str(start_date.year)+"-"+str(start_date.month)+"-"+str(start_date.day), str(end_date.year)+"-"+str(end_date.month)+"-"+str(end_date.day) 
    else:
        st.markdown('<p style="font-weight:bold;color:red;">Error: End date must be either on the same start day or fall after start date.</p>', unsafe_allow_html=True)
        return None
    
def scrape_twitter(search_text, date_range=None, max_tweet=None):
    attributes_container = []
    scrape_text = search_text
    if date_range and date_range[0] and date_range[1]:
        from_date = date_range[0]
        to_date = date_range[1]
        if from_date != to_date:
            scrape_text += search_text + " since:" + from_date +" until:" + to_date

    if max_tweet == None:
        max_tweet = 10

    twts = sntwitter.TwitterSearchScraper(scrape_text).get_items()
    for i, tweet in enumerate(twts):
        if i>=max_tweet:
            break
        attributes_container.append([tweet.date, tweet.id, tweet.url, tweet.content, tweet.username, tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.sourceLabel, tweet.likeCount])
    tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "Id", "URL", "Tweet", "User", "Reply Count", "Retweet Count", "Language", "Source", "Like Count"])
    tweets_df.index = tweets_df.index + 1
    return tweets_df


def main():
    st.title("Tweet's scrapping app")
    st.write("#")

    word = st.text_input("Enter a keyword or hashtag:", key="word", value="twitter")
    st.write("")

    st.write("Enter data range:")
    date_range = get_date_input()
    st.write("#")

    number = st.number_input("Count of tweets to scrap :", step=1, value=10, format="%d")
    st.write("")
    st.write("")

    if st.button('Submit'):
        scapped_tweets = scrape_twitter(search_text=word, date_range=date_range, max_tweet=number)
        st.dataframe(scapped_tweets)
    
    st.write("#")

    if st.button("Push data to mongodb"):
        scapped_tweets = scrape_twitter(search_text=word, date_range=date_range, max_tweet=number)
        pushed_to_mongo = push_to_mongo(scapped_tweets)
        if pushed_to_mongo.acknowledged:
            st.markdown('<p style="font-weight:bold;color:green;">Data inserted in mongodb</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p style="font-weight:bold;color:red;">Error: Data not pushed to mongodb</p>', unsafe_allow_html=True)

    st.download_button(
        label="Download data as CSV",
        data=scrape_twitter(search_text=word, date_range=date_range, max_tweet=number).to_csv(),
        file_name='tweets.csv',
        mime='text/csv',
    )

    st.download_button(
        label="Download data as Json",
        data=scrape_twitter(search_text=word, date_range=date_range, max_tweet=number).to_json(),
        file_name='tweets.json',
        mime='text/json',
    )

main()
