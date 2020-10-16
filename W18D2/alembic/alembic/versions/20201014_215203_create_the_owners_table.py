"""create the owners table

Revision ID: 6dc3a5b86fed
Revises:
Create Date: 2020-10-14 21:52:03.963495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6dc3a5b86fed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "owners",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("first_name", sa.String(50), nullable=False),
        sa.Column("last_name", sa.String(50), nullable=False),
        sa.Column("email", sa.String(255), nullable=False),
    )


def downgrade():
    op.drop_table("owners")
