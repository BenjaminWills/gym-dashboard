CREATE SCHEMA IF NOT EXISTS "admin";

CREATE SCHEMA IF NOT EXISTS "gym";

CREATE TABLE IF NOT EXISTS "admin"."users" (
  "id" SERIAL PRIMARY KEY,
  "username" VARCHAR(20),
  "password" VARCHAR(20),
  "email" VARCHAR(20),
  "first_name" VARCHAR(20),
  "last_name" VARCHAR(20),
  "DOB" DATE,
  "height" FLOAT,
  "weight" FLOAT,
  "creation_date" DATE DEFAULT (now())
);

CREATE TABLE IF NOT EXISTS "gym"."weight" (
  "user_id" INT PRIMARY KEY,
  "weight" INT,
  "updated_at" DATE,
  "active_split" INT
);

CREATE TABLE IF NOT EXISTS "gym"."splits" (
  "split_id" INT PRIMARY KEY,
  "split_name" VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS "gym"."workouts" (
  "split_id" INT PRIMARY KEY,
  "split_day" INT,
  "exercise" VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS "gym"."workout" (
  "date" DATE DEFAULT (now()),
  "user_id" INT,
  "split_id" INT,
  "split_day" INT,
  "exercise" VARCHAR(20),
  "set_1_weight" FLOAT,
  "set_1_reps" INT,
  "set_2_weight" FLOAT,
  "set_2_reps" INT,
  "set_3_weight" FLOAT,
  "set_3_reps" INT,
  PRIMARY KEY ("date", "user_id")
);

ALTER TABLE "gym"."weight" ADD FOREIGN KEY ("user_id") REFERENCES "admin"."users" ("id");

ALTER TABLE "gym"."weight" ADD FOREIGN KEY ("active_split") REFERENCES "gym"."splits" ("split_id");

ALTER TABLE "gym"."workouts" ADD FOREIGN KEY ("split_id") REFERENCES "gym"."splits" ("split_id");

ALTER TABLE "gym"."workout" ADD FOREIGN KEY ("user_id") REFERENCES "admin"."users" ("id");

ALTER TABLE "gym"."workout" ADD FOREIGN KEY ("split_id") REFERENCES "gym"."workouts" ("split_id");

ALTER TABLE "gym"."workout" ADD FOREIGN KEY ("split_day") REFERENCES "gym"."workouts" ("split_day");

ALTER TABLE "gym"."workout" ADD FOREIGN KEY ("exercise") REFERENCES "gym"."workouts" ("exercise");
