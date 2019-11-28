import git
from git import Repo
# sudo pip install gitpython


git.Git("./extra-addons/").clone("https://github.com/udistrital/odoo-idu-addons-publico.git")
git.Git("./extra-addons/").clone("https://github.com/udistrital/openerp-utils.git")
git.Git("./extra-addons/").clone("https://github.com/udistrital/odoo-colombia.git")
git.Git("./extra-addons/").clone("https://github.com/jjvargass/mspi-software.git")
Repo.clone_from(
    'https://github.com/udistrital/geospatial.git',
    './extra-addons/geospatial/',
    branch='9.0'
)
