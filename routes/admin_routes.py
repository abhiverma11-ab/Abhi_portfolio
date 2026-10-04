from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import functools
import re
from models import AdminUser, Project, BlogPost, Certificate, Skill, ContactMessage
from database import db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    return re.sub(r'[-\s]+', '-', text)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'admin_user_id' not in session:
            flash('Please log in to access the admin panel.', 'warning')
            return redirect(url_for('admin.login'))
        return view(**kwargs)
    return wrapped_view


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if 'admin_user_id' in session:
        return redirect(url_for('admin.dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        
        user = AdminUser.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['admin_user_id'] = user.id
            session['admin_username'] = user.username
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid username or password.', 'danger')
            
    return render_template('admin/login.html')


@admin_bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('admin.login'))


@admin_bp.route('/')
@admin_bp.route('/dashboard')
@login_required
def dashboard():
    stats = {
        'projects_count': Project.query.count(),
        'blogs_count': BlogPost.query.count(),
        'certs_count': Certificate.query.count(),
        'skills_count': Skill.query.count(),
        'unread_messages': ContactMessage.query.filter_by(is_read=False).count(),
        'total_messages': ContactMessage.query.count()
    }
    recent_messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).limit(5).all()
    recent_projects = Project.query.order_by(Project.created_at.desc()).limit(5).all()
    return render_template('admin/dashboard.html', stats=stats, recent_messages=recent_messages, recent_projects=recent_projects)


# Projects CRUD
@admin_bp.route('/projects')
@login_required
def manage_projects():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template('admin/projects.html', projects=projects)


@admin_bp.route('/projects/new', methods=['GET', 'POST'])
@login_required
def add_project():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        subtitle = request.form.get('subtitle', '').strip()
        description = request.form.get('description', '').strip()
        problem_statement = request.form.get('problem_statement', '').strip()
        solution = request.form.get('solution', '').strip()
        architecture_desc = request.form.get('architecture_desc', '').strip()
        features = request.form.get('features', '').strip()
        challenges = request.form.get('challenges', '').strip()
        learnings = request.form.get('learnings', '').strip()
        technologies = request.form.get('technologies', '').strip()
        category = request.form.get('category', '').strip()
        image_url = request.form.get('image_url', '').strip() or '/static/images/project-placeholder.svg'
        github_link = request.form.get('github_link', '').strip()
        live_link = request.form.get('live_link', '').strip()
        is_featured = bool(request.form.get('is_featured'))

        slug = slugify(title)
        existing = Project.query.filter_by(slug=slug).first()
        if existing:
            slug = f"{slug}-{Project.query.count() + 1}"

        project = Project(
            title=title,
            slug=slug,
            subtitle=subtitle,
            description=description,
            problem_statement=problem_statement,
            solution=solution,
            architecture_desc=architecture_desc,
            features=features,
            challenges=challenges,
            learnings=learnings,
            technologies=technologies,
            category=category,
            image_url=image_url,
            github_link=github_link,
            live_link=live_link,
            is_featured=is_featured
        )
        db.session.add(project)
        db.session.commit()
        flash('Project created successfully!', 'success')
        return redirect(url_for('admin.manage_projects'))

    return render_template('admin/project_form.html', project=None, title="Add New Project")


@admin_bp.route('/projects/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_project(id):
    project = Project.query.get_or_404(id)
    if request.method == 'POST':
        project.title = request.form.get('title', '').strip()
        project.subtitle = request.form.get('subtitle', '').strip()
        project.description = request.form.get('description', '').strip()
        project.problem_statement = request.form.get('problem_statement', '').strip()
        project.solution = request.form.get('solution', '').strip()
        project.architecture_desc = request.form.get('architecture_desc', '').strip()
        project.features = request.form.get('features', '').strip()
        project.challenges = request.form.get('challenges', '').strip()
        project.learnings = request.form.get('learnings', '').strip()
        project.technologies = request.form.get('technologies', '').strip()
        project.category = request.form.get('category', '').strip()
        if request.form.get('image_url'):
            project.image_url = request.form.get('image_url').strip()
        project.github_link = request.form.get('github_link', '').strip()
        project.live_link = request.form.get('live_link', '').strip()
        project.is_featured = bool(request.form.get('is_featured'))

        db.session.commit()
        flash('Project updated successfully!', 'success')
        return redirect(url_for('admin.manage_projects'))

    return render_template('admin/project_form.html', project=project, title="Edit Project")


@admin_bp.route('/projects/<int:id>/delete', methods=['POST'])
@login_required
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    flash('Project deleted.', 'info')
    return redirect(url_for('admin.manage_projects'))


# Blogs CRUD
@admin_bp.route('/blogs')
@login_required
def manage_blogs():
    blogs = BlogPost.query.order_by(BlogPost.published_at.desc()).all()
    return render_template('admin/blogs.html', blogs=blogs)


@admin_bp.route('/blogs/new', methods=['GET', 'POST'])
@login_required
def add_blog():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        excerpt = request.form.get('excerpt', '').strip()
        content = request.form.get('content', '').strip()
        category = request.form.get('category', '').strip()
        image_url = request.form.get('image_url', '').strip() or '/static/images/blog-placeholder.svg'
        read_time = request.form.get('read_time', '5 min read').strip()
        is_published = bool(request.form.get('is_published'))

        slug = slugify(title)
        existing = BlogPost.query.filter_by(slug=slug).first()
        if existing:
            slug = f"{slug}-{BlogPost.query.count() + 1}"

        blog = BlogPost(
            title=title,
            slug=slug,
            excerpt=excerpt,
            content=content,
            category=category,
            image_url=image_url,
            read_time=read_time,
            is_published=is_published
        )
        db.session.add(blog)
        db.session.commit()
        flash('Blog post published!', 'success')
        return redirect(url_for('admin.manage_blogs'))

    return render_template('admin/blog_form.html', blog=None, title="Add Blog Post")


@admin_bp.route('/blogs/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_blog(id):
    blog = BlogPost.query.get_or_404(id)
    if request.method == 'POST':
        blog.title = request.form.get('title', '').strip()
        blog.excerpt = request.form.get('excerpt', '').strip()
        blog.content = request.form.get('content', '').strip()
        blog.category = request.form.get('category', '').strip()
        if request.form.get('image_url'):
            blog.image_url = request.form.get('image_url').strip()
        blog.read_time = request.form.get('read_time', '5 min read').strip()
        blog.is_published = bool(request.form.get('is_published'))

        db.session.commit()
        flash('Blog post updated!', 'success')
        return redirect(url_for('admin.manage_blogs'))

    return render_template('admin/blog_form.html', blog=blog, title="Edit Blog Post")


@admin_bp.route('/blogs/<int:id>/delete', methods=['POST'])
@login_required
def delete_blog(id):
    blog = BlogPost.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    flash('Blog post deleted.', 'info')
    return redirect(url_for('admin.manage_blogs'))


# Certificates CRUD
@admin_bp.route('/certificates')
@login_required
def manage_certificates():
    certs = Certificate.query.order_by(Certificate.id.desc()).all()
    return render_template('admin/certificates.html', certificates=certs)


@admin_bp.route('/certificates/new', methods=['GET', 'POST'])
@login_required
def add_certificate():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        issuing_org = request.form.get('issuing_org', '').strip()
        issue_date = request.form.get('issue_date', '').strip()
        category = request.form.get('category', '').strip()
        credential_url = request.form.get('credential_url', '').strip()
        image_url = request.form.get('image_url', '').strip() or '/static/images/certificate-placeholder.svg'
        description = request.form.get('description', '').strip()

        cert = Certificate(
            title=title,
            issuing_org=issuing_org,
            issue_date=issue_date,
            category=category,
            credential_url=credential_url,
            image_url=image_url,
            description=description
        )
        db.session.add(cert)
        db.session.commit()
        flash('Certificate added!', 'success')
        return redirect(url_for('admin.manage_certificates'))

    return render_template('admin/cert_form.html', cert=None, title="Add Certificate")


@admin_bp.route('/certificates/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_certificate(id):
    cert = Certificate.query.get_or_404(id)
    if request.method == 'POST':
        cert.title = request.form.get('title', '').strip()
        cert.issuing_org = request.form.get('issuing_org', '').strip()
        cert.issue_date = request.form.get('issue_date', '').strip()
        cert.category = request.form.get('category', '').strip()
        cert.credential_url = request.form.get('credential_url', '').strip()
        if request.form.get('image_url'):
            cert.image_url = request.form.get('image_url').strip()
        cert.description = request.form.get('description', '').strip()

        db.session.commit()
        flash('Certificate updated!', 'success')
        return redirect(url_for('admin.manage_certificates'))

    return render_template('admin/cert_form.html', cert=cert, title="Edit Certificate")


@admin_bp.route('/certificates/<int:id>/delete', methods=['POST'])
@login_required
def delete_certificate(id):
    cert = Certificate.query.get_or_404(id)
    db.session.delete(cert)
    db.session.commit()
    flash('Certificate deleted.', 'info')
    return redirect(url_for('admin.manage_certificates'))


# Skills CRUD
@admin_bp.route('/skills')
@login_required
def manage_skills():
    skills = Skill.query.order_by(Skill.display_order.asc()).all()
    return render_template('admin/skills.html', skills=skills)


@admin_bp.route('/skills/new', methods=['GET', 'POST'])
@login_required
def add_skill():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        category = request.form.get('category', '').strip()
        proficiency = int(request.form.get('proficiency', 80))
        icon_class = request.form.get('icon_class', 'fas fa-code').strip()
        badge_color = request.form.get('badge_color', 'primary').strip()
        display_order = int(request.form.get('display_order', 0))

        skill = Skill(
            name=name,
            category=category,
            proficiency=proficiency,
            icon_class=icon_class,
            badge_color=badge_color,
            display_order=display_order
        )
        db.session.add(skill)
        db.session.commit()
        flash('Skill added!', 'success')
        return redirect(url_for('admin.manage_skills'))

    return render_template('admin/skill_form.html', skill=None, title="Add Skill")


@admin_bp.route('/skills/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_skill(id):
    skill = Skill.query.get_or_404(id)
    if request.method == 'POST':
        skill.name = request.form.get('name', '').strip()
        skill.category = request.form.get('category', '').strip()
        skill.proficiency = int(request.form.get('proficiency', 80))
        skill.icon_class = request.form.get('icon_class', 'fas fa-code').strip()
        skill.badge_color = request.form.get('badge_color', 'primary').strip()
        skill.display_order = int(request.form.get('display_order', 0))

        db.session.commit()
        flash('Skill updated!', 'success')
        return redirect(url_for('admin.manage_skills'))

    return render_template('admin/skill_form.html', skill=skill, title="Edit Skill")


@admin_bp.route('/skills/<int:id>/delete', methods=['POST'])
@login_required
def delete_skill(id):
    skill = Skill.query.get_or_404(id)
    db.session.delete(skill)
    db.session.commit()
    flash('Skill deleted.', 'info')
    return redirect(url_for('admin.manage_skills'))


# Messages Management
@admin_bp.route('/messages')
@login_required
def manage_messages():
    messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()
    return render_template('admin/messages.html', messages=messages)


@admin_bp.route('/messages/<int:id>/toggle-read', methods=['POST'])
@login_required
def toggle_message_read(id):
    msg = ContactMessage.query.get_or_404(id)
    msg.is_read = not msg.is_read
    db.session.commit()
    return redirect(url_for('admin.manage_messages'))


@admin_bp.route('/messages/<int:id>/delete', methods=['POST'])
@login_required
def delete_message(id):
    msg = ContactMessage.query.get_or_404(id)
    db.session.delete(msg)
    db.session.commit()
    flash('Message deleted.', 'info')
    return redirect(url_for('admin.manage_messages'))
