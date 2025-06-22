import openai
import streamlit as st

def suggest_keywords(topic):
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    prompt = f"""
    You are an expert SEO strategist. Given the topic: "{topic}", provide:
    
    1. A list of 8–10 high-value SEO keywords (including short- and long-tail keywords).
    2. Group those keywords into 2–3 keyword clusters by topic relevance.
    3. Suggest 1 blog topic idea for each cluster that would perform well in search engines.
    
    Format:
    - Keyword List
    - Keyword Clusters
    - Blog Topic Suggestions
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an SEO keyword expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error generating keywords: {str(e)}"
