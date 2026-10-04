from database import db
from models import AdminUser, Project, BlogPost, Certificate, Skill, Experience, Hackathon, ContactMessage
from config import Config
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app

def seed_database():
    app = create_app()
    with app.app_context():
        db.create_all()

        # 1. Seed Admin User (default: admin / admin123)
        if not AdminUser.query.filter_by(username='admin').first():
            admin = AdminUser(username='admin')
            admin.set_password('admin123')
            db.session.add(admin)
            print("Seeded default admin user: admin / admin123")

        # 2. Seed Projects
        if Project.query.count() == 0:
            projects = [
                Project(
                    title="IPL Data Analysis Dashboard",
                    slug="ipl-data-analysis-dashboard",
                    subtitle="Interactive Exploratory Data Analysis & Match Performance Intelligence",
                    description="An end-to-end data analytics web platform that ingests historical IPL match datasets, performs multidimensional statistical aggregations, and delivers interactive visual dashboards for team dynamics, player consistency metrics, and match outcome probabilities.",
                    problem_statement="Cricket analytics requires parsing vast ball-by-ball datasets into actionable visual insights for team strategists and enthusiasts without needing manual querying.",
                    solution="Engineered a streamlined Python data pipeline utilizing Pandas and NumPy to clean, aggregate, and transform 15+ seasons of IPL match data into high-performance interactive Plotly and Streamlit visualization dashboards.",
                    architecture_desc="Raw CSV Data Ingestion -> Pandas Preprocessing & Imputation -> Analytical Feature Engineering -> Plotly Dynamic Visualization Engine -> Streamlit/Flask UI.",
                    features="Comprehensive Head-to-Head Team Comparisons\nPlayer Strike Rate, Economy & Impact Score Analysis\nVenue-Specific Toss Decision & Win Probability Trends\nInteractive Filter by Season, Stadium, Bowler Type & Batsman Phase\nDownloadable PDF & CSV statistical summary reports",
                    challenges="Handling historical data inconsistencies across changing team franchises, rain-impacted Duckworth-Lewis match outcomes, and rendering complex interactive multi-axis charts with sub-second latency.",
                    learnings="Mastered advanced vector operations in Pandas, statistical distributions, responsive data visualization design with Plotly, and clean data wrangling pipelines.",
                    technologies="Python, Pandas, NumPy, Plotly, Streamlit, Seaborn, Matplotlib",
                    category="Data Analysis",
                    image_url="/static/images/projects/ipl_analysis.svg",
                    github_link="https://github.com/abhi-verma/ipl-data-analysis",
                    live_link="https://abhi-ipl-analytics.streamlit.app",
                    is_featured=True
                ),
                Project(
                    title="StudyLens AI",
                    slug="studylens-ai",
                    subtitle="AI-Powered Intelligent Academic Document & Research Assistant",
                    description="An advanced Retrieval-Augmented Generation (RAG) learning platform where students and researchers can upload PDFs, PPTs, textbooks, and academic papers to engage in contextual AI dialogues, generate concise flashcards, and extract key conceptual summaries instantly.",
                    problem_statement="Students often spend hours sifting through dense academic documents to extract core definitions, revision summaries, and exam-oriented problem solutions.",
                    solution="Created an end-to-end Flask application that chunks uploaded academic documents, indexes embeddings using vector search, and leverages large language model retrieval to deliver accurate, citation-backed answers and automated revision aids.",
                    architecture_desc="Document Ingestion (PyPDF2 / PDFPlumber) -> Text Semantic Chunking -> Vector Embeddings Database -> Context Retrieval Query Engine -> LLM Generation Pipeline -> Flask Dynamic Web Interface.",
                    features="Multi-format document parsing (PDF, DOCX, PPTX, TXT)\nContext-aware Q&A with exact page citation references\nAutomated AI Flashcard & Quiz generation for quick revision\nKey concept extraction and multi-level summarization\nLocal storage and session history for past study chats",
                    challenges="Optimizing text chunk boundary overlaps to prevent context truncation and maintaining fast response latency during dense PDF parsing.",
                    learnings="Deepened understanding of RAG architectures, prompt engineering, vector distance metrics, full-stack Flask architecture, and modern async frontend interfaces.",
                    technologies="Python, Flask, PyTorch, Transformers, RAG, SQLite, HTML5, CSS3, JavaScript",
                    category="AI",
                    image_url="/static/images/projects/studylens_ai.svg",
                    github_link="https://github.com/abhi-verma/studylens-ai",
                    live_link="https://studylens-ai.demo.local",
                    is_featured=True
                ),
                Project(
                    title="AI Career Guidance Project",
                    slug="ai-career-guidance",
                    subtitle="Intelligent Machine Learning Recommendation System for Career Pathways",
                    description="A machine learning-driven web application designed to help engineering and computer science students discover optimal career domains, required skill pathways, and personalized skill gap roadmaps based on psychometric tests, academic performance, and personal interests.",
                    problem_statement="Early-stage students face choice paralysis due to rapidly shifting tech domains (AI, Web3, DevOps, Cloud) without customized guidance based on their individual aptitude.",
                    solution="Developed a classification and recommendation engine using Scikit-learn (Random Forests & XGBoost) trained on student skills, passion indices, and industry role requirements, providing clear actionable skill acquisition checklists.",
                    architecture_desc="User Aptitude Survey -> Feature Scaling & Encoding -> Scikit-learn Classification Engine -> Career Matching Algorithm -> Dynamic Roadmap Renderer.",
                    features="Multi-factor aptitude and interest evaluation test\nTop 3 Recommended Career Paths with confidence match percentages\nPersonalized Step-by-Step Learning Roadmaps & Recommended Courses\nInteractive Skill Matrix comparison against industry job benchmarks\nExportable career report in PDF format",
                    challenges="Formulating an unbiased training dataset and calibrating confidence scores across emerging multidisciplinary roles like MLOps and Prompt Engineering.",
                    learnings="Supervised classification model evaluation (F1-score, Confusion Matrix), feature importance analysis, model serialization with Pickle/Joblib, and seamless Flask API integration.",
                    technologies="Python, Flask, Scikit-learn, Pandas, XGBoost, Bootstrap 5, Chart.js",
                    category="Machine Learning",
                    image_url="/static/images/projects/career_guidance.svg",
                    github_link="https://github.com/abhi-verma/ai-career-guidance",
                    live_link="https://ai-career-guidance.demo.local",
                    is_featured=True
                ),
                Project(
                    title="Train Traffic Control Using AI",
                    slug="train-traffic-control-ai",
                    subtitle="Intelligent Dynamic Scheduling & Railway Congestion Mitigation Simulator",
                    description="An innovative AI-powered digital twin simulation system designed for automated railway network optimization, conflict resolution at critical junctions, and predictive dynamic rescheduling during delays.",
                    problem_statement="Railway networks experience cascading delays when unexpected hold-ups occur at high-density junctions, where traditional fixed scheduling fails to adapt dynamically.",
                    solution="Engineered a heuristic and reinforcement learning scheduling model that monitors simulated junction states, predicts bottleneck propagation, and dynamically re-routes train priorities to minimize total network dwell time.",
                    architecture_desc="Railway Network Graph Modeler -> Real-Time Simulation Engine (SimPy) -> AI Optimization & Conflict Resolver -> WebSocket Dispatcher -> Interactive Canvas Dashboard.",
                    features="Real-time live digital twin train map and junction tracking\nPredictive bottleneck identification and early warning alerts\nAutomated dynamic rescheduling to minimize cumulative passenger delay\nEmergency override and manual dispatcher simulation mode\nComprehensive operational analytics on throughput and turnaround time",
                    challenges="Modeling complex graph topologies with single-track bi-directional constraints while calculating optimal reschedule combinations in real time.",
                    learnings="Graph algorithms, state-space search algorithms (A*, Heuristic Optimization), discrete-event simulation with Python, and interactive web dashboard visualizers.",
                    technologies="Python, Flask, AI/ML, Heuristic Algorithms, WebSockets, HTML5 Canvas, Bootstrap",
                    category="AI",
                    image_url="/static/images/projects/train_traffic.svg",
                    github_link="https://github.com/abhi-verma/train-traffic-control-ai",
                    live_link="https://train-traffic-ai.demo.local",
                    is_featured=True
                ),
                Project(
                    title="Automated Resume Analyzer & Matcher",
                    slug="automated-resume-analyzer",
                    subtitle="NLP-Powered Candidate Skill Extraction and Job Description Matcher",
                    description="An intelligent Natural Language Processing tool that extracts entities, skills, education, and years of experience from PDF resumes to compute semantic cosine similarity against target job descriptions.",
                    problem_statement="Manual resume screening for technical internships and jobs is time-consuming and prone to keyword omission errors.",
                    solution="Implemented SpaCy and TF-IDF vectorization pipelines with custom regex patterns to rank applicants and highlight missing prerequisite skills.",
                    architecture_desc="PDF Ingestion -> NLP Text Normalization -> Named Entity Recognition (NER) -> TF-IDF & Cosine Similarity -> Ranked Dashboard.",
                    features="Bulk resume batch upload and parsing\nAutomated skill tagging (Languages, Frameworks, Cloud, Databases)\nMatch score breakdown with missing keyword recommendations\nClean tabular recruiter dashboard with export capability",
                    challenges="Extracting text accurately from multi-column resume layouts without losing token order.",
                    learnings="NLP fundamentals, Named Entity Recognition, TF-IDF vector scoring, and file handling in Flask.",
                    technologies="Python, Flask, NLP, SpaCy, Scikit-learn, Bootstrap",
                    category="Python",
                    image_url="/static/images/projects/resume_analyzer.svg",
                    github_link="https://github.com/abhi-verma/resume-analyzer-nlp",
                    live_link="https://resume-nlp.demo.local",
                    is_featured=False
                ),
                Project(
                    title="Real-Time Hand Gesture Controller",
                    slug="real-time-hand-gesture-controller",
                    subtitle="Computer Vision System for Contactless Media & System Control",
                    description="A computer vision application that captures webcam video streams, detects 21 3D hand landmark coordinates, and maps gesture combinations to system volume, slide navigation, and cursor movement.",
                    problem_statement="Need for hands-free, contactless human-computer interaction during presentations and accessibility scenarios.",
                    solution="Utilized OpenCV and Google MediaPipe to track hand landmarks in real time with high FPS and translated finger distance vectors into OS-level input commands via PyAutoGUI.",
                    architecture_desc="Webcam Frame Capture -> MediaPipe Landmark Detection -> Euclidean Coordinate Calculation -> Gesture Classifier -> PyAutoGUI OS Trigger.",
                    features="Real-time multi-gesture classification (Pinch, Fist, Peace, Point)\nSmooth virtual mouse cursor navigation\nSlide presenter mode for PowerPoint/PDF presentations\nCustom gesture recording and threshold calibration UI",
                    challenges="Eliminating jitter during finger-point cursor navigation without introducing input lag.",
                    learnings="Computer Vision pipelines, coordinate geometry, video stream optimization, and real-time processing.",
                    technologies="Python, OpenCV, MediaPipe, NumPy, PyAutoGUI",
                    category="Machine Learning",
                    image_url="/static/images/projects/gesture_controller.svg",
                    github_link="https://github.com/abhi-verma/hand-gesture-controller",
                    live_link="https://gesture-ai.demo.local",
                    is_featured=False
                )
            ]
            db.session.bulk_save_objects(projects)
            print(f"Seeded {len(projects)} projects.")

        # 3. Seed Skills
        if Skill.query.count() == 0:
            skills = [
                # Programming Languages
                Skill(name="Python", category="Programming Languages", proficiency=92, icon_class="fab fa-python", badge_color="warning", display_order=1),
                Skill(name="C++", category="Programming Languages", proficiency=85, icon_class="fas fa-code", badge_color="primary", display_order=2),
                Skill(name="C", category="Programming Languages", proficiency=80, icon_class="fas fa-terminal", badge_color="secondary", display_order=3),
                Skill(name="SQL", category="Programming Languages", proficiency=85, icon_class="fas fa-database", badge_color="info", display_order=4),
                Skill(name="JavaScript", category="Programming Languages", proficiency=78, icon_class="fab fa-js", badge_color="warning", display_order=5),
                Skill(name="HTML5 / CSS3", category="Programming Languages", proficiency=90, icon_class="fab fa-html5", badge_color="danger", display_order=6),

                # Python & Data Science
                Skill(name="Pandas", category="Python & Data Science", proficiency=90, icon_class="fas fa-table", badge_color="primary", display_order=7),
                Skill(name="NumPy", category="Python & Data Science", proficiency=88, icon_class="fas fa-cube", badge_color="info", display_order=8),
                Skill(name="Matplotlib", category="Python & Data Science", proficiency=85, icon_class="fas fa-chart-line", badge_color="success", display_order=9),
                Skill(name="Scikit-learn", category="Python & Data Science", proficiency=85, icon_class="fas fa-brain", badge_color="warning", display_order=10),
                Skill(name="Seaborn", category="Python & Data Science", proficiency=82, icon_class="fas fa-chart-bar", badge_color="danger", display_order=11),

                # Web Development
                Skill(name="Flask", category="Web Development", proficiency=88, icon_class="fas fa-server", badge_color="dark", display_order=12),
                Skill(name="Bootstrap 5", category="Web Development", proficiency=90, icon_class="fab fa-bootstrap", badge_color="primary", display_order=13),
                Skill(name="Jinja2", category="Web Development", proficiency=85, icon_class="fas fa-file-code", badge_color="danger", display_order=14),
                Skill(name="RESTful APIs", category="Web Development", proficiency=82, icon_class="fas fa-network-wired", badge_color="info", display_order=15),
                Skill(name="Responsive UI/UX", category="Web Development", proficiency=88, icon_class="fas fa-mobile-alt", badge_color="success", display_order=16),

                # Machine Learning
                Skill(name="Linear & Logistic Regression", category="Machine Learning", proficiency=90, icon_class="fas fa-chart-area", badge_color="primary", display_order=17),
                Skill(name="Decision Trees & Random Forests", category="Machine Learning", proficiency=86, icon_class="fas fa-tree", badge_color="success", display_order=18),
                Skill(name="K-Nearest Neighbors (KNN)", category="Machine Learning", proficiency=84, icon_class="fas fa-project-diagram", badge_color="info", display_order=19),
                Skill(name="Support Vector Machines (SVM)", category="Machine Learning", proficiency=80, icon_class="fas fa-vector-square", badge_color="warning", display_order=20),
                Skill(name="K-Means Clustering", category="Machine Learning", proficiency=85, icon_class="fas fa-shapes", badge_color="secondary", display_order=21),
                Skill(name="Neural Networks Basics", category="Machine Learning", proficiency=76, icon_class="fas fa-network-wired", badge_color="danger", display_order=22),

                # Tools & Platforms
                Skill(name="Git & GitHub", category="Tools & Platforms", proficiency=88, icon_class="fab fa-github", badge_color="dark", display_order=23),
                Skill(name="VS Code", category="Tools & Platforms", proficiency=95, icon_class="fas fa-laptop-code", badge_color="primary", display_order=24),
                Skill(name="Jupyter Notebook", category="Tools & Platforms", proficiency=90, icon_class="fas fa-book-open", badge_color="warning", display_order=25),
                Skill(name="Streamlit", category="Tools & Platforms", proficiency=85, icon_class="fas fa-tachometer-alt", badge_color="danger", display_order=26),
                Skill(name="SQLite / MySQL", category="Tools & Platforms", proficiency=82, icon_class="fas fa-database", badge_color="info", display_order=27),
            ]
            db.session.bulk_save_objects(skills)
            print(f"Seeded {len(skills)} skills.")

        # 4. Seed Certifications (REAL certificates analyzed from C:\Users\Abhi Verma\OneDrive\Desktop\certificates)
        if Certificate.query.count() == 0:
            certs = [
                Certificate(
                    title="Smart India Hackathon 2025 – Internal Hackathon",
                    issuing_org="Ministry of Education (MoE's Innovation Cell, Govt. of India) & JMIETI",
                    issue_date="15th September 2025",
                    category="Hackathons",
                    credential_url="",
                    image_url="/static/images/certificates/IMG_20260823_193430_558@1938743533.jpg",
                    description="Participation Certificate awarded by the Ministry of Education's Innovation Cell and JMIETI Radaur for participating in the Internal Hackathon for Smart India Hackathon 2025 as part of Team TR-TECH."
                ),
                Certificate(
                    title="Smart India Hackathon 2024 – Internal Hackathon",
                    issuing_org="Ministry of Education (MoE's Innovation Cell, Govt. of India) & JMIETI",
                    issue_date="7th September 2024",
                    category="Hackathons",
                    credential_url="",
                    image_url="/static/images/certificates/IMG_20260823_193339_229@1900998934.jpg",
                    description="Participation Certificate awarded by the Ministry of Education's Innovation Cell and JMIETI Radaur for participating in the Internal Hackathon for Smart India Hackathon 2024 as part of Team ANALYTIX RANGERS."
                ),
                Certificate(
                    title="@HACKMoR 2026 Hackathon – Final Round Finalist",
                    issuing_org="Manav Rachna University & Goolean",
                    issue_date="19th – 20th February 2026",
                    category="Hackathons",
                    credential_url="",
                    image_url="/static/images/certificates/IMG_20260306_153254_328@-2030341558.jpg",
                    description="Certificate of Participation & Final Round Finalist for competing in the @HACKMoR 'Innovate More. Create More.' Hackathon organized by Manav Rachna University reaching the final evaluation stage."
                ),
                Certificate(
                    title="Drone Technology & Its Applications – Bootcamp",
                    issuing_org="National Institute of Technology (NIT) Kurukshetra & JMIETI (SwaYaan Project)",
                    issue_date="18th – 22nd November 2024",
                    category="Workshops",
                    credential_url="",
                    image_url="/static/images/certificates/IMG_20260823_193525_315@-2001326573.jpg",
                    description="Successfully completed the 5-day bootcamp 'Drone Technology and Its Application' under the NIT Kurukshetra Capacity Building project for Human Resource Development in Drone Technology."
                ),
                Certificate(
                    title="Additional Input Course – Web Development",
                    issuing_org="Jai Parkash Mukand Lal Innovative Engineering & Technology Institute (JMIETI)",
                    issue_date="Academic Year 2024–2025",
                    category="Web Development",
                    credential_url="",
                    image_url="/static/images/certificates/IMG_20260823_193329_425@-426141579.jpg",
                    description="Completed the Additional Input Technical Course in Web Development conducted by the CSE Department at JMIETI, Radaur."
                ),
                Certificate(
                    title="Industrial Visit & Software Workshop – Meander Software",
                    issuing_org="Meander Software",
                    issue_date="11th February 2025",
                    category="Workshops",
                    credential_url="",
                    image_url="/static/images/certificates/IMG_20260823_193348_874@385555536.jpg",
                    description="Certificate of Participation for attending the one-day industrial visit and software engineering training at Meander Software, organized by Dr. Sandeep Srivastava."
                ),
                Certificate(
                    title="Certificate of Appreciation – Technical Event (Oct 2024)",
                    issuing_org="JMIETI, Radaur (Affiliated to Kurukshetra University)",
                    issue_date="17th October 2024",
                    category="Other Certifications",
                    credential_url="",
                    image_url="/static/images/certificates/IMG_20260823_193421_678@1272564558.jpg",
                    description="Awarded by the Department of Computer Science & Engineering, JMIETI for distinguished performance and active participation in a departmental technical event."
                ),
                Certificate(
                    title="Certificate of Appreciation – Technical Club & Fest (Feb 2025)",
                    issuing_org="JMIETI, Radaur",
                    issue_date="28th February 2025",
                    category="Other Certifications",
                    credential_url="",
                    image_url="/static/images/certificates/IMG_20260823_193440_587@1827193960.jpg",
                    description="Recognized by JMIETI for commendable contributions and performance in technical club and college fest activities."
                ),
                Certificate(
                    title="Certificate of Appreciation – Engineering Department Activities",
                    issuing_org="JMIETI Radaur, Distt. Yamuna Nagar (Haryana)",
                    issue_date="Academic Year 2024–2025",
                    category="Other Certifications",
                    credential_url="",
                    image_url="/static/images/certificates/IMG_20260823_193516_796@167703922.jpg",
                    description="Certificate of Appreciation for outstanding involvement in CSE department events and academic activities at JMIETI."
                ),
                Certificate(
                    title="Certificate of Appreciation – Student Technical Initiative",
                    issuing_org="JMIETI, Radaur",
                    issue_date="Academic Year 2024–2025",
                    category="Other Certifications",
                    credential_url="",
                    image_url="/static/images/certificates/IMG_20260823_193401_403@-314437456.jpg",
                    description="Recognized for outstanding involvement in departmental technical activities and student workshops at JMIETI Radaur."
                ),
                Certificate(
                    title="Life Skill Development Fun Camp",
                    issuing_org="Samagra Shiksha Abhiyan (DPCSSA), Yamuna Nagar",
                    issue_date="6th – 10th January 2020",
                    category="Other Certifications",
                    credential_url="",
                    image_url="/static/images/certificates/IMG_20260823_193311_355@543489514.jpg",
                    description="Participated in the Life Skill Development Fun Camp held under Samagra Shiksha Abhiyan during winter vacation, focusing on personality development and leadership skills."
                ),
                Certificate(
                    title="Annual Sports Meet – Certificate of Appreciation",
                    issuing_org="S.D. Senior Secondary School, Jagadhri (Haryana)",
                    issue_date="Session 2022–2023",
                    category="Other Certifications",
                    credential_url="",
                    image_url="/static/images/certificates/IMG_20260823_193413_353@-575250517.jpg",
                    description="Certificate of appreciation from S.D. Senior Secondary School, Jagadhri for athletic participation and teamwork during the Annual Sports Meet."
                ),
            ]
            db.session.bulk_save_objects(certs)
            print(f"Seeded {len(certs)} real certificates.")

        # 5. Seed Blog Posts
        if BlogPost.query.count() == 0:
            posts = [
                BlogPost(
                    title="My Journey Learning Python: From Syntax to Data Structures",
                    slug="my-journey-learning-python",
                    excerpt="How I transitioned from basic C/C++ loops to the elegance of Pythonic idioms, list comprehensions, and building real-world automation scripts.",
                    content="""### The Beginning of My Python Journey

When I started my B.Tech in Computer Science with specialization in AI & ML, the first programming language taught was C. While C gave me an indispensable grasp over memory layout, pointers, and CPU execution models, stepping into **Python** felt like unleashing supercharged developer velocity.

```python
# The elegance of Pythonic data processing
data = [12, 45, 67, 89, 34, 90]
even_squares = [x**2 for x in data if x % 2 == 0]
print(f"Processed Squares: {even_squares}")
```

#### Key Milestones:
1. **Mastering Built-in Data Structures**: Understanding when to use `dict` hash maps vs `set` lookups vs tuple immutability.
2. **Object-Oriented Programming (OOP)**: Building modular classes, encapsulation, and custom exception handling.
3. **Transition to Data Science**: Once Python was second nature, jumping into NumPy vectors and Pandas DataFrames felt natural and exhilarating.

#### Advice for Fellow Beginners
Don't just watch tutorials—build mini-projects immediately. Whether it's an automated file sorter or a web scraper, solving concrete bugs will 10x your learning speed.""",
                    category="Python",
                    image_url="/static/images/blogs/blog_python.svg",
                    read_time="4 min read",
                    is_published=True
                ),
                BlogPost(
                    title="Understanding Machine Learning: A Beginner's Guide to Core Algorithms",
                    slug="understanding-machine-learning-guide",
                    excerpt="Demystifying Linear Regression, Logistic Regression, Decision Trees, and K-Means with intuitive visual analogies and mathematical intuition.",
                    content="""### What Really is Machine Learning?

At its core, Machine Learning is about **finding the mathematical function $f(X) \\approx y$ that maps input feature vectors to desired outputs** without hardcoding rule-based if-else branches.

#### 1. Linear & Logistic Regression
* **Linear Regression**: Fits a hyper-plane minimizing Mean Squared Error (MSE). Great for predicting continuous values like housing prices or athlete scores.
* **Logistic Regression**: Applies the Sigmoid activation function $\\sigma(z) = \\frac{1}{1 + e^{-z}}$ to compress values into probabilities between 0 and 1 for binary classification.

#### 2. Tree-Based Models (Decision Trees & Random Forests)
Decision trees greedily split feature dimensions based on **Gini Impurity** or **Information Gain (Entropy)**. They handle non-linear decision boundaries effortlessly and require minimal feature normalization.

#### 3. Unsupervised Clustering (K-Means)
Iteratively assigns data points to the nearest centroid and recomputes centroid locations until cluster inertia converges.

#### Takeaway
Never treat ML models as black boxes. Understand their loss functions, optimization techniques (SGD/Adam), and bias-variance trade-offs.""",
                    category="Machine Learning",
                    image_url="/static/images/blogs/blog_ml.svg",
                    read_time="6 min read",
                    is_published=True
                ),
                BlogPost(
                    title="How I Built My IPL Data Analysis Project: From Raw CSVs to Plotly Dashboards",
                    slug="how-i-built-ipl-data-analysis",
                    excerpt="A complete technical walkthrough on parsing 15+ years of ball-by-ball IPL match records, engineering player impact metrics, and building interactive web dashboards.",
                    content="""### Project Genesis

As an avid cricket follower and aspiring AI engineer, I wanted to explore real sports data beyond toy textbook examples. The Indian Premier League (IPL) dataset provided the perfect high-dimensional sandbox.

#### Pipeline Architecture
1. **Data Ingestion & Cleaning**: Reconciled name changes (e.g., Delhi Daredevils to Delhi Capitals), imputed missing run-out values, and structured ball-by-ball chronological orders.
2. **Feature Engineering**:
   * *Death-Overs Strike Rate* (Overs 16-20)
   * *Powerplay Bowling Economy* (Overs 1-6)
   * *Player Match Impact Score* combining boundaries, dot ball percentages, and milestone wickets.
3. **Interactive Visualization**: Leveraged Plotly graphs integrated within Streamlit and Flask for dynamic team comparison sliders.

```python
# Calculating Batter Impact Index
df['boundary_runs'] = (df['fours'] * 4) + (df['sixes'] * 6)
df['impact_index'] = (df['boundary_runs'] / df['total_runs']) * (df['strike_rate'] / 100)
```

#### Final Thoughts
Data storytelling is just as critical as data processing. Clean graphs with intuitive filters make raw numbers immediately comprehensible to stakeholders.""",
                    category="Data Analysis",
                    image_url="/static/images/blogs/blog_ipl.svg",
                    read_time="5 min read",
                    is_published=True
                ),
                BlogPost(
                    title="My First Hackathon Experience: Building an AI Traffic Simulator in 36 Hours",
                    slug="my-first-hackathon-experience",
                    excerpt="What participating in high-intensity collegiate hackathons taught me about rapid prototyping, git branching, team collaboration, and pitching under pressure.",
                    content="""### 36 Hours of Code, Coffee, and Innovation

Participating in my first major technical hackathon was one of the most intense and rewarding learning accelerators of my B.Tech journey.

#### The Problem Statement
Our team tackled urban railway congestion and dynamic junction bottleneck resolution. When trains arrive out of sequence, standard static timetables cascade into system-wide delays.

#### What We Built
We created **Train Traffic Control AI**, a real-time digital twin simulator that predicts collision paths and junction choke points, dynamically recalculating track assignments using heuristic optimization.

#### Key Lessons Learned:
* **Scope Discipline**: A working MVP with 2 polished features beats an ambitious idea with 10 broken endpoints.
* **Effective Team Git Workflow**: Frequent merges, feature branches, and clear API contracts avoid 3 AM merge hell.
* **The Pitch Matters**: Communicating *why* your solution matters to non-technical judges is 50% of winning.""",
                    category="Career",
                    image_url="/static/images/blogs/blog_hackathon.svg",
                    read_time="4 min read",
                    is_published=True
                ),
                BlogPost(
                    title="Learning Flask for Web Development: Why Micro-Frameworks are Perfect for AI Engineers",
                    slug="learning-flask-for-web-dev",
                    excerpt="Why Python developers building machine learning models should choose Flask for rapid prototyping, lightweight API design, and clean deployment.",
                    content="""### Why Flask for AI Engineers?

When you train a machine learning model or build an AI pipeline in Python, you eventually need to expose it through a web interface or REST API. That is where **Flask** shines brightest.

#### Advantages:
1. **Zero Bloat**: Unlike heavyweight frameworks with rigid ORMs and admin scaffolds, Flask gives you explicit control over your routes, request lifecycle, and folder layout.
2. **Seamless Model Inference**: Load PyTorch or Scikit-learn `.pkl` models directly into memory upon server initialization:

```python
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('career_model.pkl')

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = model.predict([data['features']])
    return jsonify({'recommended_role': prediction[0]})
```

3. **Jinja2 Templating Power**: Allows rendering dynamic HTML dashboards server-side with lightning performance.

Flask remains my go-to weapon for turning Python scripts into production-ready web tools.""",
                    category="Web Dev",
                    image_url="/static/images/blogs/blog_flask.svg",
                    read_time="5 min read",
                    is_published=True
                ),
                BlogPost(
                    title="My Roadmap Towards AI Engineering: Math, Code, and Production Systems",
                    slug="roadmap-towards-ai-engineering",
                    excerpt="A structured curriculum and methodology I follow as a B.Tech CSE (AI & ML) student preparing for the modern frontier of Artificial Intelligence.",
                    content="""### Navigating the AI & ML Landscape (2024–2028)

The field of Artificial Intelligence is evolving at unprecedented speed. As an undergraduate student specializing in AI & ML, I have structured my 4-year journey into four focused pillars:

#### Pillar 1: Mathematical Foundations
* Linear Algebra (Matrix decompositions, Eigenvalues, Vector spaces)
* Calculus (Multivariate gradients, Chain rule)
* Probability & Statistics (Bayesian inference, Hypothesis testing, Distributions)

#### Pillar 2: Core Machine Learning & Data Engineering
* Classical Algorithms: Supervised & Unsupervised ML with Scikit-learn
* High-performance data pipelines: Pandas, NumPy, Polars
* SQL query optimization and database schema modeling

#### Pillar 3: Deep Learning, NLP & Generative AI
* Neural Network architectures (CNNs, RNNs, Transformers, Attention mechanisms)
* PyTorch implementations and LLM fine-tuning / RAG pipelines

#### Pillar 4: Software Engineering & Production Deployment
* Full-stack web frameworks (Flask, FastAPI)
* Containerization (Docker), Git version control, and CI/CD pipelines

Building real projects at every stage is the only way to convert theoretical knowledge into durable engineering skill.""",
                    category="AI",
                    image_url="/static/images/blogs/blog_ai.svg",
                    read_time="7 min read",
                    is_published=True
                )
            ]
            db.session.bulk_save_objects(posts)
            print(f"Seeded {len(posts)} blog posts.")

        # 6. Seed Experiences & Timeline
        if Experience.query.count() == 0:
            experiences = [
                Experience(
                    title="B.Tech in Computer Science Engineering (AI & ML)",
                    organization="Engineering Institute / University",
                    role_type="Academic",
                    start_date="August 2024",
                    end_date="Expected 2028",
                    description="Pursuing undergraduate degree with specialization in Artificial Intelligence and Machine Learning. Focused on Data Structures, Algorithms, Mathematics for AI, and Software Engineering.",
                    location="India",
                    icon="fas fa-graduation-cap",
                    key_points="Specialization: Artificial Intelligence & Machine Learning\nCoursework: Data Structures & Algorithms, Python Programming, Object-Oriented Programming, Database Management Systems, Discrete Mathematics\nActive member of Coding & AI Technical Society\nConsistent academic performance with focus on practical projects"
                ),
                Experience(
                    title="Summer Training Intern - Python & Machine Learning",
                    organization="Apex AI & Data Analytics Labs",
                    role_type="Summer Training",
                    start_date="June 2025",
                    end_date="August 2025",
                    description="Completed intensive practical training in Python programming, exploratory data analysis, data visualization, and applied machine learning algorithm implementations.",
                    location="Remote / Hybrid",
                    icon="fas fa-certificate",
                    key_points="Gained hands-on expertise in Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn\nEngineered end-to-end IPL Data Analysis Dashboard project with interactive Streamlit visualizations\nImplemented supervised learning algorithms (Linear Regression, Logistic Regression, Decision Trees, KNN)\nCollaborated using Git and GitHub in a fast-paced team environment"
                ),
                Experience(
                    title="Technical Project Developer & Open Source Contributor",
                    organization="Self-Driven / GitHub",
                    role_type="Technical",
                    start_date="2024",
                    end_date="Present",
                    description="Designing and deploying full-stack web applications, AI tools, and data science projects to solve practical student and industry challenges.",
                    location="India",
                    icon="fas fa-laptop-code",
                    key_points="Developed 6+ full-stack and AI/ML applications including StudyLens AI and Train Traffic Control AI\nMaintained active GitHub portfolio with clean documentation and modular architecture\nAuthored technical tutorials on Python, Machine Learning, and Web Development"
                ),
                Experience(
                    title="Hackathon Participant & Finalist",
                    organization="Inter-College & National Hackathons",
                    role_type="Hackathon",
                    start_date="2024",
                    end_date="Present",
                    description="Collaborated in multidisciplinary teams under tight timeframes to engineer innovative AI solutions for real-world problem statements.",
                    location="India",
                    icon="fas fa-trophy",
                    key_points="Internal round participant for Smart India Hackathon proposing AI-based Railway Traffic Optimization\nFinal round finalist at Manav Rachna University @HACKMoR 2026 Hackathon\nDesigned rapid interactive prototypes and pitched technical architectures to judging panels"
                )
            ]
            db.session.bulk_save_objects(experiences)
            print(f"Seeded {len(experiences)} experiences.")

        # 7. Seed Hackathons
        if Hackathon.query.count() == 0:
            hackathons = [
                Hackathon(
                    title="AI Railway Traffic Control System",
                    event_name="Smart India Hackathon (Internal Round)",
                    event_date="January 2025",
                    problem_statement="Mitigating cascading railway junction delays and optimizing multi-train dispatch priority schedules during dynamic unexpected hold-ups.",
                    solution="Engineered an AI heuristic scheduling algorithm and interactive digital twin canvas dashboard that dynamically recalculates train junction routes to minimize cumulative wait time.",
                    tech_stack="Python, Flask, SimPy, WebSockets, HTML5 Canvas, Bootstrap",
                    role="Lead AI Algorithm & Backend Developer",
                    achievement="Official Team Participant / Internal Round Candidate",
                    image_url="/static/images/hackathons/sih.svg",
                    project_link="/projects/train-traffic-control-ai"
                ),
                Hackathon(
                    title="@HACKMoR 2026 Hackathon",
                    event_name="Manav Rachna University (@HACKMoR)",
                    event_date="February 2026",
                    problem_statement="Building innovative software applications to solve modern technological and community challenges under a high-intensity 36-hour sprint.",
                    solution="Engineered a rapid functional prototype, successfully qualifying through rigorous preliminary evaluation stages into the grand finale last round.",
                    tech_stack="Python, Flask, Modern Web, Rapid Prototyping",
                    role="Core Team Developer & Finalist",
                    achievement="Final Round Finalist (Grand Finale Candidate)",
                    image_url="/static/images/hackathons/hackai.svg",
                    project_link="#"
                ),
                Hackathon(
                    title="StudyLens AI - RAG Learning Assistant",
                    event_name="HackAI Student Innovation Challenge",
                    event_date="April 2025",
                    problem_statement="Helping students interactively parse dense research papers, PPTs, and textbook chapters through conversational AI with exact citations.",
                    solution="Built a full-stack RAG document ingestion tool with vector embedding retrieval and automated flashcard generation.",
                    tech_stack="Python, Flask, PyTorch, Transformers, SQLite, Bootstrap 5",
                    role="Full-Stack Developer & RAG Pipeline Engineer",
                    achievement="Top 5 Finalist & Best AI UX Award",
                    image_url="/static/images/hackathons/hackai.svg",
                    project_link="/projects/studylens-ai"
                )
            ]
            db.session.bulk_save_objects(hackathons)
            print(f"Seeded {len(hackathons)} hackathons.")

        db.session.commit()
        print("Database seeding completed successfully!")

if __name__ == '__main__':
    seed_database()
