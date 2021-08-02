from flask import Blueprint, render_template, request, g
from flask.helpers import url_for
from gstore.models import Order
from gstore import db
from datetime import datetime
from werkzeug.utils import redirect
from gstore.views.auth_views import login_required

bp = Blueprint('buy',__name__, url_prefix='/buy')

@bp.route('/')
@bp.route('/<int:num>')
@login_required
def inputTest(num=None):
    return render_template('buy/buy.html', num=num)

@bp.route('/calculate',methods=['POST'])
@login_required
def calculate(num=None):
    # form = OrderForm()
    if request.method == 'POST':
        temp = request.form['num']
        #  if문 쿼리 request.get / else 
        #  try문
        new_order = Order(product_id=int(temp), user_id= "master", order_date=datetime.now())
        db.session.add(new_order)
        db.session.commit()
        return redirect(url_for('buy.inputTest',num=temp))
    return redirect(url_for('buy.inputTest',num=num))


@bp.route('/test/')
@bp.route('/test/<int:num>')
def inputTest1(num=None):
    return render_template('buy/count.html', num=num)

@bp.route('/test/cal',methods=['POST'])
def cal(num=None):
    if request.method == 'POST':
        n = request.form['num']
    else:
        n = None
    return redirect(url_for('buy.inputTest1', num=n))





