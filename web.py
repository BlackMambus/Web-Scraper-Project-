import requests
from bs4 import BeautifulSoup

# Target website (example: Hacker News)
URL = "https://news.ycombinator.com/"

def scrape_hacker_news():
    response = requests.get(URL)
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.select('.titleline > a')

    print("📰 Top Hacker News Articles:\n")
    for i, title in enumerate(titles[:10], 1):  # Top 10 articles
        print(f"{i}. {title.text}")
        print(f"   Link: {title['href']}\n")

if __name__ == "__main__":
    scrape_hacker_news()


