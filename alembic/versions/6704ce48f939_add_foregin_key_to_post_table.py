"""add foregin key to post table

Revision ID: 6704ce48f939
Revises: 2ddc68208c63
Create Date: 2022-03-09 11:39:01.594320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6704ce48f939'
down_revision = '2ddc68208c63'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
