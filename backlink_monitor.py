import openai
import streamlit as st

# Dummy backlink data for demonstration
DUMMY_BACKLINKS = [
    {"url": "https://example.com/page1", "anchor_text": "great service", "quality": "high"},
    {"url": "https://spammy-site.com/bad-link", "anchor_text": "cheap stuff", "quality": "low"},
    {"url": "https://partner.com/blog", "anchor_text": "partner article", "quality": "medium"},
]

def check_backlinks(domain):
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    # Summarize backlink profile and give advice using GPT
    backlinks_summary = "\n".join(
        [f"- URL: {b['url']}, Anchor: {b['anchor_text']}, Quality: {b['quality']}" for b in DUMMY_BACKLINKS]
    )

    prompt = f"""
    You are an SEO specialist analyzing backlinks.

    The following backlinks are pointing to the domain: {domain}

    {backlinks_summary}

    Please:
    1. Identify any potentially harmful or low-quality backlinks.
    2. Suggest which backlinks to keep or build upon.
    3. Provide recommendations for improving the backlink profile.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an SEO backlink expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error analyzing backlinks: {str(e)}"
