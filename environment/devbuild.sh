. /home/wger/venv/bin/activate
cd /home/wger/
rm -r -f /home/wger/src/
ls -l
git clone https://github.com/lukehoulihan/fitfilment.git /home/wger/src/
cd /home/wger/src/
/home/wger/venv/bin/pip install -r requirements.txt
/home/wger/venv/bin/python3.5 setup.py develop

wger create_settings --settings-path /home/wger/src/settings.py \
  --database-type postgresql --environment dev --database-pass wger \
wger bootstrap --settings-path /home/wger/src/settings.py \
  --address http://dev.fitfilment.com --port 80 --no-start-server
python manage.py collectstatic -f
