import openai
import os
import streamlit as st

def write_blog_post(title, keyword):
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    prompt = f"""
    Write a high-quality, SEO-optimized blog post about "{title}" targeting the keyword "{keyword}".
    
    Guidelines:
    - Use the keyword in the title, introduction, and at least 3 times throughout the post.
    - Include an introduction, 2–3 informative sections with H2 headings, and a conclusion.
    - Write in a helpful, professional tone.
    - Use short paragraphs, bullet points if helpful, and include a call to action at the end.
    - Total length should be about 1400–1800 words.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert SEO content writer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error generating blog post: {str(e)}"
