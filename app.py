from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Abhi's CV.pdf"
profile_pic = current_dir / "assets" / "profilepic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Abhishek Arora"
PAGE_ICON = "random"
NAME = "Abhishek Arora"
DESCRIPTION = """
Highly Motivated graduate with strong potential
"""
EMAIL = "parasarora4040@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
  
}
PROJECTS = {
    "🏆 Image Detection and Facial Remodeling, Under Dr.Sami Azam and Menzies - School of Health Research" :"https://charlesdarwinuni.sharepoint.com/:f:/r/teams/Group8454/Shared%20Documents/General?csf=1&web=1&e=vWN5ON",
    "🏆 Solving real-time problems and Rebuilding MVR's Drivesafe portal with UX, Heuristics and Ethnographic approach" : "https://charlesdarwinuni-my.sharepoint.com/:f:/g/personal/s330022_students_cdu_edu_au/Ep3UXxa7A9REjB9SfXcnUZ8BNCf0_aYS036rA-3r0Ny93g?e=TCkhKt",
    "🏆 MVR Database Research, Under Dr.Cherry & MVR officials" : "",
    "🏆 Generated Python Based Game- Digital Excellence Award 2020 NT" : "",
    "🏆 MVR Database Research, Under Dr.Cherry & MVR officials" : "",
    "🏆 Generated Python Based Game- Digital Excellence Award 2020 NT" : "",

}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Linfox/Woolworths as a duty manager (November 2021-present)
- ✔️ ABC Driving school as an administrator (February 2021- December 2021)
- ✔️ BWS as a retailer (May 2021- November 2021)
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python,SQL, C Programming
- 📊 Data Visulization: PowerBi, MS Excel
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: MySQL, SQL Lite
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Data Analyst | Ross Industries**")
st.write("02/2020 - Present")
st.write(
    """
- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
st.write("01/2018 - 02/2022")
st.write(
    """
- ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
- ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
- ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Analyst | Chegg**")
st.write("04/2015 - 01/2018")
st.write(
    """
- ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
- ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
- ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")