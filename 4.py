'''select * from employee where department == (select id from department where name == 'Research');'''