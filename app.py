import streamlit as st
from seo_audit import audit_seo
from blog_writer import write_blog_post, suggest_blog_titles
from keyword_research import suggest_keywords
from page_optimizer import optimize_page
from backlink_monitor import check_backlinks
from structure_optimizer import analyze_structure

st.set_page_config(page_title="Seogi - Your SEO AI Mastermind", layout="wide")
st.title("🔮 Seogi - Your SEO AI Mastermind")

st.sidebar.title("🧠 Seogi Menu")
menu = st.sidebar.radio("Choose a feature:", [
    "SEO Audit",
    "Write SEO Blog Post",
    "Keyword Research",
    "Page Optimization",
    "Backlink Monitoring",
    "Site Structure Optimization"
])

# --- SEO Audit ---
if menu == "SEO Audit":
    st.header("🔍 SEO Audit")
    url = st.text_input("Enter website URL (e.g. https://example.com)")
    if st.button("Run SEO Audit") and url:
        result = audit_seo(url)
        if "error" in result:
            st.error(result["error"])
        else:
            st.subheader("Audit Results")
            st.json(result)

# --- Blog Post Writer ---
elif menu == "Write SEO Blog Post":
    st.header("✍️ Write an SEO Blog Post")

    keyword = st.text_input("Target Keyword")
    audience = st.text_input("Who is your audience? (e.g., small business owners, real estate agents)")

    if st.button("Suggest Blog Titles") and keyword and audience:
        titles = suggest_blog_titles(keyword, audience)
        st.session_state["suggested_titles"] = titles

    if "suggested_titles" in st.session_state:
        title = st.selectbox("Choose a Blog Post Title", st.session_state["suggested_titles"])
        st.markdown(f"🔎 Seogi's suggestion: **{title}**")
    else:
        title = st.text_input("Or write your own blog post title")

    tone = st.selectbox("Tone of Voice", ["Professional", "Friendly", "Persuasive", "Casual", "Educational"])
    cta = st.text_input("Call to Action (e.g., Schedule a consultation, Sign up for our newsletter)")

    if st.button("Generate Blog Post"):
        if title and keyword and audience and tone and cta:
            blog = write_blog_post(title, keyword, audience, tone, cta)
            st.markdown(blog)
        else:
            st.warning("Please fill in all fields to generate a blog post.")

# --- Keyword Research ---
elif menu == "Keyword Research":
    st.header("🔑 Keyword Research")
    topic = st.text_input("Enter your business or niche")
    if st.button("Suggest Keywords") and topic:
        keywords = suggest_keywords(topic)
        st.subheader("Suggested Keywords:")
        st.write(keywords)

# --- Page Optimization ---
elif menu == "Page Optimization":
    st.header("🧠 Page Optimization")
    raw_html = st.text_area("Paste your web page HTML or content")
    keyword = st.text_input("Main keyword for this page")
    if st.button("Optimize Page") and raw_html and keyword:
        suggestions = optimize_page(raw_html, keyword)
        st.subheader("Optimization Suggestions")
        st.write(suggestions)

# --- Backlink Monitoring ---
elif menu == "Backlink Monitoring":
    st.header("🔗 Backlink Monitoring")
    domain = st.text_input("Enter your domain (e.g. example.com)")
    if st.button("Check Backlinks") and domain:
        backlinks = check_backlinks(domain)
        st.subheader("Backlink Profile")
        st.json(backlinks)

# --- Site Structure Optimization ---
elif menu == "Site Structure Optimization":
    st.header("🏗️ Site Structure Optimization")
    sitemap_url = st.text_input("Enter your sitemap URL (e.g. https://example.com/sitemap.xml)")
    if st.button("Analyze Structure") and sitemap_url:
        structure = analyze_structure(sitemap_url)
        st.subheader("Site Structure Recommendations")
        st.write(structure)
