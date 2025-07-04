import streamlit as st
from openai import OpenAI, OpenAIError

# Use the new client-based SDK
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_content_ideas(business_type, keyword):
    prompt = f"Suggest 5 SEO blog post ideas for a {business_type} targeting the keyword: {keyword}"
    return chat_with_openai(prompt)

def write_blog_post(title, keyword):
    prompt = (
        f"Write a 1500-word blog post titled '{title}' optimized for SEO using the keyword '{keyword}'. "
        f"Include headings and subheadings, and end with a call to action."
    )
    return chat_with_openai(prompt)

def chat_with_openai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except OpenAIError as e:
        return f"❌ OpenAI API Error: {str(e)}"
