# Onlineweb 4
[![Build Status](https://cloud.drone.io/api/badges/dotkom/onlineweb4/status.svg)](https://cloud.drone.io/dotkom/onlineweb4) [![Requirements Status](https://requires.io/enterprise/dotkom/onlineweb4/requirements.svg?branch=develop)](https://requires.io/enterprise/dotkom/onlineweb4/requirements/?branch=develop) [![codecov](https://codecov.io/gh/dotkom/onlineweb4/branch/develop/graph/badge.svg)](https://codecov.io/gh/dotkom/onlineweb4) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


## Frameworks

### Frontend

The frontend code is located in the `assets` folder.
It's a mixture of old jQuery code and newer React code.
The code is built with [webpack](http://webpack.js.org/) and transpiled using [Babel](https://babeljs.io/).

*Some static files are still stored in `files/static`, but should be moved to `assets` and included using webpack*.

### Backend

Python 3 with [Django](https://docs.djangoproject.com/) is used as a backend and is mostly located in the `apps` folder.
Django templates are in `templates` folder.
The API uses [Django REST framework](http://www.django-rest-framework.org/)


## Installation - Git and repository setup
### Setting up your Git user and cloning the repo
```bash
git config core.autocrlf false
git config user.name "<your github username>"
git config user.email your.github@email.com
git clone git@github.com:dotkom/onlineweb4.git
cd onlineweb4
```

## Development environment

The easiest way to get started with development is to use the provided Docker images.
On the other hand on slower machines Docker might be noticeable slower in which case a local installation using virtualenv can be preferred.

### Docker and Docker Compose

To fire up the dev environment, you should use [Docker](https://docs.docker.com/install/). Following that, you will need [docker-compose](https://docs.docker.com/compose/overview/), which can be installed following [this](https://docs.docker.com/compose/install/) guide.

There is a `Makefile` located in the root directory. This can be used to manage the application without direct interaction with `docker`, `docker-compose`, et al.

If you can't use `make`, you can fire up the dev environment by issuing `docker-compose up -d`.

If the site doesn't load properly the first time you are running the project, you might need to restart Docker once by running `docker-compose restart`.

#### Alternative to Docker: Local installation

A few packages are required to build our Python depedencies:

- libjpeg-dev
- ghostscript

If these aren't already installed pip will likely fail to build the packages.

If you are oldschool and like using python virtual envs, just activate your env,
run `pip install -r requirements.txt`, then `python manage.py migrate`, before starting the dev server with `python manage.py runserver`.

Next, you need to fire up the front-end stuff, by running `npm install` followed by `npm start`.

The project should now be available at [http://localhost:8000](http://localhost:8000)

### Setting up Onlineweb4 with Docker and Docker-compose

After installing Docker and docker-compose, Download dependencies by running
```bash
make build
```

You also need to set up the database, by running
```bash
# Enter the bash-terminal in the Docker container
make bash-backend

# Run the migrations
python manage.py migrate
```
For your convenience, you can also just run `make migrate`

To exit the Docker bash-terminal, use `^D` (`ctrl + D`) or `exit`

And to be able to log in, you should create a superuser, a user with all types of permissions by default.
```bash
# If you aren't already in the bash-terminal in Docker
make bash-backend

# Create a super user from inside the container
python manage.py createsuperuser
```
Now follow the instructions by supplying a name, password and an email.

You can then start Onlineweb4 by running

```bash
make start
```

And your local version of Onlineweb4 should be available on [http://localhost:8000](http://localhost:8000)!
You can stop it with `make stop`

To view output from onlineweb4, run `make logs`. To view output from a specific service (e.g. django), use one of the following:
```bash
OW4_MAKE_TARGET=django make logs # for django
OW4_MAKE_TARGET=webpack make logs # for the frontend
```

## CI/CD

Pushes made to the develop branch will trigger a redeployment of the application on [dev.online.ntnu.no](https://dev.online.ntnu.no).

Pull requests trigger containerized builds that perform code style checks and tests. You can view the details of these tests by clicking the "detail" link in the pull request checks status area.

## Tools

Builds will fail if our requirements for code style are not met. To ensure that you adhere to our code guidelines, we recommend you run linting tools locally before pushing your code. This can be done by running `make lint`, and you can automatically fix the backend linting by running `make lint-backend-fix`. Running `make test` will run our tests and linters all at once. Look to our [Makefile](https://github.com/dotkom/onlineweb4/blob/86ef0e267bdad3346a705551d2a3d377b2802d81/Makefile#L55) for more specific commands.

Running `make test` frequently can be quite inefficient, which is why we recommend using editors that support linting your code as you go. For JavaScript, we use [ESLint](https://eslint.org/docs/about/), with editor plugins available [here](https://eslint.org/docs/user-guide/integrations). Correspondingly, we use [stylelint](https://stylelint.io) for our stylesheets, with editor plugins available [here](https://github.com/stylelint/stylelint/blob/master/docs/user-guide/complementary-tools.md#editor-plugins). For Python, we use [Black](https://black.readthedocs.io/en/stable/), [isort](https://github.com/timothycrosley/isort) and [Flake8](http://flake8.pycqa.org/). We highly recommend setting up your editor to automatically fix linting issues, which can be done for [Black](https://black.readthedocs.io/en/stable/editor_integration.html), and [isort](https://github.com/timothycrosley/isort/wiki/isort-Plugins)

### Our recommendation

In dotkom, we find that [PyCharm](https://www.jetbrains.com/pycharm/) is a great IDE that is well suited for contributing to onlineweb4. It'll come with support for ESLint, stylelint, and PEP 8 out of the box, and can be set up to run isort and Flake8 with some ease. We recommend it to our beginners who don't want to spend a lot of time setting up the plugins or extensions mentioned above, or don't have any preferences of their own yet. You can apply for a free student license [here](https://www.jetbrains.com/student/).
