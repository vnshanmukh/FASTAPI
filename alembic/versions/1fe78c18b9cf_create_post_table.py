"""create_post_table

Revision ID: 1fe78c18b9cf
Revises: 
Create Date: 2022-03-08 17:49:39.151866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fe78c18b9cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False),sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
