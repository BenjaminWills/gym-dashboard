# Bens Gym Dashboard

A dashboard to track my gym progress. The dashboard reads from a `postgreSQL` database that can be updated from the dashboard via some forms.

<figure align = "center">
    <img src = "https://user-images.githubusercontent.com/90726430/198308558-5074d60e-9189-4e8e-a033-35e3e38a7d44.png" />
    <figcaption >figure 1: PostgreSQL schema</figcaption>
</figure>

# TODO

- Add github workflow to include tests for each section
- Build home page GUI that will have a few options to open other windows that will all be classbased
- Make a query interface that will be able to display output as a nice looking table in a window
- Remake schema to correct it 
- Make user login function for GUI
- When docker container is intiated, create initial tables

## Fixed

- Figure out how to interract with postgres container with python <- FIXED:
  - Issue was that the service was running on brew too, so had to run `brew service deactivate postgresql@v14` and remove it and also using `sqlalchemy.text`
- Make user login page for GUI
- Made sql tests
