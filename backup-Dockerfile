FROM odoo:9

# Config python utf8
# RUN sed  -i 's+encoding = "ascii"+encoding = "utf8"+g' /usr/local/lib/python2.7/site.py

#apt install python-magic python-pyproj

# Install any needed packages
RUN pip install pyproj unittest2
RUN pip install workalendar workdays python-magic
RUN pip install appy numpy