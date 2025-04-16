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
st.sidebar.title("🚀 Navigate")
page = st.sidebar.radio("Go to",
    ["🏠 Home", "💼 Experience", "📂 Projects", "💡 Skills & 🌍 Languages", "🏆 Extracurricular"])

# Home Section
if page == "🏠 Home":
    st.markdown('<div class="animated-section"><h1>Mohamed Ghassen Bennouri</h1></div>', unsafe_allow_html=True)
    st.image("profile.jpg", width=150)
    st.markdown('<div class="animated-section"><h3>👨‍💻 Junior Software Developer | Digital Systems Enthusiast</h3></div>', unsafe_allow_html=True)
    st.write("📍 Sokra, Ariana, Tunisia | 📞 +216 55341712 | ✉️ bennourigh@gmail.com")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/ghassen-bennouri-1a35b3252/) | [🔗 Facebook](https://www.facebook.com/ghbennouri/)")
    st.subheader("💼 About Me")
    st.write("""
    Life taught me early on that purpose must be earned, not given. From working summer jobs in hospitality to crafting scalable digital systems, 
    my journey is defined by resilience, reinvention, and relentless curiosity.

    With a foundation in Business Information Systems and a deepening mastery of backend architectures, I specialize in building systems that aren’t 
    just functional — they’re thoughtful. Whether I'm working with **CQRS, event sourcing, microservices**, or exploring how **Web3** reshapes trust, 
    I approach tech as a craft with purpose.

    I’ve faced doubt, and distraction — yet each became a stepping stone. These challenges didn’t break me; they sharpened me.

    Today, I aim to build tech with soul — tools that empower, solutions that scale, and systems that leave a mark. I learn fast, think deeply, 
    and adapt quicker than most. And while others may envy the path, I choose to walk it anyway.

    **If you're building for meaning — not just markets — let’s talk.**
    """)

# Experience Section
elif page == "💼 Experience":
    st.header("🧑‍💼 Work Experience")
    
    st.subheader("🖥️ Web Integrator (WordPress) – Cardio-Life, Ariana")
    st.write("📅 Aug 2024 — Oct 2024")
    st.write("""
    - Designed and deployed a complete WordPress solution tailored to healthcare services.
    - Customized plugins and themes for performance, usability, and accessibility.
    - Led SEO improvements through on-page optimization and keyword targeting, boosting traffic by 35%.
    - Integrated Google Analytics, Search Console, and performance tuning tools for actionable insights.
    - Achieved Google PageSpeed Insight scores of 90+ via caching and image optimization.
    """)

# Projects Section
elif page == "📂 Projects":
    st.header("📊 Projects")

    st.subheader("🛠️ Software Development Project – Cardio-Life")
    st.write("📅 Mar 2024 — Jul 2024")
    st.write("""
    - Designed a modular system using **Axon Framework** with CQRS and Event Sourcing for maximum scalability.
    - Built and deployed an Angular 17 frontend with real-time state synchronization.
    - Integrated **Axon Server**, gRPC, and RESTful APIs for hybrid communication architecture.
    - Implemented secure authentication and authorization with **Keycloak** and OpenID Connect.
    - Incorporated **Stripe API** for payment automation and **HashiCorp Vault/Consul** for service secrets and discovery.
    - Delivered a robust, asynchronous and auditable microservices-ready architecture.
    """)

# Skills & Languages Section
elif page == "💡 Skills & 🌍 Languages":
    st.header("💡 Technical Skills")

    skill_levels = {
        "⚡ TypeScript (Nest.js, Next.js, Angular)": 90,
        "☕ Java (Spring Boot)": 80,
        "🐘 PHP (Laravel, WordPress)": 85,
        "🤖 ML / Data Integration (Python, Power BI, Talend)": 75,
        "🗄️ Databases (PostgreSQL, MongoDB, Axon, EdgeDB)": 85,
        "🚀 CI/CD & DevOps (GitHub Actions, Secure Secrets)": 80,
        "🔎 SEO / AEO & Web Analytics Tools": 88
    }

    for skill, level in skill_levels.items():
        st.markdown(f"<h4>{skill}</h4>", unsafe_allow_html=True)
        components.html(f"""
        <div class="animated-section">
        <div style="width: {level}%; height: 15px; background: linear-gradient(90deg, #00c6ff, #0072ff); border-radius: 10px;"></div>
        </div>
        """, height=20)

    st.subheader("🌍 Languages")
    languages = {
        "🇺🇸 English": "Highly Proficient",
        "🇫🇷 French": "Highly Proficient",
        "🇹🇳 Arabic": "Native Speaker"
    }

    for lang, level in languages.items():
        st.write(f"**{lang}:** {level}")

# Extracurricular Activities
elif page == "🏆 Extracurricular":
    st.header("🏆 Extracurricular & Volunteer Involvement")

    st.subheader("🎭 Rotaract Club Amilcar Sidi Bou Said")
    st.write("📅 Sep 2021 — Jun 2023")
    st.write("📌 Founding Member – Led several local initiatives around community development and education.")
    st.markdown("[📷 Instagram](https://www.instagram.com/tuniact_sidi_bou_said/)")

    st.subheader("🎖️ Interact Club Amilcar Sidi Bou Said")
    st.write("📅 Sep 2016 — Jun 2019")
    st.write("💼 Roles held: Treasurer, Chief of Protocol & Sponsorship Team Lead.")

    st.subheader("🩺 Basic-Life-Support Intervenant – European Resuscitation Council")
    st.write("📅 Jun 2021 — Present")
    st.write("Trained in emergency response and basic life-saving procedures.")
