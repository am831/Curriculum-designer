"""add columns to posts

Revision ID: 2da46904f575
Revises: b15f8f6e440d
Create Date: 2022-12-27 10:22:58.635497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2da46904f575'
down_revision = 'b15f8f6e440d'
branch_labels = None
depends_on = None

"add columns to posts"
def upgrade() -> None:
    op.add_column('posts', sa.Column('duration', sa.String(), nullable=True))
    op.add_column('posts', sa.Column('effort', sa.String(), nullable=True))
    op.add_column('posts', sa.Column('link', sa.String(), nullable=True))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
    nullable=False, server_default=sa.text('NOW()')),)
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", 
    referent_table="users", local_cols=['owner_id'], remote_cols=['id'], 
    ondelete="CASCADE")
    pass

def downgrade() -> None:
    op.drop_column('posts', 'effort')
    op.drop_column('posts', 'created_at')
    op.drop_column('posts', 'link')
    op.drop_column('posts', 'content')
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass