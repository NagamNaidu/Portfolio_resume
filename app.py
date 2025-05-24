import streamlit as st

# Page config
st.set_page_config(page_title="Narasimha Naidu - Portfolio", layout="centered")

# Sidebar navigation
st.sidebar.title("📂 Portfolio Sections")
selection = st.sidebar.radio(
    "Go to",
    ["Professional Background", "Technical Skills", "Projects", "Experience", "Education"]
)

# Personal Info (displayed on all pages)
st.title("👨‍💻 Narasimha Naidu Nagam")
st.markdown("📧 **nagamnaidu3@gmail.com** | 📞 **+91 9492252452 / +91 9515874452**")
st.markdown("---")

# Page content rendering
if selection == "Professional Background":
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

elif selection == "Technical Skills":
    st.header("🛠️ Technical Skills")
    st.markdown("""
    - **Web Development:** HTML, CSS, JavaScript, ReactJS, Tailwind CSS, Bootstrap, Streamlit  
    - **Languages:** Python, JavaScript  
    - **AI/ML Tools:** NumPy, Pandas, Scikit-learn, Matplotlib, Jupyter Notebook  
    - **Version Control:** Git, GitHub  
    - **IDE/Tools:** Visual Studio Code, Redux Toolkit  
    """)

elif selection == "Projects":
    st.header("📁 Project")
    st.subheader("Swiggy Clone | Duration: 6 Months")
    st.markdown("""
    - Built responsive food delivery app using ReactJS and Tailwind CSS  
    - Used Redux Toolkit, Hooks, and Atomic Design principles  
    - Integrated dynamic listings and mobile-optimized cart system  
    """)

elif selection == "Experience":
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

elif selection == "Education":
    st.header("🎓 Education")
    st.markdown("""
    **B.Tech in Petroleum Technology Engineering**  
    Aditya Engineering College (2015 – 2019) | Percentage: 75%
    """)

# Footer
st.markdown("---")
st.markdown("🔗 [GitHub](https://github.com/) | [LinkedIn](https://linkedin.com/) *(Add your links here)*")
