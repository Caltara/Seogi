from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Dummy backlink data – in a real app, fetch this from backlink tools APIs
DUMMY_BACKLINKS = [
    {"url": "https://example.com/page1", "anchor_text": "great service", "quality": "high"},
    {"url": "https://spammy-site.com/bad-link", "anchor_text": "cheap stuff", "quality": "low"},
    {"url": "https://partner.com/blog", "anchor_text": "partner article", "quality": "medium"},
]

def check_backlinks(domain):
    backlinks_summary = "\n".join(
        [f"- URL: {b['url']}, Anchor: {b['anchor_text']}, Quality: {b['quality']}" for b in DUMMY_BACKLINKS]
    )

    prompt = f"""
    Analyze the backlink profile for domain: {domain}

    Here are sample backlinks:
    {backlinks_summary}

    Provide insights on:
    - Which links are valuable or harmful
    - Overall backlink quality
    - Recommendations to improve backlink strategy
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert in SEO and backlink analysis."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error analyzing backlinks: {str(e)}"
