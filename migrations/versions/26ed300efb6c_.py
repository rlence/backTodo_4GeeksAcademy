"""empty message

Revision ID: 26ed300efb6c
Revises: 8be69ab30b6c
Create Date: 2020-10-15 11:36:49.855563

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '26ed300efb6c'
down_revision = '8be69ab30b6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('todo', sa.String(length=200), nullable=False))
    op.drop_index('email', table_name='user')
    op.drop_column('user', 'email')
    op.drop_column('user', 'password')
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('password', mysql.VARCHAR(length=80), nullable=False))
    op.add_column('user', sa.Column('email', mysql.VARCHAR(length=120), nullable=False))
    op.create_index('email', 'user', ['email'], unique=True)
    op.drop_column('user', 'todo')
    # ### end Alembic commands ###
