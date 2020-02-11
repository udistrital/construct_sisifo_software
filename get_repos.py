import os
import git
from git import Repo
# sudo pip install gitpython

# detect the current working directory and print it
path = os.getcwd()
print ("The current working directory is %s" % path)
folder = "extra-addons"
folderFin = path + '/' + folder

if os.path.isdir(folderFin):
    try:
        os.rmdir(folderFin)
    except OSError:
        print ("Deletion of the directory %s failed" % folderFin)
    else:
        print ("Successfully clean the directory %s" % folderFin)

    try:
        os.makedirs(folderFin)
    except OSError:
        print ("Creation of the directory %s failed" % folderFin)
    else:
        print ("Successfully created the directory %s" % folderFin)
else:
    try:
        os.makedirs(folderFin)
    except OSError:
        print ("Creation of the directory %s failed" % folderFin)
    else:
        print ("Successfully created the directory %s" % folderFin)

git.Git("./extra-addons/").clone("https://github.com/udistrital/odoo-idu-addons-publico.git")
git.Git("./extra-addons/").clone("https://github.com/udistrital/openerp-utils.git")
git.Git("./extra-addons/").clone("https://github.com/udistrital/odoo-colombia.git")
Repo.clone_from(
    'https://github.com/udistrital/geospatial.git',
    './extra-addons/geospatial/',
    branch='9.0'
)
