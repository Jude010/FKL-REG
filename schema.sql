-- drop tables if they exist
DROP TABLE IF EXISTS usrsave;
DROP TABLE IF EXISTS saves;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS guide;

-- create user table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT UNIQUE NOT NULL
);

-- create guide table
CREATE TABLE guide (
    guide_id SERIAL PRIMARY KEY,
    guide_name VARCHAR(10) NOT NULL,
    diagram varchar(20)
);

-- create saves table
CREATE TABLE saves (
    save_id SERIAL PRIMARY KEY,
    guide_id SERIAL REFERENCES guide(guide_id)
);

-- create usrsave table
CREATE TABLE usrsave (
    save_id SERIAL REFERENCES saves(save_id),
    user_id SERIAL REFERENCES USERS(user_id),
    PRIMARY KEY (save_id, user_id)
);

-- insert 
INSERT INTO guide (guide_name, diagram) VALUES
('k1.1.3', NULL),
('k1.1.4', 'table 1'),
('k1.1.6', 'diagram 2'),
('k1.1.7', 'diagram 1'),
('k1.1.8', NULL),
('k1.1.9', 'diagram 3'),
('k1.1.10', NULL),
('k1.1.11', NULL),
('k1.1.12', 'diagram 4'),
('k1.1.13', NULL),
('k1.1.14', 'diagram 5'),
('k1.1.15', NULL),
('k1.1.16', NULL),
('k1.1.17', 'dagram 6'),
('k1.1.18', 'diagram 6'),
('k1.1.19', NULL),
('k1.1.20', 'diagram 6'),
('k1.2.1', NULL),
('k1.2.2', NULL),
('k1.2.3', NULL),
('k1.2.4', NULL),
('k1.2.5', NULL),
('k1.2.6', NULL),
('k1.2.7', NULL),
('k2.2', NULL),
('k2.3', 'diagram 6'),
('k2.4', 'diagram 7'),
('k2.5', 'diagram 6'),
('k2.6', NULL),
('k2.7', 'diagram 9'),
('k2.8', 'diagram 10'),
('k2.9', 'diagram 11')