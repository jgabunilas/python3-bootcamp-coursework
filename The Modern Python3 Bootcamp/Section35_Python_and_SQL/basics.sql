-- Creating tables
CREATE TABLE dogs (
        name TEXT,
        breed TEXT,
        age INT
);

CREATE TABLE cats (
        name TEXT,
        breed TEXT,
        age INT
);

-- Inserting data into tables
INSERT INTO cats (name, breed, age) 
VALUES ("Blue", "Scottish Fold", 3);

INSERT INTO cats (name, breed, age) 
VALUES ("Cyrax", "Siamese", 4);

-- INSERT INTO dogs (name, age, breed) VALUES ("Champ", 4, "Husky");
-- INSERT INTO dogs (name, age, breed) VALUES ("Rose", 11, "Chihuahua");
-- INSERT INTO dogs (name, age, breed) VALUES ("Moose", 5, "Lab");
-- INSERT INTO dogs (name, age, breed) VALUES ("Piggy", 4, "Corgi");
INSERT INTO dogs (name, age, breed) VALUES ("Maggie", 4, "Terrier");
INSERT INTO dogs (name, age, breed) VALUES ("River", 7, "Husky");
INSERT INTO dogs (name, age, breed) VALUES ("Archer", 8, "Pitbull");
INSERT INTO dogs (name, age, breed) VALUES ("Pam", 2, "Pug");

-- Selecting data in tables
