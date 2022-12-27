"""create posts table

Revision ID: 66f420a081af
Revises: 
Create Date: 2022-12-27 10:17:31.448125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66f420a081af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, 
    primary_key=True), sa.Column('course', sa.String(), nullable=False))
    pass

def downgrade() -> None:
    op.drop_table('posts')
    pass
