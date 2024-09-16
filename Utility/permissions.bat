set /p env_name="Enter your Conda Env Name: "
call activate %env_name%
set /p project_name="Enter your Django Project Name: "
call SET project_name=%project_name%
cd ..
call python manage.py shell < utility_scripts\script.py
PAUSE
