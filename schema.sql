-- drop tables if they exist
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS guide;
DROP TABLE IF EXISTS saves;
DROP TABLE IF EXISTS usrsave;

-- create user table
CREATE TABLE user (
    user_id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT UNIQUE NOT NULL
);

-- create guide table
CREATE TABLE guide (
    guide_id SERIAL PRIMARY KEY,
    guide_name VARCHAR(10) NOT NULL
);

-- create saves table
CREATE TABLE saves (
    save_id SERIAL PRIMARY KEY,
    guide_id REFERENCES guide(guide_id)
);

-- create usrsave table
CREATE TABLE usrsave (
    save_id REFERENCES saves(save_id)
    user_id REFERENCES USER(user_id)
    PRIMARY KEY (save_id, user_id)
);

-- insert 
INSERT INTO guide (guide_name) VALUES
('k1.1.3'),
('k1.1.4'),
('k1.1.6'),
('k1.1.7'),
('k1.1.8'),
('k1.1.9'),
('k1.1.10'),
('k1.1.11'),
('k1.1.12'),
('k1.1.13'),
('k1.1.14'),
('k1.1.15'),
('k1.1.16'),
('k1.1.17'),
('k1.1.18'),
('k1.1.19'),
('k1.1.20'),
('k1.2.1'),
('k1.2.2'),
('k1.2.3'),
('k1.2.4'),
('k1.2.5'),
('k1.2.6'),
('k1.2.7'),
('k2.2'),
('k2.3'),
('k2.4'),
('k2.5'),
('k2.6'),
('k2.7'),
('k2.8'),
('k2.9')