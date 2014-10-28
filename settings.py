#!/usr/bin/env python


bind = 'unix:/home/ck/var/run/gunicorn.sock'

workers = 4

# you should change this
user = 'ck'

# maybe you like error
loglevel = 'warning'
errorlog = '-'

secure_scheme_headers = {
    'X-SCHEME': 'https',
}
x_forwarded_for_header = 'X-FORWARDED-FOR'
