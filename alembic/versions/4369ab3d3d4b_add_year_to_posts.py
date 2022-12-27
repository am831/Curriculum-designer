"""add year and month to posts

Revision ID: 4369ab3d3d4b
Revises: 2da46904f575
Create Date: 2022-12-27 10:40:38.956295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4369ab3d3d4b'
down_revision = '2da46904f575'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.add_column('posts', sa.Column('year', sa.Integer(), nullable=False))
    pass

def downgrade() -> None:
    op.drop_column('posts', 'year')
    pass
