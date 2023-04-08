# Tweet's scrapping app #

[Link to access the app](https://arthimurali-twitter-scrapping-tool.hf.space/)

**Overview**
------------
Tweet's scrapping app is a application that enables users to extract tweets from scattered tweet data, based on the search term,data range,count of tweets to be scraped , given by the user. This app  helps the user get specific tweet details of their interest.

**Developed using:**
------------
1. **Language** - Python (Libraries used used snscrape,pandas,Pymongo)
2. **Database** - MongoDB
3. **Front-end/GUI** - Streamlit

**User-Interface**
------------

1. The user is supposed to enter a word or hastag.
2. Choose a start date (**From**) and end date(**To**). **If the default 'From' and 'To' date is not changed, all the tweets with the keyword or hashtag will be displayed.**
3. Enter the number of tweets to be scrapped.
4. After entering all inputs, click the Submit button.The tweets will be displayed.
5. Then based on the user choice, they can **push data to mongoDB** or **download data as CSV** or **download data as Json**.
6. 
