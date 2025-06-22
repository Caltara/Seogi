import streamlit as st
from seo_audit import audit_seo
from blog_writer import write_blog_post, suggest_blog_titles
from keyword_research import suggest_keywords
from page_optimizer import optimize_page
from backlink_monitor import check_backlinks
from structure_optimizer import analyze_structure

# App setup
st.set_page_config(page_title="Seogi - Your SEO AI Mastermind", layout="wide")
st.title("🔮 Seogi - Your SEO AI Mastermind")

# Sidebar menu
st.sidebar.title("🧠 Seogi Menu")
menu = st.sidebar.radio("Choose a feature:", [
    "SEO Audit",
    "Write SEO Blog Post",
    "Keyword Research",
    "Page Optimization",
    "Backlink Monitoring",
    "Site Structure Optimization"
])

# If redirected from keyword research, handle prefilled values
if "menu" in st.session_state:
    menu = st.session_state["menu"]
    del st.session_state["menu"]

# -------------------------------
# SEO AUDIT
# -------------------------------
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

# -------------------------------
# BLOG WRITER
# -------------------------------
elif menu == "Write SEO Blog Post":
    st.header("✍️ Write an SEO Blog Post")

    keyword = st.text_input("Target Keyword", value=st.session_state.get("selected_keyword", ""))
    audience = st.text_input("Who is your audience?", value="")

    if st.button("Suggest Blog Titles") and keyword and audience:
        titles = suggest_blog_titles(keyword, audience)
        st.session_state["suggested_titles"] = titles

    if "suggested_titles" in st.session_state:
        default_title = st.session_state.get("selected_title", st.session_state["suggested_titles"][0])
        title = st.selectbox(
            "Choose a Blog Post Title",
            st.session_state["suggested_titles"],
            index=st.session_state["suggested_titles"].index(default_title)
            if default_title in st.session_state["suggested_titles"] else 0
        )
        st.markdown(f"🔎 Seogi's suggestion: **{title}**")
    else:
        title = st.text_input("Or write your own blog post title", value=st.session_state.get("selected_title", ""))

    tone = st.selectbox("Tone of Voice", ["Professional", "Friendly", "Persuasive", "Casual", "Educational"])
    cta = st.text_input("Call to Action (e.g., Schedule a consultation, Sign up for our newsletter)")

    if st.button("Generate Blog Post"):
        if title and keyword and audience and tone and cta:
            blog = write_blog_post(title, keyword, audience, tone, cta)
            st.markdown(blog)
        else:
            st.warning("Please fill in all fields to generate a blog post.")

# -------------------------------
# KEYWORD RESEARCH
# -------------------------------
elif menu == "Keyword Research":
    st.header("🔑 Keyword Research")

    topic = st.text_input("Enter your business or niche")

    if st.button("Suggest Keywords") and topic:
        result = suggest_keywords(topic)
        st.session_state["last_keyword_research"] = result
        st.session_state["topic"] = topic

    if "last_keyword_research" in st.session_state:
        st.markdown("### 🔍 Seogi's Suggestions")
        st.markdown(st.session_state["last_keyword_research"])

        # Blog topic suggestions with button
        suggestions = []
        for line in st.session_state["last_keyword_research"].splitlines():
            if line.strip().startswith("- ") and "(based on:" in line:
                text = line.strip().lstrip("- ").strip()
                if "(based on:" in text:
                    title, keyword_part = text.split("(based on:")
                    keyword = keyword_part.replace(")", "").strip()
                    suggestions.append((title.strip(), keyword))

        st.markdown("---")
        st.subheader("✨ One-Click Blog Post Creation")

        for title, keyword in suggestions:
            if st.button(f"Write: {title}"):
                st.session_state["menu"] = "Write SEO Blog Post"
                st.session_state["selected_title"] = title
                st.session_state["selected_keyword"] = keyword
                st.experimental_rerun()

# -------------------------------
# PAGE OPTIMIZATION
# -------------------------------
elif menu == "Page Optimization":
    st.header("🧠 Page Optimization")
    raw_html = st.text_area("Paste your web page's raw HTML or content")
    keyword = st.text_input("Main keyword for this page")

    if st.button("Optimize Page") and raw_html and keyword:
        suggestions = optimize_page(raw_html, keyword)
        st.subheader("Optimization Suggestions")
        st.markdown(suggestions)

# -------------------------------
# BACKLINK MONITORING
# -------------------------------
elif menu == "Backlink Monitoring":
    st.header("🔗 Backlink Monitoring")
    domain = st.text_input("Enter your domain (e.g. example.com)")

    if st.button("Check Backlinks") and domain:
        backlinks = check_backlinks(domain)
        st.subheader("Backlink Profile")
        st.markdown(backlinks)

# -------------------------------
# SITE STRUCTURE OPTIMIZATION
# -------------------------------
elif menu == "Site Structure Optimization":
    st.header("🏗️ Site Structure Optimization")
    sitemap_url = st.text_input("Enter your sitemap URL (e.g. https://example.com/sitemap.xml)")

    if st.button("Analyze Structure") and sitemap_url:
        structure = analyze_structure(sitemap_url)
        if isinstance(structure, dict) and "error" in structure:
            st.error(structure["error"])
        else:
            st.subheader("Site Structure Recommendations")
            st.markdown(structure)
