from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from database import db

class AdminUser(db.Model):
    __tablename__ = 'admin_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(150), unique=True, nullable=False)
    subtitle = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=False)
    problem_statement = db.Column(db.Text, nullable=True)
    solution = db.Column(db.Text, nullable=True)
    architecture_desc = db.Column(db.Text, nullable=True)
    features = db.Column(db.Text, nullable=True)  # JSON or newline-separated
    challenges = db.Column(db.Text, nullable=True)
    learnings = db.Column(db.Text, nullable=True)
    technologies = db.Column(db.String(300), nullable=False)  # comma separated
    category = db.Column(db.String(80), nullable=False)  # Python, Machine Learning, Data Analysis, Web Development, AI
    image_url = db.Column(db.String(255), default='/static/images/project-placeholder.svg')
    github_link = db.Column(db.String(255), nullable=True)
    live_link = db.Column(db.String(255), nullable=True)
    is_featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def tech_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]

    def feature_list(self):
        if not self.features:
            return []
        return [f.strip() for f in self.features.split('\n') if f.strip()]


class BlogPost(db.Model):
    __tablename__ = 'blog_posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    excerpt = db.Column(db.String(350), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(80), nullable=False)  # AI, Python, Web Dev, Machine Learning, Career
    image_url = db.Column(db.String(255), default='/static/images/blog-placeholder.svg')
    read_time = db.Column(db.String(30), default='5 min read')
    published_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_published = db.Column(db.Boolean, default=True)


class Certificate(db.Model):
    __tablename__ = 'certificates'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    issuing_org = db.Column(db.String(150), nullable=False)
    issue_date = db.Column(db.String(60), nullable=False)
    category = db.Column(db.String(80), nullable=False)  # Programming, Python, Machine Learning, Web Development, Training, Hackathons
    credential_url = db.Column(db.String(255), nullable=True)
    image_url = db.Column(db.String(255), default='/static/images/certificate-placeholder.svg')
    description = db.Column(db.Text, nullable=True)


class Skill(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(80), nullable=False)  # Programming Languages, Python & Data Science, Web Development, Machine Learning, Tools & Platforms
    proficiency = db.Column(db.Integer, nullable=False)  # 0 - 100
    icon_class = db.Column(db.String(100), default='fas fa-code')
    badge_color = db.Column(db.String(40), default='primary')
    display_order = db.Column(db.Integer, default=0)


class ContactMessage(db.Model):
    __tablename__ = 'contact_messages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Experience(db.Model):
    __tablename__ = 'experiences'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    organization = db.Column(db.String(150), nullable=False)
    role_type = db.Column(db.String(80), nullable=False)  # Summer Training, Academic, Leadership, Technical
    start_date = db.Column(db.String(60), nullable=False)
    end_date = db.Column(db.String(60), default='Present')
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=True)
    icon = db.Column(db.String(100), default='fas fa-briefcase')
    key_points = db.Column(db.Text, nullable=True)  # Newline separated

    def points_list(self):
        if not self.key_points:
            return []
        return [p.strip() for p in self.key_points.split('\n') if p.strip()]


class Hackathon(db.Model):
    __tablename__ = 'hackathons'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    event_name = db.Column(db.String(150), nullable=False)
    event_date = db.Column(db.String(60), nullable=False)
    problem_statement = db.Column(db.Text, nullable=False)
    solution = db.Column(db.Text, nullable=False)
    tech_stack = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(150), nullable=False)
    achievement = db.Column(db.String(150), nullable=False)
    image_url = db.Column(db.String(255), default='/static/images/hackathon-placeholder.svg')
    project_link = db.Column(db.String(255), nullable=True)
