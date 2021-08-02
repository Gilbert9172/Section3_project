from flask import Blueprint, render_template, redirect, request
from flask.helpers import url_for
from gstore.views.auth_views import login_required

bp = Blueprint('main', __name__, url_prefix='/')

# 기본 페이지
@bp.route('/')
@login_required
def go_home():
    return render_template('index.html')

# usl_for('블루프린트 이름. 블루프린트에 등록 된 함수명)
@bp.route('/list')
def index():
    return redirect(url_for('question.lst'))


