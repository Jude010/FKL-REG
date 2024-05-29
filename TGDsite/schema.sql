DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS guide;
DROP TABLE IF EXISTS saves;
DROP TABLE IF EXISTS usrsave;

CREATE TABLE user (
    user_id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT UNIQUE NOT NULL
);

CREATE TABLE guide (
    guide_id SERIAL PRIMARY KEY,
    guide_name VARCHAR(10) NOT NULL
);

CREATE TABLE saves (
    save_id SERIAL PRIMARY KEY,
    guide_id REFERENCES guide(guide_id)
);

CREATE TABLE usrsave (
    save_id REFERENCES saves(save_id)
    user_id REFERENCES USER(user_id)
    PRIMARY KEY (save_id, user_id)
);
