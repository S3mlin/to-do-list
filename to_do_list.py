from app import create_app
from app.models import ToDo

app = create_app("Config")

from app.extensions import db


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'ToDo': ToDo}