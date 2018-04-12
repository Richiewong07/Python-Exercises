import requests

from bs4 import BeautifulSoup

r = requests.get("https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Sugar+Land%2C+TX")

# CONVERT CONTENT GIVEN BY r.content
soup = BeautifulSoup(r.content, "lxml")

# print(soup.prettify())

# "a" IS HTML TAG
links = soup.find_all("a")

for link in links:
    link_text = link.text
    link_href = link.get("href")
    # print(link_text, link_href)
    print("<a href= '{}' > {} </a>".format(link_href, link_text))


g_data = soup.find_all("div", {"class": "info"})
