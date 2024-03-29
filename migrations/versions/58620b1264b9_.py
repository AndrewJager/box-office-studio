"""empty message

Revision ID: 58620b1264b9
Revises: 28d5fdd3d25b
Create Date: 2019-03-12 22:29:34.902824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58620b1264b9'
down_revision = '28d5fdd3d25b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
