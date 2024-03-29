"""empty message

Revision ID: 19c82f38f866
Revises: 58620b1264b9
Create Date: 2019-03-15 19:02:02.996305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19c82f38f866'
down_revision = '58620b1264b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('boxoffice', sa.Column('action_demand', sa.Integer(), nullable=True))
    op.add_column('boxoffice', sa.Column('comedy_demand', sa.Integer(), nullable=True))
    op.add_column('boxoffice', sa.Column('drama_demand', sa.Integer(), nullable=True))
    op.add_column('boxoffice', sa.Column('fantasy_demand', sa.Integer(), nullable=True))
    op.add_column('boxoffice', sa.Column('horror_demand', sa.Integer(), nullable=True))
    op.add_column('boxoffice', sa.Column('scifi_demand', sa.Integer(), nullable=True))
    op.add_column('boxoffice', sa.Column('superhero_demand', sa.Integer(), nullable=True))
    op.add_column('boxoffice', sa.Column('war_demand', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('boxoffice', 'war_demand')
    op.drop_column('boxoffice', 'superhero_demand')
    op.drop_column('boxoffice', 'scifi_demand')
    op.drop_column('boxoffice', 'horror_demand')
    op.drop_column('boxoffice', 'fantasy_demand')
    op.drop_column('boxoffice', 'drama_demand')
    op.drop_column('boxoffice', 'comedy_demand')
    op.drop_column('boxoffice', 'action_demand')
    # ### end Alembic commands ###
