"""vote tabel

Revision ID: 03b466e896b7
Revises: d3851067b0e3
Create Date: 2022-03-10 10:50:56.794799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03b466e896b7'
down_revision = 'd3851067b0e3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    pass


def downgrade():
    op.drop_table('votes')
    pass
