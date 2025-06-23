from openai import OpenAI
import streamlit as st
from bs4 import BeautifulSoup

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def optimize_page(raw_html, target_keyword):
    # Extract content from HTML
    soup = BeautifulSoup(raw_html, "html.parser")
    title = soup.title.string if soup.title else "No title"
    desc_tag = soup.find("meta", attrs={"name": "description"})
    meta_desc = desc_tag["content"] if desc_tag and "content" in desc_tag.attrs else ""
    visible_text = " ".join(soup.stripped_strings)[:300]

    # Prompt for GPT
    prompt = f"""
    Analyze this web page content for SEO performance.

    Title: "{title}"
    Meta Description: "{meta_desc}"
    Snippet of Visible Text: "{visible_text}"

    Provide detailed suggestions to improve SEO, focusing on keyword integration, readability, meta tags, headers, and structure.
    Target keyword: "{target_keyword}"
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an SEO consultant and page optimization expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error optimizing page: {str(e)}"
