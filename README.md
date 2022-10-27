# Bens Gym Dashboard

A dashboard to track my gym progress. The dashboard reads from a `postgreSQL` database that can be updated from the dashboard via some forms.

<figure align = "center">
    <img src = "https://user-images.githubusercontent.com/90726430/198308558-5074d60e-9189-4e8e-a033-35e3e38a7d44.png" />
    <figcaption >figure 1: PostgreSQL schema</figcaption>
</figure>

### SQL Wrapper

First we initialise the Sql wrapper with your respective credentials:

```sh
engine_connect_string = "dialect+driver://username:password@host:port/database"
```

The driver I'm using is `postgresql` and the engine is `psycopg2` but this need not be specified as it is the default.
