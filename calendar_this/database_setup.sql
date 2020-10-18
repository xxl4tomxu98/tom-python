-- create user calendar_this with password 'Ku9rSyXD';
-- create database calendar_this_dev with owner calendar_this;

create table appointments (
  id serial primary key,
  name varchar(200) not null,
  start_datetime timestamp not null,
  end_datetime timestamp not null,
  description text not null,
  private boolean not null
);

-- insert into appointments (
--   name, start_datetime, end_datetime, description, private
-- )
-- values (
--   'My appointment',
--   date(current_timestamp) + interval '14 hours',
--   date(current_timestamp) + interval '15 hours',
--   'An appointment for me',
--   false
-- );

insert into appointments (
  name, start_datetime, end_datetime, description, private
)
values (
  'My appointment',
  '2020-10-17 14:00:00',
  '2020-10-17 15:00:00',
  'An appointment for me',
  false
);
