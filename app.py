import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Page config
st.set_page_config(page_title="Narasimha Naidu - Portfolio", layout="centered")

# Function to load lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animations (replaced one broken link)
lottie_portfolio = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_mjlh3hcy.json")
lottie_skills = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_tno6cg2w.json")
lottie_projects = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_0yfsb3a1.json")  
lottie_experience = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_j1adxtyb.json")
lottie_education = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_HpFqiS.json")

# Sidebar navigation
st.sidebar.title("📁 Narasimha Naidu - Portfolio")
selection = st.sidebar.radio(
    "Navigate",
    ["Professional Background", "Technical Skills", "Projects", "Experience", "Education"]
)

# Global Personal Info
st.title("👨‍💻 Narasimha Naidu Nagam")
st.markdown("📧 **nagamnaidu3@gmail.com** | 📞 **+91 9492252452 / +91 9515874452**")
st.markdown("---")

# Inject CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
        font-family: 'Arial', sans-serif;
    }
    h1, h2, h3 {
        color: #0f4c75;
    }
    .section-style {
        padding: 10px;
        border-left: 5px solid #3282b8;
        margin-bottom: 20px;
        background-color: #e3f2fd;
        border-radius: 8px;
    }
    .footer-buttons a {
        text-decoration: none;
        color: white;
        padding: 8px 16px;
        border-radius: 8px;
        margin: 5px;
        display: inline-block;
    }
    .github-button {
        background-color: green;
    }
    .linkedin-button {
        background-color: red;
    }
    </style>
""", unsafe_allow_html=True)

# Page content
if selection == "Professional Background":
    if lottie_portfolio:
        st_lottie(lottie_portfolio, height=200)
    else:
        st.warning("⚠️ Animation failed to load.")
    st.markdown('<div class="section-style">', unsafe_allow_html=True)
    st.header("🎯 Objective")
    st.write("""
    To excel as a highly skilled and versatile professional with 4+ years of experience in the Oil & Gas industry 
    and hands-on training in React-based web development. With strong problem-solving abilities and a passion 
    for continuous learning, I aim to contribute to an innovative organization while deepening my expertise 
    in AI, Machine Learning, and data-driven applications.
    """)
    st.header("📌 Professional Summary")
    st.markdown("""
    - 4+ years in Oil & Gas with instrumentation and process engineering expertise.  
    - Web developer with ReactJS, Redux Toolkit, Tailwind CSS.  
    - Proficient in Python, NumPy, Pandas, Scikit-learn, Matplotlib.  
    - Built and deployed ML models using **Streamlit**.  
    - Strong communicator, quick learner, and adaptable across domains.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif selection == "Technical Skills":
    if lottie_skills:
        st_lottie(lottie_skills, height=200)
    else:
        st.warning("⚠️ Animation failed to load.")
    st.markdown('<div class="section-style" style="background-color:#fce4ec;">', unsafe_allow_html=True)
    st.header("🛠️ Technical Skills")
    st.markdown("""
    - **Web Development:** HTML, CSS, JavaScript, ReactJS, Tailwind CSS, Bootstrap, Streamlit  
    - **Languages:** Python, JavaScript  
    - **AI/ML Tools:** NumPy, Pandas, Scikit-learn, Matplotlib, Jupyter Notebook  
    - **Version Control:** Git, GitHub  
    - **IDE/Tools:** Visual Studio Code, Redux Toolkit  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif selection == "Projects":
    if lottie_projects:
        st_lottie(lottie_projects, height=200)
    else:
        st.warning("⚠️ Animation failed to load.")
    st.markdown('<div class="section-style" style="background-color:#fff9c4;">', unsafe_allow_html=True)
    st.header("📁 Project")
    st.subheader("Swiggy Clone | Duration: 6 Months")
    st.markdown("""
    - Built responsive food delivery app using ReactJS and Tailwind CSS  
    - Used Redux Toolkit, Hooks, and Atomic Design principles  
    - Integrated dynamic listings and mobile-optimized cart system  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif selection == "Experience":
    if lottie_experience:
        st_lottie(lottie_experience, height=200)
    else:
        st.warning("⚠️ Animation failed to load.")
    st.markdown('<div class="section-style" style="background-color:#d1f2eb;">', unsafe_allow_html=True)
    st.header("💼 Professional Experience")
    st.subheader("Software Engineer (Trainee) – Lyros Technology Pvt. Ltd | Jan 2025 – Present")
    st.markdown("""
    - Built and deployed ML models using Python and Streamlit  
    - Created interactive ML dashboards  
    - Worked on real-time data-driven applications  
    """)
    st.subheader("Process Engineer – ADI Associates, Mumbai (ONGC Offshore) | Jan 2024 – Jul 2024")
    st.markdown("""
    - Managed process operations on ONGC offshore platforms  
    - Ensured safety compliance and team collaboration  
    """)
    st.subheader("Associate Trainee Engineer – ANI Integrated Ltd Services | Apr 2022 – Dec 2023")
    st.markdown("""
    - Calibrated and troubleshot plant instrumentation systems  
    """)
    st.subheader("Graduate Engineer Trainee – LNG Bharat Pvt Ltd | Sep 2019 – Mar 2022")
    st.markdown("""
    - Oversaw well operations and equipment testing  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif selection == "Education":
    if lottie_education:
        st_lottie(lottie_education, height=200)
    else:
        st.warning("⚠️ Animation failed to load.")
    st.markdown('<div class="section-style" style="background-color:#ede7f6;">', unsafe_allow_html=True)
    st.header("🎓 Education")
    st.markdown("""
    **B.Tech in Petroleum Technology Engineering**  
    Aditya Engineering College (2015 – 2019) | Percentage: 75%
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer with styled buttons
st.markdown("---")
st.markdown("""
<div class="footer-buttons">
    <a href="https://github.com/NagamNaidu/Portfolio_resume" class="github-button" target="_blank">GitHub</a>
    <a href="https://www.linkedin.com/in/nagam-narasimha-naidu-836a92176" class="linkedin-button" target="_blank">LinkedIn</a>
</div>
""", unsafe_allow_html=True)
