from bs4 import BeautifulSoup
import urllib.request

htmlObj = urllib.request.urlopen('https://www.ua-football.com/')
html = htmlObj.read()

soup = BeautifulSoup(html, 'html.parser')

items = soup.find_all('li', class_='mb-3')

results = []

for item in items:
    title = item.find('span', class_='heading').get_text(strip=True)
    desc = item.find('span', class_='name-dop').get_text(strip=True)
    link = item.a.get('href')

    results.append({
        'title': title,
        'desc': desc,
        'link': link
    })

f = open('parsed.txt', 'w', encoding='utf-8')
f.write('PARSED ARTICLES\n\n')
i = 1
for item in results:
    f.write(f"Article #{i}\nTitle: {item['title']}\nDescription: {item['desc']}\nLink: {item['link']}\n\n*******************************************************\n\n")
    i += 1

f.close()
