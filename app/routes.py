from flask import render_template, request, url_for, redirect, flash
from app import app, db
from app.forms import TodoForm
from app.models import ToDo
from sqlalchemy_utils.functions import database_exists

@app.route('/index', methods=['GET', 'POST'])
def index():
    form = TodoForm()
    if request.method == 'GET':
        if database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
            if ToDo.query.filter_by().count() > 0:
                check = 1
                return render_template('index.html', check=check, form=form)
        else:
            return render_template('index.html',form=form)
    if form.validate_on_submit():
        to_do_task = ToDo(task=form.task.data)
        db.session.add(to_do_task)
        db.session.commit()
        return redirect(url_for('todolist'))
    return render_template('index.html',form=form)


@app.route('/to-do-list', methods=['GET', 'POST'])
def todolist():
    page = request.args.get('page', 1, type=int)
    pagination = ToDo.query.order_by(ToDo.timestamp.desc()).paginate(
        page, app.config['LIST_ITEMS_PER_PAGE'], False)
    next_url = url_for('todolist', page=pagination.next_num) \
        if pagination.has_next else None
    prev_url = url_for('todolist', page=pagination.prev_num) \
        if pagination.has_prev else None
    return render_template('todolist.html', pagination=pagination, next_url=next_url,
                            prev_url=prev_url)


@app.route('/delete_task', methods=['GET','POST'])
def delete_task():
    received_data = request.values
    task_id = received_data.get('param')
    print(task_id)
    task = ToDo.query.filter_by(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('todolist'))
