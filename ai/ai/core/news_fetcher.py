import requests

class NewsFetcher:
    def __init__(self):
        self.sources = [
            "https://newsapi.org/v2/top-headlines?category=business",
            "https://newsapi.org/v2/top-headlines?category=technology"
        ]

    def get_latest_news(self):
        news_list = []
        for url in self.sources:
            try:
                response = requests.get(url)
                data = response.json()
                if "articles" in data:
                    news_list.extend(data["articles"])
            except:
                pass
        return news_list
