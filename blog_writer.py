from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def write_blog_post(title, keyword, audience, tone, cta):
    prompt = f"""
    You are an expert SEO blog writer. Write a high-quality, SEO-optimized blog post titled "{title}" targeting the keyword "{keyword}".

    Guidelines:
    - Target audience: {audience}
    - Tone: {tone}
    - Include the keyword in the title, intro, and 3+ times throughout the content.
    - Structure: Introduction, 2–3 sections with H2s, and a conclusion.
    - End the post with this call to action: {cta}
    - Length: ~1600–1800 words.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert SEO blog writer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error generating blog post: {str(e)}"

def suggest_blog_titles(keyword, audience):
    prompt = f"""
    You are an expert SEO strategist. Suggest 5 catchy, SEO-optimized blog post titles based on the keyword "{keyword}" for the audience: "{audience}".
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert SEO strategist."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        titles_raw = response.choices[0].message.content.strip().split("\n")
        return [t.lstrip("0123456789. ").strip("- ").strip() for t in titles_raw if t.strip()]
    except Exception as e:
        return [f"❌ Error generating titles: {str(e)}"]
