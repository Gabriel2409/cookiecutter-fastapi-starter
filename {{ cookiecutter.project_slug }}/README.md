# {{ cookiecutter.project_name }}

Fastapi starter generated with Gabriel2409/cookiecutter-fastapi-starter

## Install the prerequisites

- python 3.10 or above, for ex with pyenv: https://github.com/pyenv/pyenv

## Get all dependencies

- Run `make install` to create environments and install dependencies
- Don't forget to activate python environment afterwards: `source venv/bin/activate`

Note: look at the `Makefile` to see the details of the installation

## Post installation checks

- Installation should have created a `.env` file in the `{{ cookiecutter.fastapi_app_folder }}` folder.
- Note that there is no sensitive information in this application so you won't need to modify it

## Running the application

- The simplest way is to use vscode task: `Run Fastapi`
  You can check the details of the commands in `.vscode/tasks.json`
- Alternatively,

  - in `{{ cookiecutter.fastapi_app_folder }}` folder, run `uvicorn app.main:app --reload`

- Check that app is running by going to `http://localhost:8000/docs`
