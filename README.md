# Docker with Unix Sockets

This is a minimal working example of a Docker container sending messages to the host computer over a Unix socket connection.

After installing Docker, build the Docker image with the following commands, where `<name>` is the name of the container.

```bash
docker build -t <name> .
```

Start the Python server on the host machine with the following command.

```bash
python3 server.py
```

While the `server.py` Python process is running, run `client.py` in the Docker image with the following command, where `<image>` is the image ID.

```bash
docker run -v /tmp:/tmp <image>
```
