import requests
from bs4 import BeautifulSoup

# This quote scraping game scrapes information from quotes.toscrape.com and then challenges the player to guess the person who said or wrote that quote.

# Get the response object from quotes.toscrape.com
response = requests.get("http://quotes.toscrape.com/")
# print(response.text)

# We will need to scrape quotes from every single page on this website. So let's first build a list of URLs that we will need to scrape from. Start by initializing a list with the base URL

URLs_to_scrape = ['http://quotes.toscrape.com/']
next_page_exists = True
while next_page_exists:
        soup = BeautifulSoup(response.text, "html.parser")

        # Get the next page URL by searching for the "next" <li> class, if it exists.
        # If it does exist, drill down to get the href from the anchor tag
        if soup.find(class_ = "next"):
                next_page = soup.find(class_ = "next").find('a')['href']
                # Update the next_page variable to include the entire URL that will need to be visited next
                next_page_full = f"http://quotes.toscrape.com{next_page}"
                # Append the full URL to the list of URLs to scrape
                URLs_to_scrape.append(next_page_full)
                # Now update the response response so that the next cycle of the loop goes into the 
                response = requests.get(next_page_full)
        # If the "next" class does not exist on the current page, break out of the loop as there are no further pages to scrape
        else:
                break

# print(URLs_to_scrape)

# Create an empty list of quotes, authors, and bios to be populated with this information.
quotes_list = []

# Now that we have the URLs, let's work our way through them one by one
for page in URLs_to_scrape:
        response = requests.get(page)
        soup = BeautifulSoup(response.text, "html.parser")
        # print(response.text)

        # Each self-contained quote is within a class called "text"
        all_quotes_on_page = soup.find_all(class_='quote')
        # print(quote)
        # For each quote, dig down into the text div to get the text of the quote
        for quote in all_quotes_on_page:
                quote_text = quote.find(class_='text').get_text()
                # print(quote_text)

                # The author is found within a class called "author", which is also within the quote class
                author = quote.select(".author")[0].get_text()
                # print(author)

                # Finally, get the URL for the bio page. This is also within the quote lcass under an anchor tag
                bio_link = f"http://quotes.toscrape.com{quote.find('a')['href']}"
                # print(bio_link)

                # Store the information in a the quotes list, with each quote being a list of the quote, author, and bio link. This will be a list of lists.
                quotes_list.append([quote_text, author, bio_link])

print(f"This list contains {len(quotes_list)} quotes.")

### The code below dictates the game logic

