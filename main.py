import requests
from bs4 import BeautifulSoup

def extract_competitors():
    url = "https://www.marketing91.com/amazon-competitors/"
    web = requests.get(url)
    soup = BeautifulSoup(web.content, "html.parser")

    paragraphs = [p.text.strip() for p in soup.find_all("p") if p.text.strip()]
    
    competitors = []
    for line in paragraphs:
        if any(keyword in line.lower() for keyword in ["competitor", "alternative", "similar to amazon"]):
            competitors.append(line)

    return {
        "source": url,
        "total_paragraphs": len(paragraphs),
        "competitor_related": competitors
    }
