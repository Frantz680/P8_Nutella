export DJANGO_SETTINGS_MODULE="DashbordDevise.settings.__init__.py"
export SECRET_KEY="key123456"
export DB_NAME="purbeurre"
export DB_USER="frantz"
export DB_PASSWORD="741852963"

cd /home/frantz/disquaire/
source /home/frantz/disquaire/.venv/bin.activate
python3 /home/frantz/disquaire/manage.py create_db_food