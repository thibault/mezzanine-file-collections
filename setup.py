import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'mezzanine-file-collections',
    version = '1.0',
    packages = ['mezzanine_file_collections'],
    include_package_data = True,
    license = 'WTFPL',
    description = 'A simple file collection page type for Mezzanine',
    long_description = README,
    url = 'https://github.com/thibault/mezzanine-file-collections',
    author = 'Thibault Jouannic',
    author_email = 'thibault@miximum.fr',
    setup_requires=('setuptools'),
    requires = ('mezzanine'),
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
