import requests
from bs4 import BeautifulSoup

for year in range(2015, 2020):
    res = requests.get("https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")

    images = soup.find_all("img", attrs = {"class":"thumb_img"})

    for idx, image in enumerate(images):
        # print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        
        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx + 1), "wb") as f: # wb: because it's an image file
            f.write(image_res.content) # content: ~가 가지고 있는 content(image)

        if idx >= 4:
            break