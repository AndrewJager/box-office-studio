"""empty message

Revision ID: 4e00adb79c78
Revises: 33b3273b47f9
Create Date: 2019-05-25 19:42:34.975717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e00adb79c78'
down_revision = '33b3273b47f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('china_gross', sa.Integer(), nullable=False))
    op.add_column('movies', sa.Column('dom_gross', sa.Integer(), nullable=False))
    op.add_column('movies', sa.Column('int_gross', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movies', 'int_gross')
    op.drop_column('movies', 'dom_gross')
    op.drop_column('movies', 'china_gross')
    # ### end Alembic commands ###
