import requests, sys
from bs4 import BeautifulSoup

page = requests.get("https://medium.com/@{}/latest".format(sys.argv[1]))
soup = BeautifulSoup(page.content, "lxml")

def is_post_link(tag):
    return tag.name == "a" and "https://medium.com/@adamshort/" in tag["href"]

a_links = list(soup.find_all("div", "postArticle-content"))
print len(a_links)
