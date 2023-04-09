import sys
import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def search_links(html):
    links = []
    try:
        soup = BeautifulSoup(html, "html.parser")
        tags = soup.find_all("a", href=True)

        for tag in tags:
            link = tag["href"]
            if link.startswith("http"):
                links.append(link)

        return links
        
    except:
        pass


site = 'https://' + sys.argv[1]
to_crawl = [site]

crawled = set()



while 1:

    if to_crawl:
        url = to_crawl.pop()
        response = requests.get(url, verify=False)

        html = response.text

        links = search_links(html)

        if links:
            for link in links:
                if link not in crawled and link not in to_crawl:
                    to_crawl.append(link)

        
        crawled.add(url)
        print(f"crawling {url}")

    else:
        print('Done')
        break
