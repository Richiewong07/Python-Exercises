import requests

from bs4 import BeautifulSoup

url = "https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Sugar+Land%2C+TX"

r = requests.get(url)

# CONVERT CONTENT GIVEN BY r.content
soup = BeautifulSoup(r.content, "lxml")

# print(soup.prettify())

# "a" IS HTML TAG
# links = soup.find_all("a")
#
# for link in links:
#     try:
#         if "http" in link.get("href"):
#             print("<a href= '{}'> {} </a>".format(link.get("href"), link.text))
#     except TypeError:
#         pass


g_data = soup.find_all("div", {"class": "info"})

for item in g_data:
    print(item.contents[0].find_all("a", {"class": "business-name"})[0].text)
    try:
        # print(item.contents[1].find_all("p", {"class": "adr"})[0].text)
        # print(item.contents[1].find_all("li", {"class": "primary"})[0].text)
        print(item.contents[1].find_all("span", {"itemprop": "address"})[0].text)
        # print(item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text)
        # print(item.contents[1].find_all("span", {"itemprop": "addressLocality"})[0].text.replace(',', ' '))
        # print(item.contents[1].find_all("span", {"itemprop": "addressRegion"})[0].text)
        # print(item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text)
    except:
        pass
