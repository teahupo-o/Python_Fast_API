"""New entry

Revision ID: 93e7046a2ee1
Revises: ce5f775e40da
Create Date: 2025-01-24 04:49:20.271881

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93e7046a2ee1'
down_revision: Union[str, None] = 'ce5f775e40da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
