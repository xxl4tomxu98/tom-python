"""create the ponies table

Revision ID: e4a07cccf6a0
Revises: 6dc3a5b86fed
Create Date: 2020-10-14 21:55:51.288021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4a07cccf6a0'
down_revision = '6dc3a5b86fed'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "ponies",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("breed", sa.String(20), nullable=False),
        sa.Column("birth_year", sa.Integer, nullable=False),
        sa.Column("owner_id",
                  sa.Integer,
                  sa.ForeignKey("owners.id"),
                  nullable=False)
    )


def downgrade():
    op.drop_table("ponies")
