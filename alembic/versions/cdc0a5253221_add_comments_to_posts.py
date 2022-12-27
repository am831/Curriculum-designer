"""add comments to posts

Revision ID: cdc0a5253221
Revises: 4369ab3d3d4b
Create Date: 2022-12-27 12:39:25.623695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdc0a5253221'
down_revision = '4369ab3d3d4b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('comments', sa.String(), nullable=True))
    pass

def downgrade() -> None:
    op.drop_column('posts', 'year')
    pass
