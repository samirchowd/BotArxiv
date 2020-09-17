from bs4 import BeautifulSoup
import urllib.request

# Setting up connection and grabbing data
url = 'https://arxiv.org/list/physics/new'
content = urllib.request.urlopen(url)

html = content.read()

content.close()

# Parsing the HTML 
soup = BeautifulSoup(html, 'html.parser')

# Retriving titles and extrating the text
titles = soup.findAll('div', {'class':'list-title mathjax'})

for i in range(len(titles)):
    titles[i] = titles[i].text.split(': ',1)[1]

print(titles[0])
# Retriving all the links or doi values
links = soup.findAll('span', {'class':'list-identifier'})

for i in range(len(links)):
    links[i] = links[i].a.text.split(':')[1]

print(links[0])

print('https://arxiv.org/abs/' + links[0])


def get_url(subject):
    url = "https//arxiv.org/list" + subject + "new"
    return url 

def get_html(url):
    content = urllib.request.urlopen(url)

    html = content.read()

    content.close()

    return html

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    return soup

def get_title(soup):
    # Retriving titles and extrating the text
    titles = soup.findAll('div', {'class':'list-title mathjax'})

    for i in range(len(titles)):
        titles[i] = titles[i].text.split(': ')[1]
    
    return titles[0]

def get_link(soup):
    # Retriving all the links or doi values
    links = soup.findAll('span', {'class':'list-identifier'})

   # Retriving all the links or doi values
    links = soup.findAll('span', {'class':'list-identifier'})

    for i in range(len(links)):
        links[i] = links[i].a.text.split(':')[1]

    return links[0]

def generate_url(link):
    return "https://arxiv.org/list" + link

def get_tweet(subject):
    url = get_url(subject)

    html = get_html(url)

    soup = parse_html(html)

    title = get_title(soup)

    link = get_link(soup)

    