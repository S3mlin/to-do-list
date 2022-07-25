"""list items

Revision ID: caeeb743ae60
Revises: d8e480ac4fcb
Create Date: 2022-07-26 00:15:27.144903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'caeeb743ae60'
down_revision = 'd8e480ac4fcb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('to_do',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_to_do_task'), 'to_do', ['task'], unique=True)
    op.drop_index('ix_to_do_list_task', table_name='to_do_list')
    op.drop_table('to_do_list')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('to_do_list',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('task', sa.VARCHAR(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_to_do_list_task', 'to_do_list', ['task'], unique=False)
    op.drop_index(op.f('ix_to_do_task'), table_name='to_do')
    op.drop_table('to_do')
    # ### end Alembic commands ###
