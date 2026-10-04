from flask import Blueprint, request, jsonify
from models import Project, Skill, ContactMessage
from database import db

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/contact', methods=['POST'])
def api_contact():
    data = request.get_json() or {}
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    subject = data.get('subject', '').strip()
    message = data.get('message', '').strip()

    if not name or not email or not subject or not message:
        return jsonify({'success': False, 'error': 'All fields are required.'}), 400

    contact_msg = ContactMessage(name=name, email=email, subject=subject, message=message)
    db.session.add(contact_msg)
    db.session.commit()

    return jsonify({
        'success': True,
        'message': 'Thank you! Your message has been sent successfully. Abhi will contact you soon.'
    }), 201

@api_bp.route('/projects/filter')
def api_projects_filter():
    category = request.args.get('category', 'All')
    query = Project.query
    if category != 'All':
        query = query.filter_by(category=category)
    
    projects = query.order_by(Project.created_at.desc()).all()
    
    results = []
    for p in projects:
        results.append({
            'id': p.id,
            'title': p.title,
            'slug': p.slug,
            'subtitle': p.subtitle,
            'description': p.description,
            'technologies': p.tech_list(),
            'category': p.category,
            'image_url': p.image_url,
            'github_link': p.github_link,
            'live_link': p.live_link,
            'is_featured': p.is_featured
        })
    return jsonify({'projects': results})
