## Pytest demo
* docker run -it --rm --name app-pytest app-pytest
* docker build -t app-pytest .
* docker run -it --rm --name app-pytest app-pytest --network=my-network
* docker run -it --network=my-network app-pytest bash
