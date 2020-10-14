# Docker with Unix Sockets

This is a minimal working example of a Docker container sending messages to the host computer over a Unix socket connection.

After installing Docker, build and run the Docker image with the following commands, where `<name>` is the name of the container and `<image>` is the image ID.

```bash
docker build -t <name> .
docker run -v /tmp:/tmp <image>
```
