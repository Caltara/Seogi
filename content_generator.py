import streamlit as st
openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_content_ideas(business_type, keyword):
    prompt = f"Suggest 5 SEO blog post ideas for a {business_type} targeting the keyword: {keyword}"
    return chat_with_openai(prompt)

def write_blog_post(title, keyword):
    prompt = (
        f"Write a 600-word blog post titled '{title}' optimized for SEO using the keyword '{keyword}'. "
        f"Include headings and subheadings, and end with a call to action."
    )
    return chat_with_openai(prompt)

def chat_with_openai(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content
