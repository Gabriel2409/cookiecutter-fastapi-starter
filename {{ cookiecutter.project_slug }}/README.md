# {{ cookiecutter.project_name }}

Fastapi starter generated with Gabriel2409/cookiecutter-fastapi-starter
TODO: Add postgres dependency + test containers
<https://samanta-reinosoa.medium.com/testing-fastapi-with-testcontainers-in-gitlab-b7c62068aeef>

## Install

### Using devcontainers (Easiest)

- Use vscode devcontainers extension and open the project in a devcontainer
- It should install everything for you

Note: look at the `Makefile` to see the details of the installation

### On your local machine

Similar to devcontainers but you must make sure you have the prerequisites installed:

- `uv`: `https://docs.astral.sh/uv/`

Then you need to manually run `make install` to create environments and install dependencies

## Post installation checks

- Installation should have created a `.env` file in the `{{ cookiecutter.fastapi_app_folder }}` folder.
- Note that there is no sensitive information in this application so you won't need to modify it

## Running the application

- The simplest way is to use vscode task: `Run Fastapi`
  You can check the details of the commands in `.vscode/tasks.json`
- Alternatively,

  - in `{{ cookiecutter.fastapi_app_folder }}` folder, run `uv run -- uvicorn app.main:app --reload`

- Check that app is running by going to `http://localhost:8000/docs`

## Alternative

- If you prefer, on your local machine, you can use `docker compose watch` to run the application so that
  you don't have to install python or uv on your machine. The docker version does not use uv but the generated `requirements.txt`.
- Note that you won't get the benefits of devcontainers (intellisense, linter, etc)
  with this method
