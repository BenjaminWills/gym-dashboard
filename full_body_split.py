from utilities.sql.sql_wrapper import Sql_wrapper

if __name__ == "__main__":

    sql = Sql_wrapper(
        username="admin",
        password="password",
        host="localhost",
        port=5432,
        db_name="gym_application",
    )

    full_body_split_insertion = """
        INSERT INTO 
            gym.splits(split_name) 
        VALUES 
            ('full body');
        """

    sql.execute_create(full_body_split_insertion)

    index_of_full_body_split = sql.execute_read(
        """
        SELECT 
            split_id
        FROM
            gym.splits
        WHERE
            split_name = 'full body'
        """
    )[1][0]

    split_by_day = {
        1: [
            "back squat",
            "db press",
            "leg curl",
            "pulldown",
            "bicep curl",
            "leg raise",
        ],
        2: [
            "bench press",
            "cable flye",
            "rdl",
            "db row",
            "arnold press",
            "pressdown",
            "shrug",
        ],
        3: [
            "pullup",
            "db row",
            "leg press",
            "calf raise",
            "upright row",
            "hammer curl",
            "push up",
        ],
        4: ["run"],
        5: [
            "deadlift",
            "dip",
            "hip thrust",
            "leg extension",
            "pullover",
            "lateral raise",
            "skullcrusher",
        ],
        6: [
            "overhead press",
            "lateral raise",
            "cable row",
            "hip abduction",
            "incline curl",
            "crunch",
            "calf raise",
        ],
        7: ["run"],
        8: ["rest"],
    }

    full_body_insert = """
        INSERT INTO 
            gym.workouts(split_id,split_day,exercise) 
        VALUES
    """
    for day, exercises in split_by_day.items():
        for exercise in exercises:
            if day == 8:
                insertion_statement = (
                    f"""\t({index_of_full_body_split},{day},'{exercise}')"""
                )
            else:
                insertion_statement = (
                    f"""\t({index_of_full_body_split},{day},'{exercise}'),\n"""
                )
            full_body_insert += insertion_statement

    sql.execute_create(full_body_insert)
