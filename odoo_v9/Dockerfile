FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive

# Install the default packages
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y \
    vim cron supervisor postgresql-client python-pip python-dev \
    node-less python-babel python-dateutil python-decorator python-docutils \
    python-feedparser python-imaging python-jinja2 python-ldap \
    python-mako python-mock python-openid python-passlib python-psutil \
    python-psycopg2 python-pychart python-pydot python-pyparsing python-pypdf \
    python-reportlab python-suds python-unittest2 python-shapely\
    python-libxslt1 python-lxml python-pyproj python-magic python-matplotlib \
    fontconfig fontconfig-config fonts-dejavu-core fonts-liberation ghostscript \
    graphviz gsfonts libart-2.0-2 libavahi-client3 libavahi-common-data \
    libavahi-common3 libcairo2 libcdt5 libcgraph6 libcups2 libcupsfilters1 \
    libcupsimage2 libdatrie1 libfontconfig1 libgd3 libglib2.0-0 libglib2.0-data \
    libgraphite2-3 libgs9 libgs9-common libgvc6 libgvpr2 libharfbuzz0b libice6 \
    libidn11 libijs-0.35 libjbig2dec0 libjs-jquery libltdl7 libpango-1.0-0 \
    libpangocairo-1.0-0 libpangoft2-1.0-0 libpathplan4 libpixman-1-0 libsm6 \
    libthai-data libthai0 libvpx1 libx11-6 libx11-data libxau6 libxaw7 \
    libxcb-render0 libxcb-shm0 libxcb1 libxdmcp6 libxext6 libxmu6 libxpm4 \
    libxrender1 libxt6 libyaml-0-2 poppler-data python-antlr zlib1g-dev libjpeg8-dev\
    python-egenix-mxdatetime python-egenix-mxtools python-mako python-mock \
    python-openid python-openssl python-passlib python-psutil python-psycopg2 \
    python-pychart python-pydot python-pyinotify python-pyparsing python-pypdf \
    python-renderpm python-reportlab python-reportlab-accel python-suds \
    python-support python-vatnumber python-vobject python-werkzeug python-xlwt duplicity \
    python-yaml shared-mime-info x11-common python-gevent python-gevent-websocket && \
# Clean APT temporary files
    apt-get clean && \
    apt-get autoclean

RUN pip install --upgrade setuptools
RUN pip install workalendar workdays appy numpy

ADD http://nightly.odoo.com/9.0/nightly/deb/odoo_9.0.latest_all.deb /root/odoo_v9.deb
RUN dpkg -i /root/odoo_v9.deb

ADD bin/* /usr/local/bin/
RUN chmod a+x /usr/local/bin/*
ADD etc/supervisord/* /etc/supervisor/conf.d/

RUN usermod -s /bin/bash odoo
ADD etc/openerp-server.conf /etc/odoo/
ADD etc/sitecustomize.py /etc/python2.7/


ENTRYPOINT ["/usr/bin/supervisord", "-n"]
