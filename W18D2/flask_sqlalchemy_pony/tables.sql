CREATE TABLE owners (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL
);

CREATE TABLE ponies (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  birth_year INTEGER NOT NULL,
  breed VARCHAR(255),
  owner_id INTEGER NOT NULL,
  FOREIGN KEY (owner_id) REFERENCES owners(id)
);

CREATE TABLE handlers (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  employee_id VARCHAR(12) NOT NULL
);

CREATE TABLE pony_handlers (
  pony_id INTEGER NOT NULL,
  handler_id INTEGER NOT NULL,
  PRIMARY KEY (pony_id, handler_id),
  FOREIGN KEY (pony_id) REFERENCES ponies(id),
  FOREIGN KEY (handler_id) REFERENCES handlers(id)
);

INSERT INTO owners (first_name, last_name, email)
VALUES
('Joey', 'Harker', 'joey@harker.edu'),
('Jay', 'Harker', 'jay@harker.edu'),
('Josetta', 'Harker', 'josetta@harker.edu');

INSERT INTO ponies (name, birth_year, breed, owner_id)
VALUES
('Lucky Loser', 2017, 'Halfinger', 2),
('Unlucky Usurper', 2012, 'Fleuve', 1),
('Impassive Emperor', 2016, 'Hirzai', 1);

INSERT INTO handlers (first_name, last_name, employee_id)
VALUES
('Zap', 'Branagan', 'O4F'),
('The', 'Crushinator', '00100010'),
('Bubblegum', 'Tate', 'bball117');

INSERT INTO pony_handlers (pony_id, handler_id)
VALUES
(1, 1),
(1, 2),
(2, 2),
(3, 1),
(3, 3);
