import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import pandas as pd
import altair as alt
# ────────────────────────────────────────────────────────────────────────────────
# Page configuration
# ────────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Ghassen Bennouri | Portfolio",
    page_icon="🚀",
    layout="wide",
)

# ────────────────────────────────────────────────────────────────────────────────
# Global color palette + component styles
# ────────────────────────────────────────────────────────────────────────────────
st.markdown(
    """
<style>
:root {
  --primary-color:#4CAF50;
  --secondary-color:#FFFFFF;
  --background-color:#F4F4F4;
  --text-color:#333333;
  --accent-blue:#0072ff;
}
html,body,[class*="css"]{font-family:Arial,Helvetica,sans-serif;background:var(--background-color);color:var(--text-color);} 
/* Card container */
.card{background:var(--secondary-color);border-left:6px solid var(--primary-color);padding:1.25rem 1.5rem;margin:1rem 0;border-radius:10px;box-shadow:0 2px 8px rgba(0,0,0,.08);} 
.card-title{font-weight:700;font-size:1.1rem;margin-bottom:.25rem;} 
.card-date{font-size:.9rem;color:var(--primary-color);margin-bottom:1rem;} 
/* Animated progress bar */
.progress-container{width:100%;background:rgba(0,0,0,.1);border-radius:8px;overflow:hidden;height:16px;margin-bottom:.75rem;}
.progress-bar{height:100%;background:linear-gradient(90deg,#00c6ff,var(--accent-blue));animation:grow 1.5s ease-out forwards;}
@keyframes grow{from{width:0}to{width:var(--value)}}
</style>
""",
    unsafe_allow_html=True,
)

# Fade‑in for .animated-section blocks
components.html(
    """
<script>
window.addEventListener('DOMContentLoaded',()=>{
  document.querySelectorAll('.animated-section').forEach(el=>{el.style.opacity=0;setTimeout(()=>{el.style.transition='opacity .8s';el.style.opacity=1;},100);});
});
</script>
""",
    height=0,
)

# ────────────────────────────────────────────────────────────────────────────────
# Sidebar navigation
# ────────────────────────────────────────────────────────────────────────────────
st.sidebar.title("🚀 Navigate")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home","🎓 Education","💼 Experience","📂 Projects","💡 Skills & 🌍 Languages","🏆 Extracurricular"],
)

# ────────────────────────────────────────────────────────────────────────────────
# Home
# ────────────────────────────────────────────────────────────────────────────────
if page == "🏠 Home":
    st.markdown('<div class="animated-section"><h1>Mohamed Ghassen Bennouri</h1></div>',unsafe_allow_html=True)
    if Path("profile.jpg").exists():
        st.image("profile.jpg",width=150)
    st.markdown('<div class="animated-section"><h3>👨‍💻 Software Developer | Digital Systems Enthusiast</h3></div>',unsafe_allow_html=True)
    st.write("📍  Ariana, Tunisia | 📞 +216 55341712 | ✉️ bennourigh@gmail.com")
    st.write("Born 21 Jun 2000 | Tunisian")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/ghassen-bennouri-1a35b3252/)")
    st.subheader("Profile")
    st.write(
        """Passionate about software architecture and information‑systems management, I couple strong training in Business Information Systems with hands‑on skills in full‑stack development, solution integration and production operations. Combining technical depth with a keen understanding of business processes and system administration, I stay relentlessly curious — particularly about fintech trends and the evolving WEB2 / WEB3 ecosystems."""
    )

# ────────────────────────────────────────────────────────────────────────────────
# Education
# ────────────────────────────────────────────────────────────────────────────────
elif page == "🎓 Education":
    st.header("🎓 Academic Path")
    edu = [
        ("Sep 2024 — Present","Masters in Digital Management & Information Systems","Esprit School of Business, Ariana"),
        ("Sep 2021 — Jun 2024","License in Business computing -> Information Systems","Esprit School of Business, Ariana"),
        ("Sep 2020 — Jun 2021","License in Embedded Systems & IoT","Faculty of Sciences of Bizerte"),
        ("Sep 2019 — Jun 2020","Baccalaureate in Mathematics","Lycée Tunis, Ariana"),
    ]
    for d,title,loc in edu:
        st.markdown(f"<div class='card'><div class='card-title'>{title}</div><div class='card-date'>📅 {d}</div><div>{loc}</div></div>",unsafe_allow_html=True)
    st.subheader("📜 Certificates & Courses")
    st.write("IBM Full‑Stack Software Developer Professional Certificate • IS/IT Governance (Coursera)")

# ────────────────────────────────────────────────────────────────────────────────
# Experience & Internships
# ────────────────────────────────────────────────────────────────────────────────
elif page == "💼 Experience":
    st.header("🚀 Freelance Experiences")
    roles = [
        ("🚀 Freelance Full‑Stack Developer — Djinston","Jan 2024 — Present",
         "Led React / Laravel / Python micro‑services MVP; built real‑time APIs and data pipelines."),
        ("🛠️ Freelance Backend Engineer — Nest.js (Freelance)","Jul 2023 — Dec 2023",
         "Developed GraphQL & REST services with 95 % test coverage using Jest & SuperTest."),
    ]
    for title,dates,desc in roles:
        st.markdown(f"<div class='card'><div class='card-title'>{title}</div><div class='card-date'>📅 {dates}</div><div>{desc}</div></div>",unsafe_allow_html=True)

    st.subheader("📚 Internships & Major Projects")
    internships = [
        ("🛠️ Software Development Project — Cardio‑Life","Mar 2024 — Jul 2024",
         """<ul>
            <li>Built a modular health‑equipment platform on <b>Java 17</b> & <b>Axon Framework</b> (CQRS + Event Sourcing).</li>
            <li>Developed <b>Angular 17</b> SPA synced via server‑sent events; gRPC for inter‑service comms.</li>
            <li>Infra stack: Spring Gateway, Consul, Keycloak OIDC, Stripe, Vault.</li>
         </ul>"""),
        ("🔄 Workflow Intern — Cardio‑Life","May 2022 — Aug 2022",
         """<ul>
            <li>Documented SOPs and streamlined equipment workflows for a med‑tech start‑up.</li>
            <li>Diagnosed device issues using diagnostic software; supported marketing‑policy analysis.</li>
         </ul>"""),
         ("🖥️ Web Integrator (WordPress) — Cardio‑Life","Aug 2024 — Oct 2024",
         """<ul>
            <li>Designed, developed and maintained a WordPress site with custom themes & plugins.</li>
            <li>Implemented an inbound‑marketing strategy and on‑page SEO; +65 % organic traffic.</li>
            <li>Optimised performance (caching, image compression) reaching PageSpeed ≥ 90.</li>
         </ul>""")
    ]
    for title,dates,desc in internships:
        st.markdown(f"<div class='card'><div class='card-title'>{title}</div><div class='card-date'>📅 {dates}</div><div>{desc}</div></div>",unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────────────────────────
# Projects — Highlight remains unchanged (details already covered above)
# ────────────────────────────────────────────────────────────────────────────────
elif page == "📂 Projects":
    st.header("📊 Highlight Project")
    st.markdown(
        """
<div class='card'>
  <div class='card-title'>🛠️ Modular Health Equipment Platform — Cardio‑Life</div>
  <div class='card-date'>📅 Mar 2024 — Jul 2024</div>
  <ul>
    <li><b>Axon Framework</b> (CQRS + Event Sourcing) on <b>Java 17</b> Spring Micro‑services.</li>
    <li>Frontend <b>Angular 17</b> with live state sync.</li>
    <li>Infra: Axon Server (gRPC), Spring Gateway, Consul, Keycloak OIDC, Stripe, Vault.</li>
  </ul>
</div>
""",
        unsafe_allow_html=True,
    )

# ────────────────────────────────────────────────────────────────────────────────
# Skills & Languages
# ────────────────────────────────────────────────────────────────────────────────
elif page == "💡 Skills & 🌍 Languages":
    

    st.header("💡 Core Technical Skills")

    skills = {
        "⚡ TypeScript (Nest.js, Next.js, Angular)": 80,
        "☕ Java (Spring Framework)":               70,
        "🐘 PHP (Laravel, WordPress)":              80,
        "🤖 Python (ML, Data integration, Talend)": 75,
        "📊 Power BI / Data Viz":                  70,
        "🗄️ Databases (PostgreSQL, MongoDB, AxonIQ)": 85,
        "🐳 Docker / CI-CD (GitHub Actions)":       75,
        "🔎 SEO / AEO & Web Analytics":            100,
    }

    # ── 1. Grid of native progress bars ────────────────────────────────────────
    cols = st.columns(2)
    for i, (skill, pct) in enumerate(skills.items()):
        level = (
            "Expert"       if pct >= 90 else
            "Advanced"     if pct >= 80 else
            "Proficient"   if pct >= 70 else
            "Intermediate"
        )
        with cols[i % 2]:
            st.markdown(f"**{skill}**")
            st.progress(pct)
            st.caption(f"{level} · {pct}%")

    # ── 2. Optional “bird’s-eye” bar chart (Altair) ────────────────────────────
    st.divider()
    df = pd.DataFrame({"Skill": list(skills.keys()), "Proficiency": list(skills.values())})
    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X("Proficiency:Q", title="Proficiency (%)", scale=alt.Scale(domain=[0, 100])),
            y=alt.Y("Skill:N", sort="-x", title=None),
            tooltip=["Skill", "Proficiency"]
        )
        .properties(height=300)
    )
    st.altair_chart(chart, use_container_width=True)

    # ── 3. Languages with st.metric ────────────────────────────────────────────
    st.subheader("🌍 Languages")
    langs = {
        "🇺🇸 English": "Highly proficient",
        "🇫🇷 French":  "Highly proficient",
        "🇹🇳 Arabic":  "Native",
    }
    lang_cols = st.columns(len(langs))
    for col, (lang, lvl) in zip(lang_cols, langs.items()):
        col.metric(label=lang, value=lvl)
# ────────────────────────────────────────────────────────────────────────────────
# Extracurricular
# ────────────────────────────────────────────────────────────────────────────────
elif page == "🏆 Extracurricular":
    st.header("🏆 Extracurricular & Volunteer Work")
    clubs=[
        ("🎭 Rotaract Club Amilcar Sidi Bou Said — Founding Member","Sep 2021 — Jun 2023"),
        ("🎖️ Interact Club Amilcar Sidi Bou Said — Treasurer & Team Lead","Sep 2016 — Jun 2019"),
        ("🩺 Basic‑Life‑Support Intervenant — European Resuscitation Council","Jun 2021 — Present"),
    ]
    for title,dates in clubs:
        st.markdown(f"<div class='card'><div class='card-title'>{title}</div><div class='card-date'>📅 {dates}</div></div>",unsafe_allow_html=True)
