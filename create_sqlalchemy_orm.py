from sqlalchemy import create_engine, MetaData, Integer, String, Column, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# подключение к серверу PostgreSQL
# username, password - данные для получения доступа к БД, database - название созданной БД
engine = create_engine('postgresql+psycopg2://username:password@localhost/database')

# наследование от декларативного базового класса
Base = declarative_base()

# создание объекта MetaData, используется для создания/удаления таблиц
metadata = MetaData()


class Department(Base):
    """Таблица Departments с полями 'id', 'name_department' """
    __tablename__ = 'Departments'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name_department = Column(Text, nullable=False)
    groups = relationship('Group')


class Group(Base):
    """Таблица Groups с полями 'id', 'name_group',
    'department_id' (внешний ключ с таблицей Departments) """
    __tablename__ = 'Groups'
    id = Column(Integer(), primary_key=True)
    name_group = Column(String(5), nullable=False)
    department_id = Column(Integer(), ForeignKey('Departments.id'))
    students = relationship('Student')
    workload = relationship('Workload')


class Student(Base):
    """Таблица Students с полями 'id', 'name_student', 'surname_student', 'age',
    'group_id' (внешний ключ с таблицей Groups) """
    __tablename__ = 'Students'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name_student = Column(String(30), nullable=False)
    surname_student = Column(String(30), nullable=False)
    age = Column(Integer(), nullable=False)
    group_id = Column(Integer(), ForeignKey('Groups.id'))


class Teacher(Base):
    """Таблица Teachers с полями 'id', 'name_teacher' """
    __tablename__ = 'Teachers'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name_teacher = Column(Text, nullable=False)
    workload = relationship('Workload')


class Workload(Base):
    """Таблица Workload с полями 'teacher_id' (внешний ключ с таблицей Teachers),
    'group_id' (внешний ключ с таблицей Groups) """
    __tablename__ = 'Workload'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    teacher_id = Column(Integer(), ForeignKey('Teachers.id'))
    group_id = Column(Integer(), ForeignKey('Groups.id'))

# создание таблиц
Base.metadata.create_all(engine)