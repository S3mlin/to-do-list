"""empty message

Revision ID: 51722d101ce6
Revises: acc7bd194a28
Create Date: 2022-07-29 00:01:53.774713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51722d101ce6'
down_revision = 'acc7bd194a28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_to_do_task', table_name='to_do')
    op.drop_index('ix_to_do_timestamp', table_name='to_do')
    op.drop_table('to_do')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('to_do',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('task', sa.VARCHAR(length=120), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_to_do_timestamp', 'to_do', ['timestamp'], unique=False)
    op.create_index('ix_to_do_task', 'to_do', ['task'], unique=False)
    # ### end Alembic commands ###
