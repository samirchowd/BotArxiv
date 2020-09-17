from bs4 import BeautifulSoup
import urllib.request

# Defining functions in order to make tweet
def get_url(subject):
    """Retrives url given a subject area"""
    url = "https://arxiv.org/list/" + subject + "/new"
    return url 

def get_html(url):
    """Retrieves the HTML content of a given url"""
    content = urllib.request.urlopen(url)

    html = content.read()

    content.close()

    return html

def parse_html(html):
    """Returns a parsed soup object given any HTML"""
    soup = BeautifulSoup(html, 'html.parser')

    return soup

def get_title(soup):
    """Returns the first title on the given parsed HTML"""
    titles = soup.findAll('div', {'class':'list-title mathjax'})

    for i in range(len(titles)):
        titles[i] = titles[i].text.split(': ')[1]
    
    return titles[0]

def get_link(soup):
    """Returns the first link on the given parsed HTML"""
    links = soup.findAll('span', {'class':'list-identifier'})

    for i in range(len(links)):
        links[i] = links[i].a.text.split(':')[1]

    return links[0]

def generate_ref(link):
    """Generates an Arxiv link based on the DOI"""
    return "https://arxiv.org/abs/" + link

# Master function that creates a single formatted tweet
def make_tweet(subject):
    """Returns a formatted tweet given a subject""" 
    url = get_url(subject)

    html = get_html(url)

    soup = parse_html(html)

    title = get_title(soup)

    link = get_link(soup)

    ref = generate_ref(link)

    tweet = "{}\n{}".format(title, ref)

    return tweet

    

    