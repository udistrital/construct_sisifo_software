#!/bin/sh
pip install zeep
chown odoo.odoo /opt/odoo-attachments/data/ -R
chown odoo.odoo /var/log/odoo/ -R
exec su odoo -c "/usr/bin/python /usr/bin/odoo.py --config /etc/odoo/openerp-server.conf --logfile /var/log/odoo/odoo-server.log"

