from flask import Blueprint

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/')
def user_dashboard():
    return "User Dashboard"
