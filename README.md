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

<img src="https://user-images.githubusercontent.com/112666126/230741692-3efad137-8173-4f21-b328-6b2a3cc2c55b.png" width="600" height="700">



1. The user is supposed to enter a word or hastag.

2. Choose a data range : Choose a start date (**From**) and end date(**To**). **If the default 'From' and 'To' date is not changed, all the tweets with the keyword or hashtag will be displayed.**

3. Enter the number of tweets to be scrapped.

4. After entering all inputs, click the Submit button.The tweets will be displayed.

5. Then based on the user choice, they can **push data to mongoDB** or **download data as CSV** or **download data as Json**.


**Output**
------------

![Screenshot from 2023-04-09 01-42-45](https://user-images.githubusercontent.com/112666126/230740831-ff783490-f778-4280-9b03-c29fcdf22952.png)


The tool displays tweets based on the specified search keyword or hashtag, date range, and the desired number of tweets to be scraped. The number of tweets displayed is restricted based on the count of tweets specified by the user. **The newest tweets are displayed first.**


**Pushing Data to mongoDB**
------------
Click "push to mongodb" button.Once the data is pushed into Mongo database,**'Data inserted in mongodb'** would be shown on the app.
![Screenshot from 2023-04-09 01-49-59](https://user-images.githubusercontent.com/112666126/230741249-0e58e235-9697-4ce8-903c-b0cd8b2b006b.png)

**Data pushed into MongoDB , displayed using MongoDB atlas**
![Screenshot from 2023-04-09 01-57-31](https://user-images.githubusercontent.com/112666126/230741330-c0a48157-bdbe-4f11-bd30-9f2b795e5e57.png)



**Data downloaded in CSV Format(displayed using google sheets)**
------------
![Screenshot from 2023-04-09 02-14-36](https://user-images.githubusercontent.com/112666126/230741862-253fe3f5-7634-4629-a3f3-37a3561bae13.png) 

**Data downloaded in Json Format**
------------
![Screenshot from 2023-04-09 02-19-49](https://user-images.githubusercontent.com/112666126/230742074-7b0f42fd-3fa8-435e-9700-1644946ec746.png)
