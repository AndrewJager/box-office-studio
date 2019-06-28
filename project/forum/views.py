from flask import render_template, Blueprint, request
from flask_login import current_user

from project.models import BoxOffice, ForumSection
from project import db

forum_blueprint = Blueprint(
    'forum', __name__,
    template_folder = 'templates'
)

@forum_blueprint.route('/forum', methods=['GET', 'POST'])
def forum():
    system = BoxOffice.query.first()

    if request.method == 'POST':
        if request.form['submit_button'] == 'Add section':
            newSection = ForumSection(request.form['newName'])
            db.session.add(newSection)
            db.session.commit()

    sections = ForumSection.query.all()

    return render_template('forum.html', system=system, user=current_user, sections=sections)