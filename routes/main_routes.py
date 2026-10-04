from flask import Blueprint, render_template, request, flash, redirect, url_for, abort, send_file
import os
from models import Project, BlogPost, Certificate, Skill, Experience, Hackathon, ContactMessage
from database import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/download-project')
def download_project():
    zip_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'downloads', 'abhi_verma_portfolio.zip')
    if os.path.exists(zip_path):
        return send_file(zip_path, as_attachment=True, download_name='abhi_verma_portfolio.zip')
    fallback_zip = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'abhi_verma_portfolio.zip')
    if os.path.exists(fallback_zip):
        return send_file(fallback_zip, as_attachment=True, download_name='abhi_verma_portfolio.zip')
    flash('Download file is being generated. Please try again in a moment.', 'info')
    return redirect(url_for('main.index'))

@main_bp.route('/download-resume')
def download_resume():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    possible_paths = [
        os.path.join(base_dir, 'static', 'downloads', 'Abhi_Verma_Resume.pdf'),
        os.path.join(base_dir, 'static', 'downloads', 'ABHI_VERMA.pdf'),
        r'C:\Users\Abhi Verma\OneDrive\Desktop\ABHI VERMA.pdf',
        r'C:\Users\Abhi Verma\Downloads\Abhi_Verma_Resume.pdf'
    ]
    for p in possible_paths:
        if os.path.exists(p):
            return send_file(p, as_attachment=True, download_name='Abhi_Verma_Resume.pdf')
    flash('Resume file not found. Please contact Abhi directly via the contact form.', 'warning')
    return redirect(url_for('main.resume'))


@main_bp.route('/')
def index():
    featured_projects = Project.query.filter_by(is_featured=True).order_by(Project.id.asc()).limit(4).all()
    skills = Skill.query.order_by(Skill.display_order.asc()).limit(12).all()
    recent_blogs = BlogPost.query.filter_by(is_published=True).order_by(BlogPost.published_at.desc()).limit(3).all()
    certificates = Certificate.query.order_by(Certificate.id.asc()).limit(4).all()
    hackathons = Hackathon.query.order_by(Hackathon.id.asc()).limit(3).all()
    stats = {
        'projects_count': Project.query.count(),
        'skills_count': Skill.query.count(),
        'certificates_count': Certificate.query.count(),
        'blogs_count': BlogPost.query.count()
    }
    return render_template('index.html',
                           featured_projects=featured_projects,
                           skills=skills,
                           recent_blogs=recent_blogs,
                           certificates=certificates,
                           hackathons=hackathons,
                           stats=stats)

@main_bp.route('/about')
def about():
    experiences = Experience.query.order_by(Experience.id.asc()).all()
    stats = {
        'projects_completed': 10,
        'tech_learned': 18,
        'training_completed': 1,
        'github_repos': 15
    }
    return render_template('about.html', experiences=experiences, stats=stats)

@main_bp.route('/skills')
def skills():
    all_skills = Skill.query.order_by(Skill.display_order.asc()).all()
    categories = {}
    for skill in all_skills:
        categories.setdefault(skill.category, []).append(skill)
    return render_template('skills.html', categories=categories, all_skills=all_skills)

@main_bp.route('/projects')
def projects():
    selected_category = request.args.get('category', 'All')
    if selected_category and selected_category != 'All':
        all_projects = Project.query.filter_by(category=selected_category).order_by(Project.created_at.desc()).all()
    else:
        all_projects = Project.query.order_by(Project.created_at.desc()).all()
    
    categories = ['All', 'Python', 'Machine Learning', 'Data Analysis', 'Web Development', 'AI']
    return render_template('projects.html', projects=all_projects, categories=categories, selected_category=selected_category)

@main_bp.route('/projects/<slug>')
def project_detail(slug):
    project = Project.query.filter_by(slug=slug).first_or_404()
    related_projects = Project.query.filter(Project.id != project.id, Project.category == project.category).limit(2).all()
    if not related_projects:
        related_projects = Project.query.filter(Project.id != project.id).limit(2).all()
    return render_template('project_detail.html', project=project, related_projects=related_projects)

@main_bp.route('/summer-training')
def summer_training():
    training_exp = Experience.query.filter_by(role_type='Summer Training').first()
    training_cert = Certificate.query.filter_by(category='Training').first()
    training_project = Project.query.filter_by(slug='ipl-data-analysis-dashboard').first()
    return render_template('summer_training.html',
                           training_exp=training_exp,
                           training_cert=training_cert,
                           training_project=training_project)

@main_bp.route('/experience')
def experience():
    experiences = Experience.query.order_by(Experience.id.asc()).all()
    return render_template('experience.html', experiences=experiences)

@main_bp.route('/certifications')
def certifications():
    selected_category = request.args.get('category', 'All')
    if selected_category and selected_category != 'All':
        certs = Certificate.query.filter_by(category=selected_category).order_by(Certificate.id.asc()).all()
    else:
        certs = Certificate.query.order_by(Certificate.id.asc()).all()
    
    # Categories based on real certificates
    categories = ['All', 'Hackathons', 'Web Development', 'Workshops', 'Summer Training', 'Other Certifications']
    return render_template('certifications.html', certificates=certs, categories=categories, selected_category=selected_category)

@main_bp.route('/hackathons')
def hackathons():
    all_hackathons = Hackathon.query.order_by(Hackathon.id.asc()).all()
    return render_template('hackathons.html', hackathons=all_hackathons)

@main_bp.route('/resume')
def resume():
    skills = Skill.query.order_by(Skill.proficiency.desc()).all()
    projects = Project.query.filter_by(is_featured=True).all()
    experiences = Experience.query.all()
    certificates = Certificate.query.all()
    return render_template('resume.html', skills=skills, projects=projects, experiences=experiences, certificates=certificates)

@main_bp.route('/blog')
def blog():
    selected_category = request.args.get('category', 'All')
    search_query = request.args.get('q', '').strip()

    query = BlogPost.query.filter_by(is_published=True)
    if selected_category and selected_category != 'All':
        query = query.filter_by(category=selected_category)
    if search_query:
        query = query.filter(BlogPost.title.ilike(f'%{search_query}%') | BlogPost.excerpt.ilike(f'%{search_query}%'))
    
    posts = query.order_by(BlogPost.published_at.desc()).all()
    categories = ['All', 'Python', 'Machine Learning', 'Data Analysis', 'Web Dev', 'AI', 'Career']
    return render_template('blog.html', posts=posts, categories=categories, selected_category=selected_category, search_query=search_query)

@main_bp.route('/blog/<slug>')
def blog_detail(slug):
    post = BlogPost.query.filter_by(slug=slug, is_published=True).first_or_404()
    recent_posts = BlogPost.query.filter(BlogPost.id != post.id, BlogPost.is_published == True).order_by(BlogPost.published_at.desc()).limit(3).all()
    return render_template('blog_detail.html', post=post, recent_posts=recent_posts)

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()

        if not name or not email or not subject or not message:
            flash('Please fill in all required fields.', 'danger')
            return render_template('contact.html', name=name, email=email, subject=subject, message=message)
        
        # Save to database
        contact_msg = ContactMessage(name=name, email=email, subject=subject, message=message)
        db.session.add(contact_msg)
        db.session.commit()

        flash('Thank you, your message has been received! Abhi will get back to you shortly.', 'success')
        return redirect(url_for('main.contact'))

    return render_template('contact.html')
