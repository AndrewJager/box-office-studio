"""empty message

Revision ID: 270947efbfd8
Revises: 19c82f38f866
Create Date: 2019-03-15 19:15:04.944062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '270947efbfd8'
down_revision = '19c82f38f866'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('movie_1', sa.String(), nullable=True),
    sa.Column('movie_1_results', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('results')
    # ### end Alembic commands ###