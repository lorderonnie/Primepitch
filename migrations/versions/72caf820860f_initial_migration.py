"""Initial Migration

Revision ID: 72caf820860f
Revises: 079262a1c024
Create Date: 2019-11-25 17:57:27.368740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72caf820860f'
down_revision = '079262a1c024'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('body', sa.String(length=255), nullable=True),
    sa.Column('user', sa.String(length=200), nullable=True),
    sa.Column('category', sa.String(length=200), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pitch')
    # ### end Alembic commands ###
