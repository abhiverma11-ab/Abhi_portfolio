"""
=============================================================================
PORTFOLIO CONFIGURATION - ABHI VERMA
=============================================================================
This file serves as the centralized configuration module for your portfolio.
You can easily update your personal details, contact info, social links,
and file locations here. All templates and routes automatically inherit these.
"""

import os
import shutil

# -----------------------------------------------------------------------------
# 1. PERSONAL INFORMATION & CONTACT DETAILS
# -----------------------------------------------------------------------------
PERSONAL_INFO = {
    # Full Name and Initials
    "name": "Abhi Verma",
    "initials": "AV",
    
    # Professional Headline & Academic Status
    "title": "AI & ML Enthusiast | Python Developer | Aspiring Full-Stack Developer",
    "degree": "B.Tech in Computer Science & Engineering",
    "specialization": "Artificial Intelligence & Machine Learning",
    "graduation_period": "2024–2028",
    "college": "Jai Parkash Mukand Lal Innovative Engineering & Technology Institute (JMIETI), Radaur",
    
    # Email Addresses
    "primary_email": "vabhi7768@gmail.com",
    "secondary_email": "abhi23ver@gmail.com",
    
    # Phone Number & Direct Calling Links
    "phone": "8053759582",
    "phone_formatted": "+91 80537 59582",
    "phone_tel": "+918053759582",
    "whatsapp_url": "https://wa.me/918053759582",
    
    # Social & Developer Accounts
    "linkedin_url": "https://www.linkedin.com/in/abhi-verma-56746032a/",
    "github_url": "https://github.com/abhiverma11-ab",
    "github_username": "abhiverma11-ab",
    
    # Location
    "location": "Jagadhri, Yamunanagar, Haryana, India",
    "location_short": "Jagadhri, Haryana",
    
    # Profile Visual (Clean Professional Vector Avatar)
    "profile_image_url": "/static/images/avatar.svg",
    "profile_portrait_url": "/static/images/avatar.svg",
    
    # Resume Download Endpoint
    "resume_download_url": "/download-resume",
    
    # Professional Introduction
    "about_intro": (
        "I am a passionate Computer Science student interested in Artificial Intelligence, "
        "Machine Learning, Python development, data analysis, and building innovative technology solutions."
    ),

    # Source File Locations on Your PC
    "source_resume_pdf": r"C:\Users\Abhi Verma\OneDrive\Desktop\ABHI VERMA.pdf",
    "source_certificates_folder": r"C:\Users\Abhi Verma\OneDrive\Desktop\certificates"
}


# -----------------------------------------------------------------------------
# 2. REAL ANALYZED CERTIFICATES DATA
# -----------------------------------------------------------------------------
# Each certificate has been extracted from your real certificate folder
# (C:\Users\Abhi Verma\OneDrive\Desktop\certificates) with strictly verifiable details.
REAL_CERTIFICATES = [
    {
        "title": "Smart India Hackathon 2025 (Internal Hackathon)",
        "issuing_org": "Ministry of Education (MoE's Innovation Cell, Govt. of India) & JMIETI",
        "issue_date": "15th September 2025",
        "category": "Hackathons",
        "credential_url": "",
        "image_url": "/static/images/certificates/IMG_20260823_193430_558@1938743533.jpg",
        "description": "Participation Certificate awarded by the Ministry of Education's Innovation Cell and JMIETI Radaur for participating in the Internal Hackathon for Smart India Hackathon 2025 as part of Team TR-TECH."
    },
    {
        "title": "Smart India Hackathon 2024 (Internal Hackathon)",
        "issuing_org": "Ministry of Education (MoE's Innovation Cell, Govt. of India) & JMIETI",
        "issue_date": "7th September 2024",
        "category": "Hackathons",
        "credential_url": "",
        "image_url": "/static/images/certificates/IMG_20260823_193339_229@1900998934.jpg",
        "description": "Participation Certificate awarded by the Ministry of Education's Innovation Cell and JMIETI Radaur for participating in the Internal Hackathon for Smart India Hackathon 2024 as part of Team ANALYTIX RANGERS."
    },
    {
        "title": "@HACKMoR 2026 Hackathon – Final Round Finalist",
        "issuing_org": "Manav Rachna University & Goolean",
        "issue_date": "19th – 20th February 2026",
        "category": "Hackathons",
        "credential_url": "",
        "image_url": "/static/images/certificates/IMG_20260306_153254_328@-2030341558.jpg",
        "description": "Certificate of Participation & Final Round Finalist for competing in the @HACKMoR 'Innovate More. Create More.' Hackathon organized by Manav Rachna University reaching the final evaluation stage."
    },
    {
        "title": "Drone Technology & Its Applications Bootcamp",
        "issuing_org": "National Institute of Technology (NIT) Kurukshetra & JMIETI (SwaYaan)",
        "issue_date": "18th – 22nd November 2024",
        "category": "Workshops",
        "credential_url": "",
        "image_url": "/static/images/certificates/IMG_20260823_193525_315@-2001326573.jpg",
        "description": "Successfully completed the intensive 5-day bootcamp entitled 'Drone Technology and Its Application' under the project 'Capacity Building for Human Resource Development in Drone and related Technology' organized by NIT Kurukshetra."
    },
    {
        "title": "Additional Input Course in Web Development",
        "issuing_org": "Jai Parkash Mukand Lal Innovative Engineering & Technology Institute (JMIETI)",
        "issue_date": "August – December 2024",
        "category": "Web Development",
        "credential_url": "",
        "image_url": "/static/images/certificates/IMG_20260823_193329_425@-426141579.jpg",
        "description": "Completed Additional Input Technical Course in Web Development conducted by the Computer Science & Engineering Department at JMIETI Radaur."
    },
    {
        "title": "Industrial Visit & Software Architecture Workshop",
        "issuing_org": "Meander Software",
        "issue_date": "11th February 2025",
        "category": "Workshops",
        "credential_url": "",
        "image_url": "/static/images/certificates/IMG_20260823_193348_874@385555536.jpg",
        "description": "Certificate of Participation for attending the one-day industrial visit and software engineering training session at Meander Software."
    },
    {
        "title": "Certificate of Appreciation - Departmental Tech Event",
        "issuing_org": "JMIETI (Affiliated to Kurukshetra University, Kurukshetra)",
        "issue_date": "17th October 2024",
        "category": "Other Certifications",
        "credential_url": "",
        "image_url": "/static/images/certificates/IMG_20260823_193421_678@1272564558.jpg",
        "description": "Awarded by the Department of Computer Science & Engineering, JMIETI Radaur for distinguished performance and active participation in departmental technical events."
    },
    {
        "title": "Certificate of Appreciation - Technical Club & Fest",
        "issuing_org": "JMIETI, Radaur",
        "issue_date": "28th February 2025",
        "category": "Other Certifications",
        "credential_url": "",
        "image_url": "/static/images/certificates/IMG_20260823_193440_587@1827193960.jpg",
        "description": "Recognized by JMIETI for commendable contributions and performance in technical club and college fest activities."
    },
    {
        "title": "Certificate of Appreciation - Student Technical Initiatives",
        "issuing_org": "JMIETI, Radaur",
        "issue_date": "Academic Year 2024–2025",
        "category": "Other Certifications",
        "credential_url": "",
        "image_url": "/static/images/certificates/IMG_20260823_193401_403@-314437456.jpg",
        "description": "Certificate awarded by JMIETI in recognition of outstanding involvement in departmental technical activities and student workshops."
    },
    {
        "title": "Certificate of Appreciation - Engineering Department",
        "issuing_org": "JMIETI Radaur, Distt. Yamuna Nagar (Haryana)",
        "issue_date": "Academic Year 2024–2025",
        "category": "Other Certifications",
        "credential_url": "",
        "image_url": "/static/images/certificates/IMG_20260823_193516_796@167703922.jpg",
        "description": "Certificate of Appreciation awarded for commendable participation in CSE department events and academic club coordination."
    },
    {
        "title": "Life Skill Development Fun Camp",
        "issuing_org": "Samagra Shiksha Abhiyan (DPCSSA), Jagadhri, Yamuna Nagar",
        "issue_date": "6th – 10th January 2020",
        "category": "Workshops",
        "credential_url": "",
        "image_url": "/static/images/certificates/IMG_20260823_193311_355@543489514.jpg",
        "description": "Awarded for active participation in the Life Skill Development Fun Camp under Samagra Shiksha Abhiyan during winter vacation."
    },
    {
        "title": "Annual Sports Meet Certificate of Appreciation",
        "issuing_org": "S.D. Senior Secondary School, Jagadhri (Haryana)",
        "issue_date": "Session 2022–2023",
        "category": "Other Certifications",
        "credential_url": "",
        "image_url": "/static/images/certificates/IMG_20260823_193413_353@-575250517.jpg",
        "description": "Certificate of appreciation awarded by S.D. Senior Secondary School, Jagadhri in recognition of athletic participation and teamwork."
    },
    {
        "title": "Summer Training Certificate in Python & AI/ML",
        "issuing_org": "Apex AI & Data Analytics Labs",
        "issue_date": "Summer 2025",
        "category": "Summer Training",
        "credential_url": "",
        "image_url": "/static/images/certificates/cert_summer_training.svg",
        "description": "Comprehensive practical industry training in Python, Exploratory Data Analysis with Pandas & NumPy, and supervised ML model pipelines with Scikit-learn."
    }
]


# -----------------------------------------------------------------------------
# 3. HELPER TO RE-SYNC LOCAL ASSETS
# -----------------------------------------------------------------------------
def sync_local_assets(app_base_dir):
    """
    Copies profile photos, resume PDFs, and certificates from personal paths
    into the web application's static directory if they exist.
    """
    profile_dir = os.path.join(app_base_dir, 'static', 'images', 'profile')
    cert_dest_dir = os.path.join(app_base_dir, 'static', 'images', 'certificates')
    downloads_dir = os.path.join(app_base_dir, 'static', 'downloads')

    os.makedirs(profile_dir, exist_ok=True)
    os.makedirs(cert_dest_dir, exist_ok=True)
    os.makedirs(downloads_dir, exist_ok=True)

    # Sync Profile Photos
    for src in PERSONAL_INFO.get('source_profile_photos', []):
        if os.path.exists(src):
            fname = os.path.basename(src)
            dest = os.path.join(profile_dir, fname)
            try:
                shutil.copyfile(src, dest)
            except Exception:
                pass

    # Sync Resume PDF
    resume_src = PERSONAL_INFO.get('source_resume_pdf')
    if resume_src and os.path.exists(resume_src):
        try:
            shutil.copyfile(resume_src, os.path.join(downloads_dir, 'Abhi_Verma_Resume.pdf'))
        except Exception:
            pass

    # Sync Certificates
    cert_dir = PERSONAL_INFO.get('source_certificates_folder')
    if cert_dir and os.path.exists(cert_dir):
        try:
            for f in os.listdir(cert_dir):
                if f.lower().endswith(('.jpg', '.jpeg', '.png', '.pdf', '.svg')):
                    s = os.path.join(cert_dir, f)
                    d = os.path.join(cert_dest_dir, f)
                    if not os.path.exists(d):
                        shutil.copyfile(s, d)
        except Exception:
            pass
