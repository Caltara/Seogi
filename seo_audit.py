import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_page_html(url):
    # Ensure URL starts with http:// or https://
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def audit_seo(url):
    html = get_page_html(url)
    if not html:
        return {"error": "Unable to retrieve page. Please check the URL or try again later."}

    soup = BeautifulSoup(html, 'lxml')

    # Extract SEO elements
    title = soup.title.string.strip() if soup.title else "Missing"
    meta_desc_tag = soup.find("meta", attrs={"name": "description"})
    meta_desc = meta_desc_tag['content'].strip() if meta_desc_tag and meta_desc_tag.get("content") else "Missing"
    h1_tags = [h1.get_text(strip=True) for h1 in soup.find_all('h1')]
    word_count = len(soup.get_text().split())

    return {
        "Title Tag": title,
        "Meta Description": meta_desc,
        "H1 Tags": h1_tags,
        "Word Count": word_count
    }
