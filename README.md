# information-storage-and-backend <!-- omit in toc -->

A MySQL and Python Flask rest API run using docker

## Table of Contents <!-- omit in toc -->

<!-- TOC -->
- [Quick Start](#quick-start)
- [Contributing](#contributing)
- [Run The Application](#run-the-application)
- [Additional Docs](#additional-docs)
<!-- /TOC -->

## Quick Start

1. go through all the Prerequisites in [Prerequisites](docs/prerequisites.md)
2. run `npm i`
3. `docker compose up` to build docker images and run docker containers
4. Go to `localhost:443` and you should see a "Not Found" page

If you run into issues, see the additional docs below **[bottom of page](#Additional-Docs)**

## Contributing

Before contributing **please read through everything in [Contributing](docs/contributing.md)**.

**[⬆ back to top](#table-of-contents)**

## Run The Application

```bash
docker compose up
```

This will automatically start the flask application via a local server at localhost:443 and the mysql database.

**[⬆ back to top](#table-of-contents)**

## Additional Docs

- [Contributing](docs/contributing.md)
- [Prerequisites](docs/prerequisites.md)
- [Database Setup](docs/database-setup.md)
- [Node Version](docs/node-version.md)

**[⬆ back to top](#table-of-contents)**
