-- drop tables if they exist
DROP TABLE IF EXISTS proj_stair;
DROP TABLE IF EXISTS saves;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS guide;
DROP TABLE IF EXISTS stairs;
DROP TABLE IF EXISTS signatures;
DROP TABLE IF EXISTS project;

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

-- create project table
CREATE TABLE project (
    proj_id SERIAL PRIMARY KEY,
    pname VARCHAR (50),
    floors NUMERIC,
    privacy VARCHAR(20)
);

-- create signatures table
CREATE TABLE signatures(
    sig_id SERIAL PRIMARY KEY,
    sig VARCHAR(50),
    date_ VARCHAR(10),
    proj_id serial REFERENCES project(proj_id)
);

--create table stairs
CREATE TABLE stairs (
    stair_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    rise NUMERIC,
    part_m BOOLEAN,
    inside VARCHAR(10)
);

-- create saves table
CREATE TABLE saves (
    user_id SERIAL REFERENCES users(user_id),
    proj_id SERIAL REFERENCES project(proj_id),
    PRIMARY KEY (user_id, proj_id)
);

-- create proj_stair table
CREATE TABLE proj_stair (
    stair_id SERIAL REFERENCES stairs(stair_id),
    proj_id SERIAL REFERENCES project(proj_id),
    PRIMARY KEY (stair_id, proj_id)
);

--add test user
INSERT INTO users (username, password) VALUES ('test' , 'open');

--add test project
INSERT INTO project (pname , floors , privacy) VALUEs ('test', '1' , 'private');
INSERT INTO saves (user_id , proj_id ) (SELECT u.user_id FROM users u WHERE u.username = 'test' UNION ALL SELECT p.proj_id FROM project p WHERE p.pname = 'test');

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