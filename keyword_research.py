import openai
import streamlit as st

def suggest_keywords(topic):
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    prompt = f"""
    You are an expert SEO strategist. Given the topic: "{topic}", provide:

    1. A list of 8–10 high-value SEO keywords (short- and long-tail).
    2. Group those into 2–3 keyword clusters with clear labels.
    3. Suggest 1 blog topic per cluster, formatted like:
       - Blog Title (based on: keyword)

    Format your output in markdown like this:
    ## Keyword List
    - keyword 1
    - keyword 2
    ...

    ## Keyword Clusters
    ### Cluster Name 1
    - keyword a
    - keyword b

    ### Cluster Name 2
    ...

    ## Blog Topic Suggestions
    - Blog Title A (based on: keyword a)
    - Blog Title B (based on: keyword x)
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
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Error generating keyword suggestions: {str(e)}"
