import requests
from bs4 import BeautifulSoup
import tldextract

def get_page_html(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    return response.text if response.status_code == 200 else None

def audit_seo(url):
    html = get_page_html(url)
    if not html:
        return {"error": "Unable to retrieve page"}

    soup = BeautifulSoup(html, 'lxml')
    title = soup.title.string if soup.title else "Missing"
    meta_desc = soup.find("meta", attrs={"name": "description"})
    meta_desc = meta_desc['content'] if meta_desc else "Missing"
    h1_tags = [h1.text.strip() for h1 in soup.find_all('h1')]
    
    return {
        "Title Tag": title,
        "Meta Description": meta_desc,
        "H1 Tags": h1_tags,
        "Word Count": len(soup.get_text().split())
    }
