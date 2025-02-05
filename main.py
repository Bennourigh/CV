import streamlit as st
import streamlit.components.v1 as components

# Load Framer Motion Animations
components.html("""
    <script>
    function fadeInEffect() {
        var elements = document.querySelectorAll('.animated-section');
        elements.forEach(el => {
            el.style.opacity = 0;
            setTimeout(() => {
                el.style.transition = "opacity 0.8s ease-in-out";
                el.style.opacity = 1;
            }, 100);
        });
    }
    fadeInEffect();
    </script>
""", height=0)

# Sidebar Navigation
st.sidebar.title("🚀 Navigation")
page = st.sidebar.radio("Go to",
                        ["🏠 Home", "💼 Experience", "📂 Projects", "💡 Skills & 🌍 Languages", "🏆 Extracurricular"])

# Home Section
if page == "🏠 Home":
    st.markdown('<div class="animated-section"><h1>Mohamed Ghassen Bennouri</h1></div>', unsafe_allow_html=True)
    st.image("profile.jpg", width=150)
    st.markdown('<div class="animated-section"><h3>👨‍💻 Junior Software Developer</h3></div>', unsafe_allow_html=True)
    st.write("📍 Sokra, Ariana, Tunisia | 📞 +216 55341712 | ✉️ bennourigh@gmail.com")
    st.markdown(
        "[🔗 LinkedIn](https://www.linkedin.com/in/ghassen-bennouri-1a35b3252/) | [🔗 Facebook](https://www.facebook.com/ghbennouri/)")

    st.subheader("💼 Profile")
    st.write("""
    - 🚀 Motivated junior developer with a strong foundation in software development and an academic background in Business Information Systems & Digital Management.
    - 💡 Combining technical expertise with a deep understanding of business processes.
    - 🔥 Passionate about learning and staying updated with the latest trends in finance technologies and the WEB2/WEB3 ecosystem.
    """)

# Experience Section
elif page == "💼 Experience":
    st.header("🧑‍💼 Work Experience")
    st.subheader("🖥️ Web Integrator (WordPress) - Cardio-Life, Ariana")
    st.write("📅 Aug 2024 — Oct 2024")
    st.write("""
    - 🎨 Designed, developed, and maintained a WordPress website for a small business.
    - 📈 Conducted keyword research and optimized SEO, increasing organic traffic by 35%.
    - 🔍 Used Google Analytics, Google Search Console, and Yoast SEO for performance tracking.
    - ⚡ Improved website speed, achieving a Google PageSpeed score of 90+.
    """)

# Projects Section
elif page == "📂 Projects":
    st.header("📊 Projects")
    st.subheader("🛠️ Software Development Project - Cardio-Life")
    st.write("📅 Mar 2024 — Jul 2024")
    st.write("""
    - ⚙️ Developed using Axon Framework, CQRS, and Event Sourcing for scalability and performance.
    - 🎨 Built front-end with Angular 17.
    - 🔄 Implemented asynchronous messaging using Axon Server, gRPC, and a REST API.
    - 🔐 Integrated HashiCorp Consul, Keycloak (OIDC), Stripe API, and HashiCorp Vault.
    """)

# Skills & Languages Section
elif page == "💡 Skills & 🌍 Languages":
    st.header("💡 Skills & 🌍 Languages Overview")

    skill_levels = {
        "⚡ TypeScript (Nest.js, Next.js, Angular)": 90,
        "☕ Java (Spring Boot)": 80,
        "🐘 PHP (Laravel, WordPress)": 85,
        "🤖 Machine Learning / Data Integration (Python, Power BI, Talend)": 75,
        "🗄️ Databases (PostgreSQL, MongoDB, Axon, EdgeDB)": 85,
        "🚀 CI/CD (GitHub, GitHub Actions)": 80,
        "🔎 SEO/AEO Optimization": 88
    }

    for skill, level in skill_levels.items():
        st.markdown(f"<h4>{skill}</h4>", unsafe_allow_html=True)
        components.html(f"""
        <div class="animated-section">
        <div style="width: {level}%; height: 15px; background: linear-gradient(90deg, #ff8a00, #e52e71); border-radius: 10px;"></div>
        </div>
        """, height=20)

    st.subheader("🌍 Languages")
    languages = {
        "🇺🇸 English": "Native Speaker",
        "🇫🇷 French": "Highly Proficient",
        "🇹🇳 Arabic": "Native Speaker"
    }

    for lang, level in languages.items():
        st.write(f"**{lang}:** {level}")

# Extracurricular Activities
elif page == "🏆 Extracurricular":
    st.header("🏆 Extracurricular Activities")

    st.subheader("🎭 Rotaract Club Amilcar Sidi Bou Said")
    st.write("📅 Sep 2021 — Jun 2023 (Founding Member)")
    st.markdown("[📷 Instagram](https://www.instagram.com/tuniact_sidi_bou_said/)")

    st.subheader("🎖️ Interact Club Amilcar Sidi Bou Said")
    st.write("📅 Sep 2016 — Jun 2019 (Treasurer, Chief of Protocol & Sponsoring Team Chief)")
    st.markdown("[📷 Instagram](https://www.instagram.com/interactclubamilcarsidibou/)")

    st.subheader("🩺 Basic-Life-Support Intervenant - European Resuscitation Council")
    st.write("📅 Jun 2021 — Present")
