from create_sqlalchemy_orm import engine, Department, Group, Student, Teacher, Workload
from sqlalchemy.orm import Session


# создание объекта Session
session = Session(bind=engine)

# создание объектов для таблицы 'Departments'
d1 = Department(name_department = 'Экономика')
d2 = Department(name_department = 'Юриспруденция')
d3 = Department(name_department = 'Информационные технологии')
d4 = Department(name_department = 'Психология')

# добавление объектов для таблицы 'Departments'
session.add_all([d1, d2, d3, d4])

# создание объектов для таблицы 'Groups'
g1 = Group(id=11, name_group='11-Эк', department_id=1)
g2 = Group(id=12, name_group='11-Эк', department_id=1)
g3 = Group(id=21, name_group='21-Юр', department_id=2)
g4 = Group(id=22, name_group='22-Юр', department_id=2)
g5 = Group(id=31, name_group='31-Ит', department_id=3)
g6 = Group(id=32, name_group='32-Ит', department_id=3)
g7 = Group(id=41, name_group='41-Пс', department_id=4)
g8 = Group(id=42, name_group='42-Пс', department_id=4)

# добавление объектов для таблицы 'Groups'
session.add_all([g1, g2, g3, g4, g5, g6, g7, g8])

# создание объектов для таблицы 'Teachers'
t1 = Teacher(name_teacher='Орлов О. В.')
t2 = Teacher(name_teacher='Велешкин Р. Т.')
t3 = Teacher(name_teacher='Григорович С. Е.')
t4 = Teacher(name_teacher='Руставели О. П.')
t5 = Teacher(name_teacher='Колокольцева Е. А.')
t6 = Teacher(name_teacher='Зюзин Е. П.')

# добавление объектов для таблицы 'Teachers'
session.add_all([t1, t2, t3, t4, t5, t6])

# создание объектов для таблицы 'Workload'
w1 = Workload(teacher_id=1, group_id=11)
w2 = Workload(teacher_id=1, group_id=12)
w3 = Workload(teacher_id=2, group_id=21)
w4 = Workload(teacher_id=2, group_id=22)
w5 = Workload(teacher_id=3, group_id=31)
w6 = Workload(teacher_id=3, group_id=32)
w7 = Workload(teacher_id=4, group_id=41)
w8 = Workload(teacher_id=4, group_id=42)
w9 = Workload(teacher_id=5, group_id=11)
w10 = Workload(teacher_id=5, group_id=12)
w11 = Workload(teacher_id=5, group_id=21)
w12 = Workload(teacher_id=5, group_id=22)
w13 = Workload(teacher_id=4, group_id=31)
w14 = Workload(teacher_id=4, group_id=32)
w15 = Workload(teacher_id=4, group_id=41)
w16 = Workload(teacher_id=4, group_id=42)

# добавление объектов для таблицы 'Workload'
session.add_all([w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16])

# создание объектов для таблицы 'Students'
s1 = Student(name_student='Олег', surname_student='Костромин', age=17, group_id=11)
s2 = Student(name_student='Илья', surname_student='Лукин', age=19, group_id=11)
s3 = Student(name_student='Ирина', surname_student='Павлова', age=18, group_id=12)
s4 = Student(name_student='Константин', surname_student='Соколов', age=19, group_id=12)
s5 = Student(name_student='Ольга', surname_student='Михайлова', age=21, group_id=21)
s6 = Student(name_student='Светлана', surname_student='Охлопкова', age=18, group_id=21)
s7 = Student(name_student='Игорь', surname_student='Великий', age=24, group_id=22)
s8 = Student(name_student='Полина', surname_student='Желтухова', age=17, group_id=31)
s9 = Student(name_student='Денис', surname_student='Малышев', age=20, group_id=31)
s10 = Student(name_student='Софья', surname_student='Кожухова', age=19, group_id=31)
s11 = Student(name_student='Георгий', surname_student='Качанов', age=18, group_id=32)
s12 = Student(name_student='Селия', surname_student='Степанова', age=21, group_id=32)
s13 = Student(name_student='Агния', surname_student='Морозова', age=25, group_id=41)
s14 = Student(name_student='Соломон', surname_student='Яковлев', age=18, group_id=41)
s15 = Student(name_student='Алексей', surname_student='Мирный', age=17, group_id=42)

# добавление объектов для таблицы 'Students'
session.add_all([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15])

# сохранение данных в БД
session.commit()

