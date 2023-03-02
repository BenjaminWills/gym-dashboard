# Bens Gym Dashboard

A dashboard to track my gym progress. The dashboard reads from a `postgreSQL` database that can be updated from the dashboard via some forms.

<figure align = "center">
    <img src = "https://user-images.githubusercontent.com/90726430/198308558-5074d60e-9189-4e8e-a033-35e3e38a7d44.png" />
    <figcaption >figure 1: PostgreSQL schema</figcaption>
</figure>

# TODO

- Add github workflow to include tests for each section
- Build home page GUI that will have a few options to open other windows that will all be classbased
- Remake schema to correct it 
- When docker container is intiated, create initial tables
- Find a way to run the docker compose and then the gui in one command (desktop icon?)

## Fixed

- Make a query interface that will be able to display output as a nice looking table in a window
- Figure out how to interract with postgres container with python <- FIXED:
  - Issue was that the service was running on brew too, so had to run `brew service deactivate postgresql@v14` and remove it and also using `sqlalchemy.text`
- Make user login page for GUI
- Made sql tests
- Make user login function for GUI

# HOW TO USE

First `cd` into the `postgres_server` file and write the command:

```shell
docker compose up -d
```

This will run all the specified containers in the docker compose in `detatched` (`-d`) mode. Once this has been run, and 

```shell
docker ps
```

Shows a container running, we can cd out to the top level directory and run the GUI!

```shell
python gym_gui/gui.py
```

Note that the storage is persisted even when the `docker compose down` is run.