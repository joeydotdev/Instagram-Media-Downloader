from bs4 import BeautifulSoup
import requests

class Instagram:

    def __init__(self, url):
        self.url = url
        self.source_code = requests.get(self.url).text
        self.scrape_page()

    def __repr__(self):
        return str(self.url)

    def validate(self):
        if self.source_code.find("Sorry, this page") > -1 or self.url.find("/p/") == -1:
            raise Exception("Invalid Instagram Media URL")
        return True

    def scrape_page(self):
        if self.validate():
            self.soup = BeautifulSoup(self.source_code, "html.parser")
            self.media_type = self.soup.find("meta", {'property': 'og:type'})['content']
            self.post_id = self.soup.find("meta", {'property': 'og:url'})['content'][-12:-1]

    def get_media_type(self):
        return self.media_type

    def get_post_id(self):
        return self.post_id

    def get_download_url(self):
        if self.media_type == "instapp:photo":
            return self.soup.find("meta", {'property': 'og:image'})['content']
        elif self.media_type == "video":
            return self.soup.find("meta", {'property': 'og:video:secure_url'})['content']

    def get_source_code(self):
        return self.source_code

