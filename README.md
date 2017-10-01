This is the code for an introductory Django talk I gave for the monthly Central Arkansas Python meetup on 9/28/2017.

Learn more:
- [Meetup](https://www.meetup.com/Python-Artists-of-Arkansas/)
- [Website](http://pyark.org/)

# Setup

```bash
# make a virtualenv (using virtualenv-wrapper)
mkvirtualenv --python=/path/to/python3 djtest

# or if you already have a virtualenv for this project
workon djtest

# clone the repo
git clone git@github.com:calebrash/intro-to-django.git djtest
cd djtest

# install dependencies
pip install -r requirements.txt

# run migrations
./manage.py migrate

# run server
./manage.py runserver
```

Test pages:
- [admin: /admin/](http://localhost:8000/admin/)
- [customers: /customers/](http://localhost:8000/customers/)
