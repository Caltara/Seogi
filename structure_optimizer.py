import openai
import streamlit as st
import requests
from xml.etree import ElementTree

def analyze_structure(sitemap_url):
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    try:
        resp = requests.get(sitemap_url)
        if resp.status_code != 200:
            return {"error": f"Failed to fetch sitemap. Status code: {resp.status_code}"}

        # Parse sitemap XML URLs
        tree = ElementTree.fromstring(resp.content)
        urls = [elem.text for elem in tree.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]

        sample_urls = urls[:10]  # Sample first 10 for analysis

        prompt = f"""
        You are an SEO expert analyzing a website's structure.

        The sitemap contains these pages (sample 10):

        {chr(10).join(sample_urls)}

        Please:
        1. Evaluate the overall site structure and hierarchy.
        2. Suggest improvements for internal linking and navigation.
        3. Recommend best practices to enhance user experience and SEO crawlability.
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an SEO site structure expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content

    except Exception as e:
        return {"error": f"Error analyzing site structure: {str(e)}"}
