# Using docker to host postgres server

First to run the docker compose we use the `docker compose up` command. Then we enter the `bash` shell of the container

```sh
docker exec -it <container_id> bash
```

Then once in the container we should see something like:

```sh
bash-5.1#
```

Then to enter `postgresql`:

```sh
bash-5.1# psql -U postgres
```
