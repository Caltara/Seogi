import openai
import streamlit as st
from bs4 import BeautifulSoup

def optimize_page(raw_html, target_keyword):
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    # Use BeautifulSoup to parse HTML and extract text & meta info
    soup = BeautifulSoup(raw_html, "html.parser")

    # Extract title and meta description if present
    title = soup.title.string if soup.title else "No title found"
    meta_desc = ""
    desc_tag = soup.find("meta", attrs={"name":"description"})
    if desc_tag and "content" in desc_tag.attrs:
        meta_desc = desc_tag["content"]

    # Extract visible text for keyword density check
    texts = soup.stripped_strings
    visible_text = " ".join(texts)

    # Prompt for GPT to analyze the page content
    prompt = f"""
    You are an SEO expert. Analyze the following webpage content for SEO optimization targeting the keyword: "{target_keyword}".

    Current page title: "{title}"
    Meta description: "{meta_desc}"
    Page content excerpt (first 300 chars): "{visible_text[:300]}"

    Please:
    1. Identify missing or weak SEO elements (title, meta description, headers).
    2. Suggest improvements to better target the keyword.
    3. Recommend content or structural changes to increase SEO effectiveness.

    Provide actionable suggestions in a numbered list.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an SEO optimization consultant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error optimizing page: {str(e)}"
