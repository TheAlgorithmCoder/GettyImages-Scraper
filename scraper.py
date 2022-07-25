import requests
from bs4 import BeautifulSoup
import urllib.request
import progressbar


class scraping():
    def __init__(self):
        self.page = 1

    def scraper(self, phrase):
        headers = requests.utils.default_headers()
        headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}) # bypass GettyImage Request denied

        while True:
            url = f"https://www.gettyimages.co.uk/photos/{phrase}?assettype=image&license=rf&phrase={phrase}&sort=mostpopular&page={self.page}"
            get_soup = requests.get(url, headers=headers)
            soup = BeautifulSoup(get_soup.text, "lxml")
            pics = soup.findAll("img", {"class": "MosaicAsset-module__thumb___yvFP5"})# Search all Thumbnails 
            for pic in progressbar.progressbar(pics, prefix=f"Crawling Pictures [{phrase}]"): 
                try:

                    urllib.request.urlretrieve(pic.get("src"), f"Images/{pic.get('alt')}.jpg")
                except:
                    return
            self.page +=1


def main():
    search = input("Phrase: ")
    scraping().scraper(search)

if __name__ == "__main__":
    main()