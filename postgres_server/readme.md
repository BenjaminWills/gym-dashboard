# Using docker to host postgres server

First to run the docker compose we use the `docker compose up` command. Then we enter the `bash` shell of the container

```sh
docker exec -it <container_id> bash
```

Then to enter `postgresql`:

```sh
bash-5.1# psql postgres://<username>:<password>@<hostname>/<db_name>
```
