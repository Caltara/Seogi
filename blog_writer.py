import openai
import streamlit as st

# Generate a complete SEO blog post
def write_blog_post(title, keyword, audience, tone, cta):
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    prompt = f"""
    You are an expert SEO blog writer. Write a high-quality, SEO-optimized blog post titled "{title}" targeting the keyword "{keyword}".

    Guidelines:
    - Target audience: {audience}
    - Tone: {tone}
    - Include the keyword in the title, intro, and 3+ times throughout the content.
    - Use short paragraphs and bullet points where appropriate.
    - Structure: Introduction, 2–3 sections with H2 subheadings, and a conclusion.
    - End the post with this call to action: {cta}
    - Length: ~1600–1800 words.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert SEO blog writer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error generating blog post: {str(e)}"

# Suggest SEO blog titles based on keyword + audience
def suggest_blog_titles(keyword, audience):
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    prompt = f"""
    You are an expert SEO strategist. Suggest 5 catchy, SEO-optimized blog post titles based on the keyword "{keyword}" and designed for the audience: "{audience}".

    Guidelines:
    - Titles should be 6–12 words
    - Include the keyword
    - Be engaging and drive clicks
    - Optimized for SEO
    - Avoid clickbait, keep it helpful and relevant
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert SEO strategist."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        titles_raw = response.choices[0].message.content.strip().split("\n")

        # Clean and return a list of titles
        titles = [t.lstrip("0123456789. ").strip("- ").strip() for t in titles_raw if t.strip()]
        return titles

    except Exception as e:
        return [f"❌ Error generating titles: {str(e)}"]
