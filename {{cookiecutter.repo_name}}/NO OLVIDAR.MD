# Antes de empezar tu proyecto recuerda:

1. Github

git init
git remote add origin remote repository URL

2. Crear ambiente para trabajar
pyenv virtualenv {{cookiecutter.python_version}} {{cookiecutter.repo_name}} 

3. Activar tu ambiente
pyenv activate {{cookiecutter.repo_name}} 

4. Instalar librerías base
make install