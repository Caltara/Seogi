from openai import OpenAI
import streamlit as st
import requests
from xml.etree import ElementTree

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def analyze_structure(sitemap_url):
    try:
        response = requests.get(sitemap_url, timeout=10)
        if response.status_code != 200:
            return f"❌ Failed to fetch sitemap. Status code: {response.status_code}"

        tree = ElementTree.fromstring(response.content)
        urls = [elem.text for elem in tree.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
        sample_urls = urls[:10]  # Limit sample size for prompt length

        prompt = f"""
        You are an expert in SEO and site architecture. Analyze the following list of URLs from a sitemap:

        {chr(10).join(sample_urls)}

        Based on these URLs, provide:
        - An assessment of site structure and internal linking strategy
        - Suggestions for improving crawlability, user navigation, and SEO
        - Any issues you detect with the URL structure
        """

        ai_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an SEO site structure and architecture expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return ai_response.choices[0].message.content.strip()
    
    except Exception as e:
        return f"❌ Error analyzing site structure: {str(e)}"
