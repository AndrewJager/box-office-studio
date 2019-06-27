from flask import render_template, Blueprint
from flask_login import current_user

from project.models import BoxOffice

forum_blueprint = Blueprint(
    'forum', __name__,
    template_folder = 'templates'
)

@forum_blueprint.route('/forum')
def forum():
    system = BoxOffice.query.first()

    return render_template('forum.html', system=system, user=current_user)