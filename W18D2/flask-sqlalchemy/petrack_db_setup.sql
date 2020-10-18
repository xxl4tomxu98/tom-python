CREATE TABLE owners (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL
);

CREATE TABLE pet_types (
  id SERIAL PRIMARY KEY,
  type VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age integer,
    pet_type_id INTEGER NOT NULL,
    FOREIGN KEY(pet_type_id) REFERENCES pet_types(id),
    has_microchip BOOLEAN
);

CREATE TABLE pet_owners (
  owner_id INTEGER NOT NULL,
  pet_id INTEGER NOT NULL,
  PRIMARY KEY (owner_id, pet_id),
  FOREIGN KEY (owner_id) REFERENCES owners(id),
  FOREIGN KEY (pet_id) REFERENCES pets(id)
);

INSERT INTO owners (first_name, last_name, email)
  VALUES
  ('Julie', 'Nisbet', 'julie@example.com'),
  ('Mylo', 'James', 'mylo@example.com');

  INSERT INTO pet_types (type)
  VALUES
  ('Bird'),
  ('Cat'),
  ('Dog'),
  ('Elephant'),
  ('Frog');

INSERT INTO pets (name, age, pet_type_id, has_microchip)
VALUES
('Benny', 5, 3, true);
