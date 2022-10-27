-- ####################################################CATEGORY TABLE##############################################################

CREATE TABLE categories (
id SERIAL PRIMARY KEY NOT NULL,
category TEXT not null);

INSERT INTO categories (category) VALUES
('push'),
('pull'),
('legs');

-- ####################################################EXERCISE TABLE##############################################################

CREATE TABLE exercises(
id SERIAL PRIMARY KEY NOT NULL,
category_id INT,
exercise TEXT,
FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- ####################################################GYM TABLE###################################################################

CREATE TABLE gym(
id SERIAL PRIMARY KEY NOT NULL,
exercise_id INT NOT NULL,
date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (exercise_id) REFERENCES exercises(id)
);

-- ####################################################SETS TABLE##################################################################

CREATE TABLE sets(
gym_id INT,
exercise_id INT,
repetitions INT,
weight REAL,
rpe REAL,
PRIMARY KEY(gym_id,exercise_id),
FOREIGN KEY (gym_id) REFERENCES gym(id),
FOREIGN KEY (exercise_id) REFERENCES exercises(id)
);