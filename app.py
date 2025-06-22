import streamlit as st
from blog_writer import write_blog_post, suggest_blog_titles
from keyword_research import suggest_keywords
from page_optimizer import optimize_page
from backlink_monitor import check_backlinks
from structure_optimizer import analyze_structure
from seo_audit import audit_seo  # assuming you have this module updated similarly

st.set_page_config(page_title="Seogi SEO Mastermind", layout="wide")

st.title("🚀 Seogi — Your SEO Mastermind Agent")

menu = [
    "SEO Audit",
    "Keyword Research",
    "Blog Writing",
    "Page Optimization",
    "Backlink Monitoring",
    "Site Structure Analysis",
]

choice = st.sidebar.selectbox("Select Feature", menu)

if choice == "SEO Audit":
    st.header("SEO Audit")
    url = st.text_input("Enter website URL to audit (include http/https)")
    if st.button("Run Audit"):
        if url:
            with st.spinner("Auditing..."):
                result = audit_seo(url)
            st.markdown("### Audit Results")
            st.write(result)
        else:
            st.error("Please enter a valid URL")

elif choice == "Keyword Research":
    st.header("Keyword Research")
    topic = st.text_input("Enter your topic or niche")
    if st.button("Get Keyword Suggestions"):
        if topic:
            with st.spinner("Generating keywords..."):
                keywords = suggest_keywords(topic)
            st.markdown("### Keyword Clusters and Suggestions")
            st.write(keywords)
        else:
            st.error("Please enter a topic")

elif choice == "Blog Writing":
    st.header("SEO Blog Writer")
    keyword = st.text_input("Primary keyword")
    audience = st.text_input("Target audience")
    tone = st.selectbox("Tone", ["Professional", "Casual", "Friendly", "Formal", "Conversational"])
    cta = st.text_input("Call to Action (e.g., Contact us today!)")

    st.markdown("**Generate Blog Title Ideas**")
    if st.button("Get Blog Titles"):
        if keyword and audience:
            with st.spinner("Generating blog titles..."):
                titles = suggest_blog_titles(keyword, audience)
            for i, t in enumerate(titles, 1):
                st.write(f"{i}. {t}")
        else:
            st.error("Please enter keyword and audience")

    st.markdown("---")
    st.markdown("**Write Full Blog Post**")
    blog_title = st.text_input("Blog Post Title")
    if st.button("Write Blog Post"):
        if blog_title and keyword and audience and tone and cta:
            with st.spinner("Writing blog post..."):
                post = write_blog_post(blog_title, keyword, audience, tone, cta)
            st.markdown("### Generated Blog Post")
            st.write(post)
        else:
            st.error("Please fill in all fields above")

elif choice == "Page Optimization":
    st.header("Page Optimization")
    raw_html = st.text_area("Paste raw HTML content of the page")
    target_keyword = st.text_input("Target keyword for optimization")
    if st.button("Optimize Page"):
        if raw_html and target_keyword:
            with st.spinner("Optimizing page..."):
                suggestions = optimize_page(raw_html, target_keyword)
            st.markdown("### Optimization Suggestions")
            st.write(suggestions)
        else:
            st.error("Please provide page HTML and target keyword")

elif choice == "Backlink Monitoring":
    st.header("Backlink Monitoring")
    domain = st.text_input("Enter your domain (e.g., example.com)")
    if st.button("Analyze Backlinks"):
        if domain:
            with st.spinner("Analyzing backlinks..."):
                report = check_backlinks(domain)
            st.markdown("### Backlink Analysis Report")
            st.write(report)
        else:
            st.error("Please enter a domain")

elif choice == "Site Structure Analysis":
    st.header("Site Structure Analysis")
    sitemap_url = st.text_input("Enter sitemap URL (e.g., https://example.com/sitemap.xml)")
    if st.button("Analyze Structure"):
        if sitemap_url:
            with st.spinner("Analyzing site structure..."):
                structure_report = analyze_structure(sitemap_url)
            st.markdown("### Site Structure Report")
            st.write(structure_report)
        else:
            st.error("Please enter a sitemap URL")
