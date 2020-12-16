"""empty message

Revision ID: 892b264937ec
Revises: df1834485f57
Create Date: 2019-05-08 13:57:15.653356

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlalchemy_utils
import uuid

# revision identifiers, used by Alembic.
revision = '892b264937ec'
down_revision = 'df1834485f57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('change', sa.Boolean(), nullable=False),
    sa.Column('person_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=False),
    sa.Column('author_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=False),
    sa.Column('comment_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=True),
    sa.Column('task_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=False),
    sa.Column('preview_file_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['comment_id'], ['comment.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['preview_file_id'], ['task.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['task.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_news_author_id'), 'news', ['author_id'], unique=False)
    op.create_index(op.f('ix_news_comment_id'), 'news', ['comment_id'], unique=False)
    op.create_index(op.f('ix_news_person_id'), 'news', ['person_id'], unique=False)
    op.create_index(op.f('ix_news_preview_file_id'), 'news', ['preview_file_id'], unique=False)
    op.create_index(op.f('ix_news_task_id'), 'news', ['task_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_news_task_id'), table_name='news')
    op.drop_index(op.f('ix_news_preview_file_id'), table_name='news')
    op.drop_index(op.f('ix_news_person_id'), table_name='news')
    op.drop_index(op.f('ix_news_comment_id'), table_name='news')
    op.drop_index(op.f('ix_news_author_id'), table_name='news')
    op.drop_table('news')
    # ### end Alembic commands ###
