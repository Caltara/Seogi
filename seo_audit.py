import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_page_html(url):
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

def analyze_length(tag, optimal_min, optimal_max):
    if tag == "Missing":
        return "Missing"
    length = len(tag)
    if length < optimal_min:
        return f"Too short ({length} chars). Recommended: {optimal_min}-{optimal_max}."
    elif length > optimal_max:
        return f"Too long ({length} chars). Recommended: {optimal_min}-{optimal_max}."
    else:
        return f"Good ({length} chars)."

def audit_seo(url, target_keyword=None):
    html = get_page_html(url)
    if not html:
        return {"error": "Unable to retrieve page. Please check the URL or try again later."}

    soup = BeautifulSoup(html, 'lxml')

    title = soup.title.string.strip() if soup.title else "Missing"
    meta_tag = soup.find("meta", attrs={"name": "description"})
    meta_desc = meta_tag['content'].strip() if meta_tag and meta_tag.get("content") else "Missing"
    h1_tags = [h1.get_text(strip=True) for h1 in soup.find_all('h1')]
    word_count = len(soup.get_text().split())

    # Start audit with recommendations
    recommendations = []

    # Title analysis
    title_analysis = analyze_length(title, 50, 60)
    if "Missing" in title_analysis:
        recommendations.append("Add a title tag.")
    elif target_keyword and target_keyword.lower() not in title.lower():
        recommendations.append(f"Add the target keyword '{target_keyword}' to the title.")

    # Meta description analysis
    meta_analysis = analyze_length(meta_desc, 140, 160)
    if "Missing" in meta_analysis:
        recommendations.append("Add a meta description.")
    elif target_keyword and target_keyword.lower() not in meta_desc.lower():
        recommendations.append(f"Include the target keyword '{target_keyword}' in the meta description.")

    # H1 analysis
    if not h1_tags:
        recommendations.append("Missing H1 tag.")
    elif len(h1_tags) > 1:
        recommendations.append("Multiple H1 tags found. Use only one primary H1 per page.")
    elif target_keyword and target_keyword.lower() not in h1_tags[0].lower():
        recommendations.append(f"Include the target keyword '{target_keyword}' in the H1.")

    # Word count analysis
    if word_count < 300:
        recommendations.append("Content is too short. Aim for at least 300+ words for SEO.")

    # Result
    return {
        "Title Tag": title,
        "Title Analysis": title_analysis,
        "Meta Description": meta_desc,
        "Meta Description Analysis": meta_analysis,
        "H1 Tags": h1_tags,
        "Word Count": word_count,
        "Recommendations": recommendations
    }
