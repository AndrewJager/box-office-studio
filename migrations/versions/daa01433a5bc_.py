"""empty message

Revision ID: daa01433a5bc
Revises: f07b1721c394
Create Date: 2019-03-10 21:00:14.827314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'daa01433a5bc'
down_revision = 'f07b1721c394'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('isAdmin', sa.Boolean(), nullable=False, server_default='False'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'isAdmin')
    # ### end Alembic commands ###
