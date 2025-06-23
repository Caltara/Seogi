from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def suggest_keywords(topic):
    prompt = f"""
    You are an expert SEO strategist. Given the topic: "{topic}", provide:

    1. A list of 8–10 high-value SEO keywords (short- and long-tail).
    2. Group those into 2–3 keyword clusters with clear labels.
    3. Suggest 1 blog topic per cluster, formatted like:
       - Blog Title (based on: keyword)
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an SEO keyword research expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error generating keyword suggestions: {str(e)}"
