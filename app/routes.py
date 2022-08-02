from flask import Blueprint, render_template, request, url_for, redirect, flash, current_app
from app.extensions import  db
from app.forms import TodoForm
from app.models import ToDo

bp = Blueprint("bp", __name__)


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = TodoForm()

    if request.method == 'POST' and form.validate_on_submit():
        to_do_task = ToDo(task=form.task.data)
        db.session.add(to_do_task)
        db.session.commit()
        return redirect(url_for('bp.todolist'))

    if ToDo.query.filter_by().count() > 0:
        return render_template('index.html', todo_exists=True, form=form)
    else:
        return render_template('index.html', todo_exists=False, form=form)


@bp.route('/to-do-list', methods=['GET', 'POST'])
def todolist():
    page = request.args.get('page', 1, type=int)

    pagination = ToDo.query.order_by(ToDo.timestamp.desc()).paginate(
        page, current_app.config['LIST_ITEMS_PER_PAGE'], False)

    next_url = url_for('bp.todolist', page=pagination.next_num) \
        if pagination.has_next else None
    prev_url = url_for('bp.todolist', page=pagination.prev_num) \
        if pagination.has_prev else None

    return render_template('todolist.html', pagination=pagination, next_url=next_url,
                            prev_url=prev_url)


@bp.route('/delete_task/<task_id>')
def delete_task(task_id):
    task = ToDo.query.get(task_id)

    if not task:
        return redirect(url_for('bp.todolist'))

    try:    
        db.session.delete(task)
    except Exception as e:
        print('Something happened with db session/connection...')
        print(e)
        db.session.rollback()
    else:
        db.session.commit()

    return redirect(url_for('bp.todolist'))


@bp.route('/edit_task/<task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    form = TodoForm()
    task = ToDo.query.get(task_id)
    
    if not task:
        return redirect(url_for('index'))

    if request.method == 'GET':
        return render_template('edit_task.html', form=form)

    if form.validate_on_submit():
        task.task = form.task.data
        db.session.commit()
        return redirect(url_for('bp.todolist'))