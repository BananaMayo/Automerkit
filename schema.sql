CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
);
CREATE TABLE polls (
    id SERIAL PRIMARY KEY,
    topic TEXT,
    created_at TIMESTAMP
);
CREATE TABLE choices (
    id SERIAL PRIMARY KEY,
    poll_id INTEGER REFERENCES polls,
    choice TEXT
);
CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    choice_id INTEGER REFERENCES choices,
    sent_at TIMESTAMP
);

CREATE TABLE correct (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    poll_id INTEGER REFERENCES polls,
    
);