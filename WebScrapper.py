import gspread
from oauth2client.service_account import ServiceAccountCredentials
from urllib.request import urlopen as urlopen
from bs4 import BeautifulSoup as soup

scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('secret.json',scope)
gclient = gspread.authorize(creds)

sheet = gclient.open('ostl-project').sheet1
sheet2 = gclient.open('ostl-project').worksheet('Sheet2')

values_list = sheet.col_values(1)

def scrappy(url):
    client = urlopen(url)

    pagehtml = client.read()

    client.close

    pagesoup = soup(pagehtml, "html.parser")
    print('hello')

    name = pagesoup.h1.span.text
    print(str(name))

    price = pagesoup.find("div", {"class": "_3auQ3N _1POkHg"}).text

    print(str(price))

    discount = pagesoup.find("div", {"class": "_1vC4OE _3qQ9m1"}).text


    print(str(discount))

    rating = pagesoup.find("div", {"class": "hGSR34"}).text

    print(str(rating))

    dilivery = pagesoup.find("div", {"class": "_29Zp1s"}).text

    print(str(dilivery))

    emi = pagesoup.find("li", {"class": "_2-n-Lg col"}).text

    print(str(emi))

    ratings = pagesoup.find("span", {"class": "_38sUEc"}).span.span.text

    print(str(ratings))


    reviews = pagesoup.find("span", {"class": "_38sUEc"}).span.span.next_sibling.next_sibling.text

    print(str(reviews.strip()))

    star = pagesoup.findAll("div", {"class": "CamDho"})

    star1 = star[0]
    star1 = str(star1.text).strip()
    print(star1)

    star2 = star[1]
    star2 = str(star2.text).strip()
    print(star2)

    star3 = star[2]
    star3 = str(star3.text).strip()
    print(star3)

    star4 = star[3]
    star4 = str(star4.text).strip()
    print(star4)

    star5 = star[4]
    star5 = str(star5.text).strip()
    print(star5)

    sheet2.append_row([name,price,discount,dilivery,ratings,reviews,star1,star2,star3,star4,star5])

for itemurl in values_list:
    scrappy(itemurl)

sheet2.append_row(['.'])
sheet2.append_row(['New iteration'])
sheet2.append_row(['.'])
