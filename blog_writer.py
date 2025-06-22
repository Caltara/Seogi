import openai
import streamlit as st

# Generate full SEO blog post
def write_blog_post(title, keyword, audience, tone, cta):
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    prompt = f"""
    Write a high-quality, SEO-optimized blog post titled "{title}" targeting the keyword "{keyword}".

    Guidelines:
    - Tailor the content for this audience: {audience}.
    - Use this tone: {tone}.
    - Include the keyword in the title, introduction, and at least 3 times throughout.
    - Include an introduction, 2–3 informative sections with H2 subheadings, and a conclusion.
    - End the post with this call to action: {cta}.
    - Use short paragraphs, and bullet points if helpful.
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

# Suggest SEO blog titles before writing
def suggest_blog_titles(keyword, audience):
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    prompt = f"""
    You are an expert SEO content strategist. Suggest 5 catchy, SEO-optimized blog post titles that would appeal to this audience: "{audience}", and are based on the keyword: "{keyword}".

    Make the titles:
    - Between 6–12 words
    - Focused on generating clicks and improving SEO
    - Clear and professional
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
        # Clean up titles
        titles = [t.lstrip("0123456789. ").strip("- ").strip() for t in titles_raw if t.strip()]
        return titles

    except Exception as e:
        return [f"❌ Error generating titles: {str(e)}"]
