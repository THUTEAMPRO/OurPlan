read -p "Why you need to update the datebase?"
python start.py db migrate -m "$REPLY"
python start.py db upgrade
