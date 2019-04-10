from urllib.request import urlopen as urlopen
from bs4 import BeautifulSoup as soup

url = 'https://www.flipkart.com/stealodeal-aluminium-zipper-headphone-case/p/itmf27yfbzfag4zs?pid=HPPF27UVHH5CSGZW&lid=LSTHPPF27UVHH5CSGZWY6Y1SN&marketplace=FLIPKART&fm=productRecommendation%2FcrossSelling&iid=R%3Ac%3Bp%3AACCEXQ6YHAXTCNQT%3Bpt%3App%3Buid%3Aeb040093-c87e-bedd-44a7-dc9cc1f3ed52%3B.HPPF27UVHH5CSGZW.LSTHPPF27UVHH5CSGZWY6Y1SN&ppt=ProductPage&ppn=ProductPage&ssid=y7sxieq6400000001554134460823&otracker=pp_reco_Bought%2BTogether_15_32.productCard.PMU_TAB_Stealodeal%2BAluminium%2BZipper%2BHeadphone%2BCase_HPPF27UVHH5CSGZW.LSTHPPF27UVHH5CSGZWY6Y1SN_productRecommendation%2FcrossSelling_2&cid=HPPF27UVHH5CSGZW.LSTHPPF27UVHH5CSGZWY6Y1SN'

client = urlopen(url)

pagehtml = client.read()

client.close

pagesoup = soup(pagehtml, "html.parser")
print('hello')

print(str(pagesoup.h1.span.text))

price = pagesoup.find("div", {"class": "_3auQ3N _1POkHg"}).text

print(str(price))

discount = pagesoup.find("div", {"class": "_1vC4OE _3qQ9m1"}).text


print(str(discount))

rating = pagesoup.find("div", {"class": "hGSR34"}).text

print(str(rating))

emi = pagesoup.find("li", {"class": "_2-n-Lg col"}).text

print(str(emi))

ratings = pagesoup.find("span", {"class": "_38sUEc"}).span.span.text

print(str(ratings))


reviews = pagesoup.find(
    "span", {"class": "_38sUEc"}).span.span.next_sibling.next_sibling.text

print(str(reviews.strip()))

star = pagesoup.findAll("div", {"class": "CamDho"})

for star1 in star:
    print(str(star1.text).strip())
