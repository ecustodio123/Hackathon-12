"""alumno table

Revision ID: 5e67d5092b62
Revises: 
Create Date: 2020-10-28 22:34:58.607823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e67d5092b62'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alumno',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=70), nullable=True),
    sa.Column('salon', sa.String(length=70), nullable=True),
    sa.Column('nota', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=140), nullable=True),
    sa.Column('password', sa.String(length=140), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_alumno_email'), 'alumno', ['email'], unique=True)
    op.create_index(op.f('ix_alumno_nombre'), 'alumno', ['nombre'], unique=True)
    op.create_index(op.f('ix_alumno_nota'), 'alumno', ['nota'], unique=False)
    op.create_index(op.f('ix_alumno_salon'), 'alumno', ['salon'], unique=False)
    op.create_table('profesor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=70), nullable=True),
    sa.Column('curso', sa.String(length=70), nullable=True),
    sa.Column('email', sa.String(length=140), nullable=True),
    sa.Column('password', sa.String(length=140), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_profesor_curso'), 'profesor', ['curso'], unique=False)
    op.create_index(op.f('ix_profesor_email'), 'profesor', ['email'], unique=True)
    op.create_index(op.f('ix_profesor_nombre'), 'profesor', ['nombre'], unique=True)
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('alumno', sa.String(length=70), nullable=True),
    sa.Column('asistencia', sa.String(length=70), nullable=True),
    sa.Column('tipo_examen', sa.String(length=70), nullable=True),
    sa.Column('nota', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('alumno_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['alumno_id'], ['profesor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_alumno'), 'post', ['alumno'], unique=False)
    op.create_index(op.f('ix_post_asistencia'), 'post', ['asistencia'], unique=False)
    op.create_index(op.f('ix_post_nota'), 'post', ['nota'], unique=False)
    op.create_index(op.f('ix_post_tipo_examen'), 'post', ['tipo_examen'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_tipo_examen'), table_name='post')
    op.drop_index(op.f('ix_post_nota'), table_name='post')
    op.drop_index(op.f('ix_post_asistencia'), table_name='post')
    op.drop_index(op.f('ix_post_alumno'), table_name='post')
    op.drop_table('post')
    op.drop_index(op.f('ix_profesor_nombre'), table_name='profesor')
    op.drop_index(op.f('ix_profesor_email'), table_name='profesor')
    op.drop_index(op.f('ix_profesor_curso'), table_name='profesor')
    op.drop_table('profesor')
    op.drop_index(op.f('ix_alumno_salon'), table_name='alumno')
    op.drop_index(op.f('ix_alumno_nota'), table_name='alumno')
    op.drop_index(op.f('ix_alumno_nombre'), table_name='alumno')
    op.drop_index(op.f('ix_alumno_email'), table_name='alumno')
    op.drop_table('alumno')
    # ### end Alembic commands ###
