import requests

my_list_of_links = [
    # "http://www.hipstercode.com",
    # "http://www.hipstercode.com/about",
    "http://google.com/"
    ]

for index, link in enumerate(my_list_of_links):
    payload = {'q': 'test'}
    test = requests.get(link, params=payload)
    test.encoding = 'ISO-8859-1'

    # outfile = "/Users/richiewong/Documents/Python-Exercises/requests/test" + str(index) + ".txt"
    # with open(outfile, "w") as f_obj:
    #     f_obj.write(str(test.text))

    # GET HEADERS
    # print(test.headers)

    # GET COOKIES
    # print(test.cookies.get_dict())

    print(test.url)
