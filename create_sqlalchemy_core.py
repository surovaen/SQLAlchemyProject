from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, ForeignKey


# подключение к серверу PostgreSQL
# username, password - данные для получения доступа к БД, database - название созданной БД
engine = create_engine('postgresql+psycopg2://username:password@localhost/database')
engine.connect()

# создание объекта MetaData, используется для создания/удаления таблиц
metadata = MetaData()

# схема таблицы 'Departments' с полями 'id', 'name_department'
department = Table('Departments', metadata,
    Column('id', Integer(), primary_key=True, autoincrement=True),
    Column('name_department', Text, nullable=False)
)

# схема таблицы 'Groups' с полями 'id', 'name_group', 'department_id' (внешний ключ с таблицей 'Departments')
group = Table('Groups', metadata,
    Column('id', Integer(), primary_key=True),
    Column('name_group', String(10), nullable=False),
    Column('department_id', Integer(), ForeignKey(department.c.id))
)

# схема таблицы 'Students' с полями 'id', 'name_student', 'surname_student', 'age',
# 'group_id' (внешний ключ с таблицей 'Groups')
student = Table('Students', metadata,
    Column('id', Integer(), primary_key=True, autoincrement=True),
    Column('name_student', String(30), nullable=False),
    Column('surname_student', String(30), nullable=False),
    Column('age', Integer(), nullable=False),
    Column('group_id', Integer(), ForeignKey(group.c.id))
)

# схема таблицы 'Teachers' с полями 'id', 'name_teacher'
teacher = Table('Teachers', metadata,
    Column('id', Integer(), primary_key=True, autoincrement=True),
    Column('name_teacher', Text, nullable=False)
)

# схема таблицы 'Workload' с полями 'teacher_id' (внешний ключ с таблицей 'Teachers'),
#'group_id' (внешний ключ с таблицей 'Groups')
workload = Table('Workload', metadata,
    Column('teacher_id', Integer(), ForeignKey('Teachers.id')),
    Column('group_id', Integer(), ForeignKey('Groups.id'))
)

# создание таблиц
metadata.create_all(engine)