from create_sqlalchemy_core import department, group, teacher, workload, student, engine
from sqlalchemy import insert


# список данных для таблицы 'Departments'
department_list = [
    {
        'name_department': 'Экономика'
    },
    {
        'name_department': 'Менеджмент'
    },
    {
        'name_department': 'Юриспруденция'
    },
    {
        'name_department': 'Информационные технологии'
    },
    {
        'name_department': 'Филология'
    },
    {
        'name_department': 'Архитектура и дизайн'
    },
    {
        'name_department': 'Психология'
    }
]

# список данных для таблицы 'Groups'
group_list = [
    {
        'id': 11,
        'name_group': '00-AA',
        'department_id': 1
    },
    {
        'id': 12,
        'name_group': '00-AB',
        'department_id': 1
    },
    {
        'id': 13,
        'name_group': '00-AC',
        'department_id': 1
    },
    {
        'id': 21,
        'name_group': '00-BA',
        'department_id': 2
    },
    {
        'id': 22,
        'name_group': '00-BC',
        'department_id': 2
    },
    {
        'id': 23,
        'name_group': '00-BC',
        'department_id': 2
    },
    {
        'id': 31,
        'name_group': '00-CA',
        'department_id': 3
    },
    {
        'id': 32,
        'name_group': '00-CB',
        'department_id': 3
    },
    {
        'id': 33,
        'name_group': '00-CC',
        'department_id': 3
    },
    {
        'id': 41,
        'name_group': '00-DA',
        'department_id': 4
    },
    {
        'id': 42,
        'name_group': '00-DB',
        'department_id': 4
    },
    {
        'id': 43,
        'name_group': '00-DC',
        'department_id': 4
    },
    {
        'id': 51,
        'name_group': '00-EA',
        'department_id': 5
    },
    {
        'id': 61,
        'name_group': '00-FA',
        'department_id': 6
    },
    {
        'id': 62,
        'name_group': '00-FB',
        'department_id': 6
    },
    {
        'id': 71,
        'name_group': '00-JA',
        'department_id': 7
    },
    {
        'id': 72,
        'name_group': '00-JB',
        'department_id': 7
    }
]

# список данных для таблицы 'Teachers'
teacher_list = [
    {
        'name_teacher': 'Орлова О. Г.'
    },
    {
        'name_teacher': 'Зюзин Е. П.'
    },
    {
        'name_teacher': 'Ельцов Д. В.'
    },
    {
        'name_teacher': 'Колокольцева Е. А.'
    },
    {
        'name_teacher': 'Алешкина З. В.'
    },
    {
        'name_teacher': 'Перельман Г. Я.'
    },
    {
        'name_teacher': 'Дудин П. Ф.'
    },
    {
        'name_teacher': 'Суздальцева С. С.'
    },
    {
        'name_teacher': 'Чикин А. В.'
    },
    {
        'name_teacher': 'Булкина П. Р.'
    },
    {
        'name_teacher': 'Велешкин Р. Т.'
    },
    {
        'name_teacher': 'Григорович С. Е.'
    },
    {
        'name_teacher': 'Яковлев О. Ю.'
    },
    {
        'name_teacher': 'Коммандер Ю. В.'
    },
    {
        'name_teacher': 'Руставели О. П.'
    },
    {
        'name_teacher': 'Никитин О. Ю.'
    },
    {
        'name_teacher': 'Пономарев И. С.'
    },
    {
        'name_teacher': 'Колокольцева Е. А.'
    }
]

# список данных для таблицы 'Workload'
workload_list = [
    {
        'teacher_id': 1,
        'group_id': 11
    },
    {
        'teacher_id': 1,
        'group_id': 12
    },
    {
        'teacher_id': 1,
        'group_id': 13
    },
    {
        'teacher_id': 1,
        'group_id': 21
    },
    {
        'teacher_id': 1,
        'group_id': 31
    },
    {
        'teacher_id': 1,
        'group_id': 61
    },
    {
        'teacher_id': 2,
        'group_id': 11
    },
    {
        'teacher_id': 2,
        'group_id': 12
    },
    {
        'teacher_id': 2,
        'group_id': 13
    },
    {
        'teacher_id': 2,
        'group_id': 22
    },
    {
        'teacher_id': 2,
        'group_id': 32
    },
    {
        'teacher_id': 2,
        'group_id': 62
    },
    {
        'teacher_id': 3,
        'group_id': 11
    },
    {
        'teacher_id': 3,
        'group_id': 12
    },
    {
        'teacher_id': 3,
        'group_id': 13
    },
    {
        'teacher_id': 3,
        'group_id': 23
    },
    {
        'teacher_id': 3,
        'group_id': 33
    },
    {
        'teacher_id': 4,
        'group_id': 41
    },
    {
        'teacher_id': 4,
        'group_id': 42
    },
    {
        'teacher_id': 4,
        'group_id': 43
    },
    {
        'teacher_id': 4,
        'group_id': 51
    },
    {
        'teacher_id': 4,
        'group_id': 71
    },
    {
        'teacher_id': 4,
        'group_id': 72
    },
    {
        'teacher_id': 5,
        'group_id': 21
    },
    {
        'teacher_id': 5,
        'group_id': 22
    },
    {
        'teacher_id': 5,
        'group_id': 23
    },
    {
        'teacher_id': 5,
        'group_id': 11
    },
    {
        'teacher_id': 5,
        'group_id': 31
    },
    {
        'teacher_id': 5,
        'group_id': 41
    },
    {
        'teacher_id': 5,
        'group_id': 61
    },
    {
        'teacher_id': 6,
        'group_id': 21
    },
    {
        'teacher_id': 5,
        'group_id': 22
    },
    {
        'teacher_id': 5,
        'group_id': 23
    },
    {
        'teacher_id': 5,
        'group_id': 12
    },
    {
        'teacher_id': 5,
        'group_id': 32
    },
    {
        'teacher_id': 5,
        'group_id': 42
    },
    {
        'teacher_id': 5,
        'group_id': 62
    },
    {
        'teacher_id': 6,
        'group_id': 21
    },
    {
        'teacher_id': 6,
        'group_id': 22
    },
    {
        'teacher_id': 6,
        'group_id': 23
    },
    {
        'teacher_id': 6,
        'group_id': 13
    },
    {
        'teacher_id': 6,
        'group_id': 33
    },
    {
        'teacher_id': 6,
        'group_id': 43
    },
    {
        'teacher_id': 6,
        'group_id': 51
    },
    {
        'teacher_id': 7,
        'group_id': 71
    },
    {
        'teacher_id': 7,
        'group_id': 72
    },
    {
        'teacher_id': 8,
        'group_id': 31
    },
    {
        'teacher_id': 8,
        'group_id': 32
    },
    {
        'teacher_id': 8,
        'group_id': 33
    },
    {
        'teacher_id': 8,
        'group_id': 41
    },
    {
        'teacher_id': 9,
        'group_id': 31
    },
    {
        'teacher_id': 9,
        'group_id': 32
    },
    {
        'teacher_id': 9,
        'group_id': 33
    },
    {
        'teacher_id': 9,
        'group_id': 42
    },
    {
        'teacher_id': 9,
        'group_id': 43
    },
    {
        'teacher_id': 10,
        'group_id': 41
    },
    {
        'teacher_id': 10,
        'group_id': 42
    },
    {
        'teacher_id': 10,
        'group_id': 43
    },
    {
        'teacher_id': 10,
        'group_id': 61
    },
    {
        'teacher_id': 10,
        'group_id': 62
    },
    {
        'teacher_id': 11,
        'group_id': 41
    },
    {
        'teacher_id': 11,
        'group_id': 42
    },
    {
        'teacher_id': 11,
        'group_id': 43
    },
    {
        'teacher_id': 11,
        'group_id': 61
    },
    {
        'teacher_id': 11,
        'group_id': 62
    },
    {
        'teacher_id': 12,
        'group_id': 41
    },
    {
        'teacher_id': 12,
        'group_id': 42
    },
    {
        'teacher_id': 12,
        'group_id': 43
    },
    {
        'teacher_id': 13,
        'group_id': 51
    },
    {
        'teacher_id': 13,
        'group_id': 21
    },
    {
        'teacher_id': 13,
        'group_id': 22
    },
    {
        'teacher_id': 13,
        'group_id': 23
    },
    {
        'teacher_id': 14,
        'group_id': 51
    },
    {
        'teacher_id': 14,
        'group_id': 71
    },
    {
        'teacher_id': 14,
        'group_id': 72
    },
    {
        'teacher_id': 15,
        'group_id': 61
    },
    {
        'teacher_id': 15,
        'group_id': 62
    },
    {
        'teacher_id': 15,
        'group_id': 41
    },
    {
        'teacher_id': 15,
        'group_id': 42
    },
    {
        'teacher_id': 16,
        'group_id': 61
    },
    {
        'teacher_id': 16,
        'group_id': 62
    },
    {
        'teacher_id': 16,
        'group_id': 43
    },
    {
        'teacher_id': 17,
        'group_id': 71
    },
    {
        'teacher_id': 17,
        'group_id': 72
    },
    {
        'teacher_id': 17,
        'group_id': 21
    },
    {
        'teacher_id': 17,
        'group_id': 22
    },
    {
        'teacher_id': 18,
        'group_id': 71
    },
    {
        'teacher_id': 18,
        'group_id': 72
    },
    {
        'teacher_id': 18,
        'group_id': 23
    },
    {
        'teacher_id': 18,
        'group_id': 51
    },
]

# список данных для таблицы 'Students'
student_list = [
    {
        'name_student': 'Алеся',
        'surname_student': 'Петрова',
        'age': 17,
        'group_id': 11
    },
    {
        'name_student': 'Борис',
        'surname_student': 'Коломнов',
        'age': 18,
        'group_id': 11
    },
    {
        'name_student': 'Вероника',
        'surname_student': 'Соболева',
        'age': 17,
        'group_id': 11
    },
    {
        'name_student': 'Григорий',
        'surname_student': 'Усольцев',
        'age': 19,
        'group_id': 12
    },
    {
        'name_student': 'Денис',
        'surname_student': 'Поромонов',
        'age': 17,
        'group_id': 12
    },
    {
        'name_student': 'Елена',
        'surname_student': 'Никитина',
        'age': 23,
        'group_id': 12
    },
    {
        'name_student': 'Жизель',
        'surname_student': 'Обудсен',
        'age': 20,
        'group_id': 13
    },
    {
        'name_student': 'Зоя',
        'surname_student': 'Григоренко',
        'age': 17,
        'group_id': 13
    },
    {
        'name_student': 'Илья',
        'surname_student': 'Макаров',
        'age': 20,
        'group_id': 13
    },
    {
        'name_student': 'Константин',
        'surname_student': 'Королев',
        'age': 19,
        'group_id': 21
    },
    {
        'name_student': 'Лев',
        'surname_student': 'Ослов',
        'age': 21,
        'group_id': 21
    },
    {
        'name_student': 'Мария',
        'surname_student': 'Егорова',
        'age': 18,
        'group_id': 21
    },
    {
        'name_student': 'Николай',
        'surname_student': 'Леонов',
        'age': 24,
        'group_id': 22
    },
    {
        'name_student': 'Ольга',
        'surname_student': 'Варфоломеева',
        'age': 21,
        'group_id': 22
    },
    {
        'name_student': 'Полина',
        'surname_student': 'Щеткина',
        'age': 22,
        'group_id': 22
    },
    {
        'name_student': 'Роман',
        'surname_student': 'Алабаев',
        'age': 17,
        'group_id': 23
    },
    {
        'name_student': 'Светлана',
        'surname_student': 'Александрова',
        'age': 19,
        'group_id': 23
    },
    {
        'name_student': 'Татьяна',
        'surname_student': 'Ульянова',
        'age': 19,
        'group_id': 23
    },
    {
        'name_student': 'Ульрих',
        'surname_student': 'Иванов',
        'age': 25,
        'group_id': 31
    },
    {
        'name_student': 'Фекла',
        'surname_student': 'Дремова',
        'age': 17,
        'group_id': 31
    },
    {
        'name_student': 'Харитон',
        'surname_student': 'Мартемьянов',
        'age': 19,
        'group_id': 31
    },
    {
        'name_student': 'Церцея',
        'surname_student': 'Драконова',
        'age': 18,
        'group_id': 32
    },
    {
        'name_student': 'Чингиз',
        'surname_student': 'Айтматов',
        'age': 21,
        'group_id': 32
    },
    {
        'name_student': 'Шафран',
        'surname_student': 'Александров',
        'age': 17,
        'group_id': 32
    },
    {
        'name_student': 'Эльза',
        'surname_student': 'Морозова',
        'age': 23,
        'group_id': 33
    },
    {
        'name_student': 'Юрий',
        'surname_student': 'Коротов',
        'age': 20,
        'group_id': 33
    },
    {
        'name_student': 'Ярослава',
        'surname_student': 'Гордова',
        'age': 22,
        'group_id': 33
    },
    {
        'name_student': 'Альфред',
        'surname_student': 'Морган',
        'age': 21,
        'group_id': 41
    },
    {
        'name_student': 'Бомбина',
        'surname_student': 'Сельвия',
        'age': 19,
        'group_id': 41
    },
    {
        'name_student': 'Вениамин',
        'surname_student': 'Григорян',
        'age': 22,
        'group_id': 41
    },
    {
        'name_student': 'Галина',
        'surname_student': 'Егорова',
        'age': 17,
        'group_id': 42
    },
    {
        'name_student': 'Дарья',
        'surname_student': 'Чурикова',
        'age': 26,
        'group_id': 42
    },
    {
        'name_student': 'Екатерина',
        'surname_student': 'Суворова',
        'age': 21,
        'group_id': 42
    },
    {
        'name_student': 'Золанд',
        'surname_student': 'Проперти',
        'age': 19,
        'group_id': 43
    },
    {
        'name_student': 'Ирина',
        'surname_student': 'Кравцова',
        'age': 22,
        'group_id': 43
    },
    {
        'name_student': 'Константин',
        'surname_student': 'Семенов',
        'age': 22,
        'group_id': 43
    },
    {
        'name_student': 'Лаура',
        'surname_student': 'Эдельвайс',
        'age': 17,
        'group_id': 51
    },
    {
        'name_student': 'Михаил',
        'surname_student': 'Сотников',
        'age': 27,
        'group_id': 51
    },
    {
        'name_student': 'Наталья',
        'surname_student': 'Поленова',
        'age': 21,
        'group_id': 51
    },
    {
        'name_student': 'Олег',
        'surname_student': 'Великолепнов',
        'age': 24,
        'group_id': 61
    },
    {
        'name_student': 'Поль',
        'surname_student': 'Кертис',
        'age': 21,
        'group_id': 61
    },
    {
        'name_student': 'Редиса',
        'surname_student': 'Зеленова',
        'age': 17,
        'group_id': 61
    },
    {
        'name_student': 'Степан',
        'surname_student': 'Ильин',
        'age': 18,
        'group_id': 62
    },
    {
        'name_student': 'Теодор',
        'surname_student': 'Лукьянов',
        'age': 22,
        'group_id': 62
    },
    {
        'name_student': 'Ульяна',
        'surname_student': 'Селикатова',
        'age': 17,
        'group_id': 62
    },
    {
        'name_student': 'Феликс',
        'surname_student': 'Командоров',
        'age': 17,
        'group_id': 71
    },
    {
        'name_student': 'Харм',
        'surname_student': 'Париш',
        'age': 24,
        'group_id': 71
    },
    {
        'name_student': 'Честер',
        'surname_student': 'Беннингтон',
        'age': 27,
        'group_id': 71
    },
    {
        'name_student': 'Шалом',
        'surname_student': 'Белини',
        'age': 18,
        'group_id': 72
    },
    {
        'name_student': 'Элина',
        'surname_student': 'Ростова',
        'age': 22,
        'group_id': 72
    },
    {
        'name_student': 'Юлия',
        'surname_student': 'Аркадьева',
        'age': 21,
        'group_id': 72
    },
]


# подключение к серверу PostgreSQL
connect = engine.connect()

# внесение данных в таблицы
connect.execute(insert(department), department_list)
connect.execute(insert(group), group_list)
connect.execute(insert(teacher), teacher_list)
connect.execute(insert(workload), workload_list)
connect.execute(insert(student), student_list)
