from setuptools import setup, find_packages
setup(
    name = "aminatorplugins_chef",
    version = "0.1",
    packages = find_packages(),
    namespace_packages = ( 'aminatorplugins', 'aminatorplugins.provisioner'),

    data_files = [
        ('/etc/aminator/plugins', ['default_conf/aminatorplugins.provisioner.chef_zero.yml']),
    ],

    entry_points = {
       'aminator.plugins.provisioner': [
           'chef_zero = aminatorplugins.provisioner.chef_zero:ChefProvisionerPlugin',
       ],
    },

    # metadata for upload to PyPI
    author = "Asbjorn Kjaer",
    author_email = "bunjiboys@bunjiboys.dk",
    description = "Chef Solo provisioner for Netflix's aminator",
    license = "Apache 2.0",
    keywords = "aminator plugin chef-solo chef solo",
)
