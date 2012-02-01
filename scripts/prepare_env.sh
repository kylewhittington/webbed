#!/bin/sh -ex

APP_NAME='guideapp'

cd `dirname $0`
cd ..

python scripts/virtualenv.py test
. ./test/bin/activate
pip install -v --requirement `pwd`/$APP_NAME/requirements.txt
pip install epio

cd $APP_NAME
./manage.py syncdb  --settings=local_settings
./manage.py migrate  --settings=local_settings


#./manage.py test

echo "Run source test/bin/activate"
