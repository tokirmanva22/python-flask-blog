"""Made email in User model indexed

Revision ID: 79fe69aa8d0e
Revises: e0cf84cc2bb8
Create Date: 2018-10-15 15:48:17.443723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79fe69aa8d0e'
down_revision = 'e0cf84cc2bb8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    # ### end Alembic commands ###
