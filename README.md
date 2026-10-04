# Abhi Verma - Full-Stack AI & ML Developer Portfolio

A modern, responsive, full-stack personal portfolio web application for **Abhi Verma**, a **B.Tech Computer Science Engineering student specializing in Artificial Intelligence and Machine Learning (2024–2028)**.

Built with **Python, Flask, Jinja2, SQLAlchemy (SQLite), Bootstrap 5, Font Awesome 6, and modern interactive Custom CSS/JS**.

---

## 🌟 Key Highlights & Features

- **Cyber-Minimalist AI Theme**: Dynamic dark/light mode toggle with seamless transitions and local storage persistence.
- **Interactive Neural Particles Canvas**: Custom HTML5 interactive particle network in the Hero section with mouse interaction physics.
- **Dynamic Project Details System**: Rich dynamic routes (`/projects/<slug>`) with architecture diagrams, problem/solution comparisons, challenges, and live demo links.
- **Dedicated Summer Training Showcase**: In-depth review of the practical industry immersion at Apex AI Labs, training timeline, curriculum breakdown, and verified certificate lightbox.
- **Online & Printable ATS Resume**: Interactive web resume with specialized print stylesheet (`print.css`) for 1-click clean PDF export.
- **Dynamic Blog & Learning Journey**: Article index with live keyword search and category filtering, complete with a reading layout.
- **Secure Flask Admin Dashboard**: Protected portal (`/admin`) with Werkzeug authentication to perform full CRUD operations on Projects, Blogs, Certificates, Skills, and view Contact Inquiries.
- **Interactive Contact Engine**: Asynchronous AJAX + standard form submission with server-side validation and SQLite database persistence.
- **Fully Responsive**: Optimized for ultra-wide desktop monitors, laptops, tablets, and mobile smartphones.

---

## 📂 Project Architecture

```
abhi_verma_portfolio/
├── app.py                      # Flask application factory and entry point
├── config.py                   # Configuration settings (Secret key, SQLite URI)
├── database.py                 # SQLAlchemy database instance
├── models.py                   # Schema models (Project, BlogPost, Certificate, Skill, etc.)
├── seed_data.py                # Database population script with rich initial data
├── requirements.txt            # Python dependencies
├── README.md                   # Complete documentation and setup guide
├── routes/
│   ├── __init__.py             # Blueprint exporter
│   ├── main_routes.py          # Public routes (Home, About, Skills, Projects, Blog, etc.)
│   ├── admin_routes.py         # Secure admin management routes & CRUD
│   └── api_routes.py           # AJAX API endpoints (Contact submission, filtering)
├── static/
│   ├── css/
│   │   ├── style.css           # Custom theme variables, neon glows, glassmorphism
│   │   └── print.css           # Print-optimized stylesheet for Resume PDF export
│   ├── js/
│   │   ├── main.js             # Theme switcher, counters, search filter, AJAX form
│   │   └── particles-hero.js   # Interactive neural canvas particle simulation
│   └── images/                 # Custom SVG illustrations, project banners, certificates
└── templates/
    ├── base.html               # Master layout with navbar, footer, modals
    ├── includes/
    │   ├── navbar.html         # Responsive navigation bar with dark mode toggle
    │   ├── footer.html         # Professional footer with social links & status
    │   └── alerts.html         # Flash messages component
    ├── index.html              # Homepage with all 10 ordered sections
    ├── about.html              # Detailed About Me page with education timeline & strengths
    ├── skills.html             # Categorized Skills Dashboard with animated meters
    ├── projects.html           # Project Gallery with dynamic category filters & search
    ├── project_detail.html     # Deep dive project view (architecture, features, learnings)
    ├── summer_training.html    # Dedicated Summer Training showcase & outcomes
    ├── experience.html         # Timeline of hackathons, projects, and activities
    ├── certifications.html     # Certificate gallery with lightbox modal viewer
    ├── hackathons.html         # Hackathon projects, problem statements & solutions
    ├── resume.html             # Interactive Resume with 1-click Print/PDF export
    ├── blog.html               # Tech Blog & Learning Journey post index
    ├── blog_detail.html        # Single Blog Post reader with code highlighting
    ├── contact.html            # Contact page with validated form & social cards
    ├── 404.html                # Custom 404 Not Found error page
    ├── 500.html                # Custom 500 Server Error page
    └── admin/
        ├── login.html          # Admin authentication page
        ├── dashboard.html      # Stats overview, quick actions, inquiries counter
        ├── projects.html       # Project management list (Add/Edit/Delete)
        ├── project_form.html   # Create/Edit project form
        ├── blogs.html          # Blog management list
        ├── blog_form.html      # Create/Edit blog post form
        ├── certificates.html   # Certificate management
        ├── cert_form.html      # Create/Edit certificate form
        ├── skills.html         # Skill management dashboard
        ├── skill_form.html     # Create/Edit skill form
        └── messages.html       # Contact form submissions inbox with reply links
```

---

## 🚀 Quick Start & Installation

### 1. Prerequisites
Ensure you have Python 3.9+ installed on your system.

### 2. Navigate to the project directory
```bash
cd "C:\Users\Abhi Verma\.gemini\antigravity\scratch\abhi_verma_portfolio"
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Seed Database (Auto-seeds on first run, or run manually)
```bash
python seed_data.py
```

### 5. Start the Flask Application
```bash
python app.py
```

Open your browser and visit: **`http://127.0.0.1:5000`**

---

## 🔐 Admin Dashboard Access

- **URL**: `http://127.0.0.1:5000/admin/login`
- **Default Username**: `admin`
- **Default Password**: `admin123`

The admin dashboard provides full content management capabilities:
- **Projects**: Add new projects, update screenshots, edit system architecture flow, toggle featured status.
- **Blog Posts**: Draft and publish Markdown/HTML formatted technical articles.
- **Certificates**: Add new credentials with issuing organization and lightbox previews.
- **Skills Matrix**: Adjust proficiency percentages, categories, and icon classes.
- **Inquiries Inbox**: Review incoming contact inquiries and reply directly via email.

---

## 📱 Pages & Dynamic Routes

| Route | Description |
|---|---|
| `/` | Main landing page featuring all 10 ordered sections |
| `/about` | Bio, B.Tech CSE (AI & ML) timeline (2024–2028), strengths |
| `/skills` | Filterable skill dashboard with animated proficiency meters |
| `/projects` | Filterable project showcase by domain with live keyword search |
| `/projects/<slug>` | Deep-dive dynamic project breakdown (e.g. `/projects/studylens-ai`) |
| `/summer-training` | Dedicated Summer Training report at Apex AI Labs |
| `/experience` | Milestone timeline covering hackathons and technical leadership |
| `/certifications` | Certificate gallery with instant lightbox modal zoom |
| `/hackathons` | Smart India Hackathon and competitive event showcases |
| `/resume` | ATS-compliant online resume with 1-click print / PDF export |
| `/blog` | Searchable technical blog and learning notes |
| `/blog/<slug>` | Single blog post reader with formatted code blocks |
| `/contact` | Validated contact form with SQLite message storage |
| `/admin/*` | Secure admin control center |

---

## 📄 License & Attribution

Created with precision for **Abhi Verma** — B.Tech Computer Science Engineering (AI & ML), 2024–2028.
