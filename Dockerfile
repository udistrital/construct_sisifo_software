FROM odoo:9

# Config python utf8
RUN sed  -i 's+encoding = "ascii"+encoding = "utf8"+g' /usr/local/lib/python2.7/site.py