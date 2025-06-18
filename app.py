import streamlit as st
from seo_audit import audit_seo
from content_generator import generate_content_ideas, write_blog_post

st.set_page_config(page_title="SEO AI Agent", layout="wide")
st.title("🔍 SEO AI Agent")

menu = st.sidebar.radio("Choose an option", ["Audit Website", "Generate Blog Post"])

if menu == "Audit Website":
    url = st.text_input("Enter Website URL")
    if st.button("Run Audit") and url:
        result = audit_seo(url)
        if "error" in result:
            st.error(result["error"])
        else:
            st.json(result)

elif menu == "Generate Blog Post":
    business = st.text_input("Business Type (e.g., dentist, roofer)")
    keyword = st.text_input("Target SEO Keyword")
    if st.button("Suggest Blog Ideas") and business and keyword:
        ideas = generate_content_ideas(business, keyword)
        st.write(ideas)

    title = st.text_input("Blog Post Title")
    if st.button("Generate Blog Post") and title and keyword:
        blog = write_blog_post(title, keyword)
        st.markdown(blog)
