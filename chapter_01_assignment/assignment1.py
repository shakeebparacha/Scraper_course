from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup

def get_status(url):

    try:
        html = urlopen(url)
    except URLError:
        print("There is an error.")
        return None

    try:
        bs = BeautifulSoup(html.read(), "html.parser")

        title = bs.title
        heading = bs.h1
        paragraph = bs.p
        div = bs.div

    except AttributeError:
        print("Tag was not found.")
        return None

    print("Status: Completed Successfully")
    return title, heading, paragraph, div


status = get_status("http://www.pythonscraping.com/pages/page1.html")

if status is None:
    print("There is no status")
else:
    print(status)



