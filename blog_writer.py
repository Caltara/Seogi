import openai
import streamlit as st

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
