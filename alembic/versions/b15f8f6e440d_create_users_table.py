"""create users table

Revision ID: b15f8f6e440d
Revises: 66f420a081af
Create Date: 2022-12-27 10:22:15.262777

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b15f8f6e440d'
down_revision = '66f420a081af'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
    server_default=sa.text('now()'), nullable=False), 
    sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('email'))
    pass

def downgrade() -> None:
    op.drop_table('users')
    pass
