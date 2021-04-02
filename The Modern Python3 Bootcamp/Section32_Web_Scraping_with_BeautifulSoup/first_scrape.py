# In this exercise we scrape the website https://www.rithmschool.com/blog, collecting the blog titles, links, and dates, and then publish them to a CSV file

import requests
from bs4 import BeautifulSoup
import csv

# Request the HTML
response = requests.get("https://www.rithmschool.com/blog")
# Check the text to ensure you get when you wanted
# print(response.text)

## The Approach!
# Note that each blog post is within an <article> tag. What we will want to do is first select all articles in HTML. Then within each article, we'll want to select the <h4> tag and the anchor tag within, where we will save the URL and the title of the text. Finally, for the date, we will select the datetime metadata that's embedded in the page

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")
# print(articles)

# To get the title, let's dive into the first anchor tag of each article. We can use soup.find instead of soup.find_all since the first anchor tag of each article has the information we need.

# open the CSV!
with open("blog_data.csv", "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write the headers row of the CSV
        csv_writer.writerow(["title", "link", "date"])

        for article in articles:
                # Save the article.find("a") command in a variable for the anchor tag, which will make it easier to use later
                a_tag = article.find("a")

                # print(article.find("a").get_text())

                # get the title, which can be done using the get_text() method
                title = a_tag.get_text()

                # Get the URL
                url = f'https://www.rithmschool.com{a_tag["href"]}'

                # Get the date, which is within a <time> element. However, what we really want is the value of the datetime attribute
                date = article.find("time")["datetime"][0:10]
                # print(title, url, date)

                csv_writer.writerow([title, url, date])



        