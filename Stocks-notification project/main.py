import requests
from twilio.rest import Client
import os

#STOCK DATA
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

percent_change = -6
if abs(percent_change) >= 5:

    NEWS_PARAMETERS = {
        "q": COMPANY_NAME,
        "sortBy": "publishedAt",
        "apiKey": os.getenv("NEWS_API_KEY"),
    }

    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    news_response = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    news_data = news_response.json()
    articles = news_data.get("articles", [])[:3]
    if not articles:
        print("No articles found.")
        exit()

    client = Client(os.getenv("ACCOUNT_SID"), os.getenv("AUTH"))

    arrow = "🔺" if percent_change > 0 else "🔻"

    articles = news_data.get("articles", [])[:3]
# NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
# news_response = requests.get(url= NEWS_ENDPOINT,params=NEWS_PARAMETERS)
# news_data = news_response.json()
# article  = news_data["articles"][0]["title"]
# description = news_data["articles"][0]["description"]
# articles = news_data["articles"]
# print(articles[:3])
# Only trigger if change is 5% or more

if abs(percent_change) >= 5:

    NEWS_PARAMETERS = {
        "q": COMPANY_NAME,
        "sortBy": "publishedAt",
        "apiKey": os.getenv("NEWS_API_KEY"),
    }

    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    news_response = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    news_data = news_response.json()

    articles = news_data.get("articles", [])[:3]

    if not articles:
        print("No articles found.")
        exit()

    client = Client(os.getenv("ACCOUNT_SID"), os.getenv("AUTH"))

    arrow = "🔺" if percent_change > 0 else "🔻"

    for article in articles:
        message = client.messages.create(
            body=f"""{STOCK_NAME}: {arrow}{abs(percent_change)}%
Headline: {article['title']}
Brief: {article['description']}""",
            from_=os.getenv("PHONE_NUMBER"),
            to=os.getenv("MY_PHONE"),
        )

else:
    print("Price change less than 5% — no alert sent.")
# percent_change = 4
# if percent_change > 5:
#     client = Client(os.getenv('ACCOUNT_SID'), os.getenv('AUTH'))
#     message = client.messages.create(
#         body=f"{STOCK_NAME} price increase🟢🔼📈 5% \n{article}\n{description}",
#         from_=os.getenv('PHONE_NUMBER'),
#         to="+any number!",
#     )
# elif percent_change < 5:
#     client = Client(os.getenv('ACCOUNT_SID'), os.getenv('AUTH'))
#     message = client.messages.create(
#         body=f"{STOCK_NAME} decrease🔴🔽📉 5%\n{article}\n{description}",
#         from_=os.getenv('PHONE_NUMBER'),
#         to="any number!",
#     )
# else:
#     print(None)





    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

