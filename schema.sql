CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT,
    role INTEGER
);

CREATE TABLE polls (
    id SERIAL PRIMARY KEY,
    creator_id INTEGER REFERENCES users,
    topic TEXT,
    created_at TIMESTAMP,
    visible INTEGER
);

CREATE TABLE choices (
    id SERIAL PRIMARY KEY,
    poll_id INTEGER REFERENCES polls,
    choice TEXT,
    image BYTEA,
    correct_choice TEXT
);

CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    choice_id INTEGER REFERENCES choices,
    sent_at TIMESTAMP,
    user_id INTEGER REFERENCES users,
    result INTEGER
);