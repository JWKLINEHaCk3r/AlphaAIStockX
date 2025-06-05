from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'credit_usage',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('used', sa.Float(), nullable=False),
        sa.Column('available', sa.Float(), nullable=False),
        sa.Column('limit', sa.Float(), nullable=False),
        sa.Column('timestamp', sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.ForeignKeyConstraint(['user_id'], ['user.id']),
    )

def downgrade():
    op.drop_table('credit_usage')
