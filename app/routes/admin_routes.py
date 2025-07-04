from flask import Blueprint
from flask_login import login_required, current_user
from flask import redirect, url_for

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        return redirect(url_for('user.user_dashboard'))
    return "Admin Dashboard"

