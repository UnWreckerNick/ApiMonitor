"""Initial migration
Revision ID: 001_initial_migration
Revises: 2024-12-28 00:00:00.000000
"""

from alembic import op
import sqlalchemy as sa
from datetime import datetime, timezone


revision = '001_initial_migration'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=True),
        sa.Column('is_superuser', sa.Boolean(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)

    op.create_table(
        'endpoints',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('url', sa.String(), nullable=False),
        sa.Column('method', sa.String(), nullable=False),
        sa.Column('headers', sa.String(), nullable=True),
        sa.Column('check_interval', sa.Interval(), nullable=False),
        sa.Column('expected_status_code', sa.Integer(), nullable=True),
        sa.Column('timeout', sa.Integer(), nullable=True),
        sa.Column('retry_count', sa.Integer(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_endpoints_id'), 'endpoints', ['id'], unique=False)

    op.create_table(
        'checks',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('endpoint_id', sa.Integer(), nullable=False),
        sa.Column('timestamp', sa.DateTime(timezone=True), nullable=False),
        sa.Column('response_time', sa.Float(), nullable=True),
        sa.Column('status_code', sa.Integer(), nullable=True),
        sa.Column('error_message', sa.String(), nullable=True),
        sa.Column('is_successful', sa.Boolean(), nullable=True),
        sa.Column('response_size', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['endpoint_id'], ['endpoints.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_checks_id'), 'checks', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_checks_id'), table_name='checks')
    op.drop_table('checks')
    op.drop_index(op.f('ix_endpoints_id'), table_name='endpoints')
    op.drop_table('endpoints')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')