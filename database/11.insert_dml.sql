insert into programs values (1, 'математика и информационные технологии');
insert into programs values (2, 'теоретическая физика');

insert into students(id, program_id, card, surname, name) values(1, 1, '180101', 'Битов', 'Антон');
insert into students(id, program_id, card, surname, name) values(2, 1, '180102', 'Иванов', 'Алексей');
insert into students(id, program_id, card, surname, name) values(3, 2, '180201', 'Аргонова', 'Виолетта');
insert into students(id, program_id, card, surname, name) values(4, 2, '180202', 'Смирнов', 'Федор');
insert into students(id, program_id, card, surname, name) values(5, 2, '180203', 'Петров', 'Василий');

insert into courses values(101, 'линейная алгебра');
insert into courses values(201, 'численные методы');

insert into marks values(1, 101, 3);
insert into marks values(2, 101, 5);
insert into marks values(3, 201, 4);
insert into marks values(4, 201, 2);
insert into marks values(5, 201, 5);
