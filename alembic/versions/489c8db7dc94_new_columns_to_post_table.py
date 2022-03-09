"""new_columns_to_post_table

Revision ID: 489c8db7dc94
Revises: 1fe78c18b9cf
Create Date: 2022-03-09 11:25:12.474282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '489c8db7dc94'
down_revision = '1fe78c18b9cf'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
