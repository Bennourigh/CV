import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from pathlib import Path
import pandas as pd
import altair as alt

# ────────────────────────────────────────────────────────────────────────────────
# Page configuration
# ────────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MGB | Portfolio",
    page_icon="🏴‍☠️",
    layout="wide",
)

# --- SEO + Social meta injection & sitemap generation --------------------------------
def _inject_meta():
    base_url = "https://bennouri-ghassen.streamlit.app"  # change if different
    title = "Mohamed Ghassen Bennouri — Software Architect & Full‑Stack Developer"
    description = ("Software architect and full‑stack developer specialized in scalable web "
                   "and microservice architectures, event‑driven systems and digital product delivery.")
    image = f"{base_url}/profile.jpg"  # change if hosted elsewhere
    twitter_handle = "@your_twitter"  # optional: update or leave as placeholder
    canonical = base_url

    # JS that inserts meta tags into document.head (works in Streamlit)
    js = f"""
    <script>
    (function(){{
        try {{
            const head = document.head || document.getElementsByTagName('head')[0];

            function addMeta(tagName, attrs) {{
                var el = document.createElement(tagName);
                for (var k in attrs) el.setAttribute(k, attrs[k]);
                head.appendChild(el);
                return el;
            }}

            // Basic meta
            addMeta('meta', {{ name: 'description', content: '{description}' }});
            addMeta('link', {{ rel: 'canonical', href: '{canonical}' }});
            addMeta('meta', {{ name: 'robots', content: 'index,follow' }});

            // Open Graph
            addMeta('meta', {{ property: 'og:title', content: '{title}' }});
            addMeta('meta', {{ property: 'og:description', content: '{description}' }});
            addMeta('meta', {{ property: 'og:type', content: 'website' }});
            addMeta('meta', {{ property: 'og:url', content: '{canonical}' }});
            addMeta('meta', {{ property: 'og:image', content: '{image}' }});

            // Twitter Card
            addMeta('meta', {{ name: 'twitter:card', content: 'summary_large_image' }});
            addMeta('meta', {{ name: 'twitter:title', content: '{title}' }});
            addMeta('meta', {{ name: 'twitter:description', content: '{description}' }});
            addMeta('meta', {{ name: 'twitter:image', content: '{image}' }});
            addMeta('meta', {{ name: 'twitter:site', content: '{twitter_handle}' }});

            // Preconnect & preload for fonts and profile image
            addMeta('link', {{ rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }});
            addMeta('link', {{ rel: 'preload', href: '{image}', as: 'image' }});

            // JSON-LD Person schema
            var ld = document.createElement('script');
            ld.type = 'application/ld+json';
            ld.text = JSON.stringify({{
                "@context": "https://schema.org",
                "@type": "Person",
                "name": "Mohamed Ghassen Bennouri",
                "url": "{canonical}",
                "image": "{image}",
                "jobTitle": "Software Architect / Full‑Stack Developer",
                "description": "{description}",
                "sameAs": [
                    "https://www.linkedin.com/in/ghassen-bennouri-1a35b3252/"
                ]
            }});
            head.appendChild(ld);

        }} catch(e) {{ console.error('SEO injection error', e); }}
    }})();
    </script>
    """
    components.html(js, height=0)

def _write_sitemap(base_url="https://bennouri-ghassen.streamlit.app"):
    """
    Generate sitemap.xml in repo root (only sitemap; no robots.txt).
    Includes main page and common section anchors for better crawl hints.
    """
    try:
        urls = [
            base_url,
            f"{base_url}#home",
            f"{base_url}#education",
            f"{base_url}#experience",
            f"{base_url}#projects",
            f"{base_url}#skills",
            f"{base_url}#extracurricular",
        ]

        url_entries = "\n".join(
            f"""  <url>
    <loc>{u}</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""" for u in urls
        )

        sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{url_entries}
</urlset>"""

        Path("sitemap.xml").write_text(sitemap, encoding="utf-8")
    except Exception:
        # keep silent on failure to avoid breaking the app
        pass

# Run SEO helpers
_inject_meta()
_write_sitemap()

# ────────────────────────────────────────────────────────────────────────────────
# Global color palette + component styles with responsiveness
# ────────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

:root {
    --primary-color: #6366f1;          /* Indigo */
    --primary-light: #818cf8;          /* Light Indigo */
    --primary-dark: #4f46e5;           /* Dark Indigo */
    --secondary-color: #ffffff;         /* White */
    --background-color: #fafafa;       /* Light Gray */
    --text-color: #18181b;             /* Zinc-900 */
    --text-light: #71717a;             /* Zinc-500 */
    --surface-color: #ffffff;          /* White */
    --accent-color: #ec4899;           /* Pink-500 */
    --success-color: #10b981;          /* Emerald-500 */
    --warning-color: #f59e0b;          /* Amber-500 */
    --error-color: #ef4444;            /* Red-500 */
    --gradient-start: #6366f1;         /* Indigo-500 */
    --gradient-end: #8b5cf6;           /* Violet-500 */
    --card-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
    --hover-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
    --transition-speed: 0.3s;
}

/* Base styles */
body {
    font-family: 'Inter', sans-serif;
    background-color: var(--background-color);
    color: var(--text-color);
    line-height: 1.5;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    color: var(--text-color);
}

/* Card improvements */
.card {
    background: var(--surface-color);
    border-left: 4px solid var(--gradient-start);
    padding: 1.5rem;
    margin: 1.2rem 0;
    border-radius: 8px;
    box-shadow: var(--card-shadow);
    transition: all var(--transition-speed) ease;
}

.card:hover {
    transform: translateY(-2px);
    box-shadow: var(--hover-shadow);
}

.card-title {
    font-weight: 600;
    font-size: 1.1rem;
    color: var(--primary-dark);
    margin-bottom: 0.5rem;
}

/* Progress bars refinement */
.progress-bar-bg {
    background: #e2e8f0;
    height: 6px;
}

.progress-bar-fill {
    background: linear-gradient(90deg, var(--gradient-start), var(--gradient-end));
}

/* Skills section enhancement */
.skill-container {
    background: var(--surface-color);
    border: 1px solid #e2e8f0;
    padding: 1rem;
    border-radius: 8px;
    margin: 0.75rem 0;
}

.skill-name {
    color: var(--text-color);
    font-weight: 500;
}

.skill-level {
    color: var(--primary-color);
    font-weight: 500;
}

/* Language cards improvement */
.language-card {
    background: var(--surface-color);
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 1.5rem;
    transition: all var(--transition-speed) ease;
}

.language-card:hover {
    border-color: var(--primary-light);
}

.lang-level {
    color: var(--accent-color);
    background: color-mix(in srgb, var(--accent-color) 15%, transparent);
    padding: 0.25rem 0.75rem;
    border-radius: 16px;
    display: inline-block;
}

/* Dark mode refinements */
@media (prefers-color-scheme: dark) {
    :root {
        --background-color: #18181b;    /* Zinc-900 */
        --text-color: #fafafa;          /* Zinc-50 */
        --text-light: #a1a1aa;          /* Zinc-400 */
        --surface-color: #27272a;       /* Zinc-800 */
        --card-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.2);
        --hover-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.2);
    }
}

/* Tab navigation enhancement */
.streamlit-tabs button[role="tab"] {
    font-family: 'Inter', sans-serif;
    color: var(--text-color);
    border-color: #e2e8f0;
    background: transparent;
}

.streamlit-tabs button[role="tab"][aria-selected="true"] {
    background: linear-gradient(90deg, var(--gradient-start), var(--gradient-end));
    border-color: var(--gradient-start);
    color: white;
}

/* Profile section refinement */
.profile-section {
    background: var
    border-radius: 16px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: var(--card-shadow);
}

.profile-image {
    border: 3px solid var(--primary-color);
}

/* Center the main container */
div.block-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 1rem;
}

/* Optionally wrap content in a centered container if needed */
.centered-content {
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* Profile container styles */
.profile-container {
    max-width: 900px;
    margin: 0 auto;
    padding: 3rem 1.5rem;
}

.profile-header {
    text-align: center;
    margin-bottom: 3rem;
}

.profile-image {
    width: 180px;
    height: 180px;
    border-radius: 50%;
    border: 4px solid var(--primary-color);
    padding: 4px;
    margin: 2rem auto;
    display: block;
    object-fit: cover;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
}

.profile-image:hover {
    transform: scale(1.05);
}

.profile-title {
    font-size: 2.5rem;
    color: var(--text-color);
    margin-bottom: 1rem;
}

.profile-subtitle {
    font-size: 1.5rem;
    color: var(--primary-color);
    margin-bottom: 2rem;
}

.profile-contact {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    flex-wrap: wrap;
    margin-bottom: 2rem;
}

.contact-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--text-color);
}

.social-links {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 3rem;
}

.social-link {
    padding: 0.8rem 1.5rem;
    border-radius: 8px;
    background: var(--primary-color);
    color: white !important;
    text-decoration: none;
    transition: all 0.3s ease;
}

.social-link:hover {
    transform: translateY(-2px);
    background: var(--primary-dark);
}

.profile-content {
    max-width: 800px;
    margin: 0 auto;
    text-align: justify;
    line-height: 1.8;
    font-size: 1.1rem;
    color: var(--text-color);
}

@media (max-width: 768px) {
    .profile-container {
        padding: 2rem 1rem;
    }
    
    .profile-title {
        font-size: 2rem;
    }
    
    .profile-subtitle {
        font-size: 1.2rem;
    }
    
    .profile-contact {
        flex-direction: column;
        align-items: center;
        gap: 1rem;
    }
}
</style>
""", unsafe_allow_html=True,
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

components.html(
    """
<script>
// Intersection Observer for smooth animations
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, {
    threshold: 0.1
});

// Animate elements when they come into view
window.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.card, .skill-badge, .progress-container').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        observer.observe(el);
    });
});

// Smooth scroll behavior
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Add visible class for animation triggers
document.querySelectorAll('.animated-section').forEach(el => {
    el.classList.add('visible');
});
</script>
""",
    height=0,
)

# ────────────────────────────────────────────────────────────────────────────────
# Top navigation tabs (responsive & interactive)
# ────────────────────────────────────────────────────────────────────────────────
tab_home, tab_edu, tab_exp, tab_proj, tab_skills, tab_extrac = st.tabs([
    "🏠 Home",
    "🎓 Education",
    "💼 Experience",
    "📂 Projects",
    "💡 Skills & 🌍 Languages",
    "🏆 Extracurricular",
])

# ────────────────────────────────────────────────────────────────────────────────
# Home
# ────────────────────────────────────────────────────────────────────────────────
with tab_home:
    # Create a centered layout using Streamlit columns
    col1, col2, col3 = st.columns([1, 2, 1])  # Center the content
    with col2:
        # Display the profile image
        if Path("profile.jpg").exists():
            st.image("profile.jpg", caption="Mohamed Ghassen Bennouri", use_container_width=True)
        
        # Add the title and subtitle
        st.markdown("<h1 style='text-align: center;'>Mohamed Ghassen Bennouri</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: var(--primary-color);'>👨‍💻 Software Developer | Digital Systems Enthusiast</h3>", unsafe_allow_html=True)
        
        # Add contact information
        st.markdown("""
        <div style="text-align: center; margin-top: 1rem;">
            <p>📍 Ariana, Tunisia |  ✉️ new0mgb@gmail.com</p>
            <p>🎂 Born 21 Jun 2000 | 🏳️ Tunisian</p>
            <a href="https://www.linkedin.com/in/ghassen-bennouri-1a35b3252/" style="color: var(--primary-color); text-decoration: none;">🔗 LinkedIn</a>
        </div>
        """, unsafe_allow_html=True)
        
        # Add the professional profile section
        st.markdown("""
        <div style="text-align: justify; margin-top: 2rem; max-width: 800px; margin-left: auto; margin-right: auto;">
            <h2 style="text-align: center; margin-bottom: 1rem;">Professional Profile</h2>
            <p>
                I am a dedicated software architect with a strong foundation in Business Information Systems 
                and extensive hands‑on expertise in full‑stack development, solution integration, and production/Sales operations.
                My approach blends technical acumen with a deep understanding of business processes, enabling me to design and implement 
                scalable, efficient, and secure software solutions that drive operational excellence.
            </p>
            <p style="margin-top: 1rem;">
                With a passion for continuous learning, I keep pace with emerging trends in cloud architecture, 
                microservices, and event-driven systems. My goal is to deliver thought‑provoking innovations 
                that not only solve today's challenges but anticipate tomorrow's needs in the ever-evolving 
                landscape of digital transformation.
            </p>
        </div>
        """, unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────────────────────────
# Education
# ────────────────────────────────────────────────────────────────────────────────
with tab_edu:
    st.markdown('<div class="centered-content">', unsafe_allow_html=True)
    st.header("🎓 Academic Path")
    edu = [
        ("Sep 2024 — Jun 2025", "Masters in Digital Management & Information Systems", "Esprit School of Business, Ariana"),
        ("Sep 2021 — Jun 2024", "License in Business computing -> Information Systems", "Esprit School of Business, Ariana"),
        ("Sep 2020 — Jun 2021", "License in Embedded Systems & IoT", "Faculty of Sciences of Bizerte"),
        ("Sep 2019 — Jun 2020", "Baccalaureate in Mathematics", "Lycée Tunis, Ariana"),
    ]
    for d, title, loc in edu:
        st.markdown(f"""
        <div class='card'>
            <div class='card-title'>{title}</div>
            <div class='card-date'>📅 {d}</div>
            <div>{loc}</div>
        </div>
        """, unsafe_allow_html=True)
    st.subheader("📜 Certificates & Courses")
    certs = [
        ("IBM Full-Stack Software Developer Professional Certificate", "Coursera"),
        ("IS/IT Governance", "Coursera")
    ]
    for title, provider in certs:
        st.markdown(f"""
        <div class='card'>
            <div class='card-title'>{title}</div>
            <div class='card-date'>{provider}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────────────────────────
# Experience & Internships
# ────────────────────────────────────────────────────────────────────────────────
with tab_exp:
    st.markdown('<div class="centered-content">', unsafe_allow_html=True)
    st.header("🚀 Freelance Experiences")
    roles = [
        ("🚀 Freelance Full‑Stack Developer — Djinston", "Jan 2024 — Present",
         "Led React / Laravel / Python micro‑services MVP; built real‑time APIs and data pipelines."),
        ("🛠️ Freelance Backend Developer — Nest.js (Freelance)", "Jul 2023 — Dec 2023",
         "Developed GraphQL & REST services with 95 % test coverage using Jest & SuperTest."),
    ]
    for title, dates, desc in roles:
        st.markdown(f"""
        <div class='card'>
            <div class='card-title'>{title}</div>
            <div class='card-date'>📅 {dates}</div>
            <div>{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("📚 Internships & Major Projects")
    internships = [
        ("🛠️ Software Development Project — Cardio‑Life", "Mar 2024 — Jul 2024",
         """<ul>
            <li><b>Axon Framework</b> (CQRS + Event Sourcing) on <b>Java 17</b> Spring Micro‑services.</li>
            <li>Frontend <b>Angular 17</b> with live state sync.</li>
            <li>Infra: Axon Server (gRPC), Spring Gateway, Consul, Keycloak OIDC, Stripe, Vault.</li>
         </ul>"""),
        ("🔄 Workflow Intern — Cardio‑Life", "May 2022 — Aug 2022",
         """<ul>
            <li>Documented SOPs and streamlined equipment workflows for a med‑tech start‑up.</li>
            <li>Diagnosed device issues using diagnostic software; supported marketing policy analysis.</li>
         </ul>"""),
         ("🖥️ Web Integrator (WordPress) — Cardio‑Life", "Aug 2024 — Oct 2024",
         """<ul>
            <li>Designed, developed, and maintained a WordPress site with custom themes & plugins.</li>
            <li>Implemented inbound‑marketing strategy and on‑page SEO; increased organic traffic by 65 %.</li>
            <li>Optimized performance (caching, image compression) achieving PageSpeed ≥ 90.</li>
         </ul>"""),
         ("🖥️ Web Integrator (Angular) — Cardio‑Life-Backend", "Aug 2025 — Oct 2025",
         """<ul>
            <li>Designed, developed, and maintained a Angular site with custom themes & plugins.</li>
            <li>linked app with firebase to perform CRUD operations.</li>
            <li>Implemented inbound‑marketing strategy and on‑page SEO; increased organic traffic by 65 %.</li>
            <li>Optimized performance (caching, image compression) achieving PageSpeed ≥ 90.</li>
         </ul>"""),
    ]
    for title, dates, desc in internships:
        st.markdown(f"""
        <div class='card'>
            <div class='card-title'>{title}</div>
            <div class='card-date'>📅 {dates}</div>
            <div>{desc}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────────────────────────
# Projects
# ────────────────────────────────────────────────────────────────────────────────
with tab_proj:
    st.markdown('<div class="centered-content">', unsafe_allow_html=True)
    st.header("📊 Highlight Project")
    st.markdown(
        """
        <div class='card'>
          <div class='card-title'>🛠️ Modular Health Equipment Platform — Cardio‑Life</div>
          <div class='card-date'>📅 Mar 2024 — Jul 2024</div>
          <ul>
           <li>Built a modular Health Equipment Management & performance tracking platform.</li>
            <li>Backend on <b>Java 17</b> using <b>Spring Framework</b> & <b>Axon Framework</b> (CQRS + Event Sourcing).</li>
            <li>Frontend using <b>Angular 17</b> SPA with state management.</li>
            <li>Implemented gRPC for inter‑service communication.</li>
            <li>Infra stack: Spring Gateway, Consul, Keycloak OIDC, Stripe, Vault.</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────────────────────────
# Skills & Languages (Already compact)
# ────────────────────────────────────────────────────────────────────────────────
with tab_skills:
    st.markdown('<div class="centered-content">', unsafe_allow_html=True)
    st.markdown("<h2>💻 Technical Skills</h2>", unsafe_allow_html=True)
    
    tech_skills = {
        "Frontend": {
            "React & Next.js": 85,
            "Angular": 70,
            "TypeScript": 75,
        },
        "Backend": {
            "Java/Spring/Quarkus": 70,
            "Python (Fast-API)": 90,
            "Node.js (Nest.js)": 75,
            "PHP/Laravel/WordPress": 80
        },
        "Database": {
            "PostgreSQL": 85,
            "MongoDB": 80,
            "Redis": 70,
            "AxonIQ": 60
        },
        "Cloud": {
            "AWS": 60,
            "Azure": 50,
            "OVH": 40
        },
        "ML/Data": {
            "Python": 90,
            "R": 80,
            "Talend Data Integration": 70,
            "Power BI": 80
        },
        "Tools": {
            "Apache Kafka": 60,
            "Git/GitHub": 85,
            "Docker": 70,
            "Websocket/REST/GraphQL/Grpc": 75,
            "SEO/AEO": 80,
            "Agile/Scrum": 80,
            "CI/CD": 65,
            "Lead Gen": 75
        }
    }

    st.markdown("""
    <style>
    .compact-skill-list { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.5rem; }
    .compact-skill-item {
        background: var(--surface-color);
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        padding: 0.5rem 0.75rem;
        margin-bottom: 0.2rem;
        box-shadow: 0 1px 2px rgba(0,0,0,0.04);
        font-size: 0.97rem;
        display: flex;
        flex-direction: column;
        gap: 0.3rem;
        min-width: 0;
    }
    .compact-skill-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.97rem;
    }
    .compact-skill-name { font-weight: 500; color: var(--text-color); }
    .compact-skill-level { color: var(--primary-color); font-weight: 600; font-size: 0.9rem; }
    .compact-progress-bg {
        width: 100%;
        height: 5px;
        background: #e2e8f0;
        border-radius: 3px;
        overflow: hidden;
    }
    .compact-progress-fill {
        height: 100%;
        background: linear-gradient(90deg, var(--gradient-start), var(--gradient-end));
        border-radius: 3px;
        transition: width 1s cubic-bezier(.4,0,.2,1);
    }
    @media (max-width: 768px) {
        .compact-skill-list { grid-template-columns: 1fr; }
    }
    </style>
    """, unsafe_allow_html=True)

    for category, skills in tech_skills.items():
        st.markdown(f"<h4 style='margin-top:1.2rem;'>{category}</h4>", unsafe_allow_html=True)
        st.markdown("<div class='compact-skill-list'>", unsafe_allow_html=True)
        for skill, level in skills.items():
            st.markdown(f"""
                <div class="compact-skill-item">
                    <div class="compact-skill-header">
                        <span class="compact-skill-name">{skill}</span>
                        <span class="compact-skill-level">{level}%</span>
                    </div>
                    <div class="compact-progress-bg">
                        <div class="compact-progress-fill" style="width: {level}%"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    # Language Section
    st.markdown("<h2>🌍 Languages</h2>", unsafe_allow_html=True)
    
    languages = {
        "Arabic": {"level": "Native", "proficiency": 100, "flag": "🇹🇳"},
        "French": {"level": "Professional", "proficiency": 90, "flag": "🇫🇷"},
        "English": {"level": "Professional", "proficiency": 95, "flag": "🇺🇸"}
    }

    st.markdown("""
        <style>
        .language-list {
            display: flex;
            flex-direction: column;
            gap: 1rem;
            margin-top: 1rem;
        }

        .language-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: var(--surface-color);
            padding: 1rem;
            border-radius: 8px;
            box-shadow: var(--card-shadow);
            transition: transform 0.3s ease;
        }

        .language-item:hover {
            transform: translateY(-2px);
            box-shadow: var(--hover-shadow);
        }

        .language-flag {
            font-size: 2rem;
            margin-right: 1rem;
        }

        .language-details {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }

        .language-name {
            font-weight: 600;
            font-size: 1.2rem;
            color: var(--text-color);
        }

        .language-level {
            font-size: 1rem;
            color: var(--primary-color);
        }

        .progress-bar-bg {
            width: 100%;
            height: 6px;
            background: #e2e8f0;
            border-radius: 3px;
            overflow: hidden;
        }

        .progress-bar-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--gradient-start), var(--gradient-end));
            border-radius: 3px;
            transition: width 0.5s ease;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="language-list">', unsafe_allow_html=True)
    for lang, details in languages.items():
        st.markdown(f"""
            <div class="language-item">
                <span class="language-flag">{details['flag']}</span>
                <div class="language-details">
                    <span class="language-name">{lang}</span>
                    <span class="language-level">{details['level']}</span>
                    <div class="progress-bar-bg">
                        <div class="progress-bar-fill" style="width: {details['proficiency']}%;"></div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────────────────────────
# Extracurricular
# ────────────────────────────────────────────────────────────────────────────────
with tab_extrac:
    st.markdown('<div class="centered-content">', unsafe_allow_html=True)
    st.header("🏆 Extracurricular & Volunteer Work")
    clubs = [
        ("🎭 Rotaract Club Amilcar Sidi Bou Said — Founding Member", "Sep 2021 — Jun 2023"),
        ("🎖️ Interact Club Amilcar Sidi Bou Said — Treasurer & Team Lead", "Sep 2016 — Jun 2019"),
        ("🩺 Basic‑Life‑Support Intervenant — European Resuscitation Council", "Jun 2021 — Present"),
    ]
    for title, dates in clubs:
        st.markdown(f"""
        <div class='card'>
            <div class='card-title'>{title}</div>
            <div class='card-date'>📅 {dates}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
