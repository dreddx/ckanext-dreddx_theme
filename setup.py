from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='''ckanext-dreddx_theme''',
    version='0.0.1',
    description='''Custom theme for dreddx CKAN site''',
    long_description='''
    ''',
    url='https://github.com/dreddx/ckanext-dreddx_theme',
    author='''Dreddx''',
    author_email='''
    ''',
    license='AGPL',
    classifiers=[],
    keywords='''CKAN dreddx theme''',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    namespace_packages=['ckanext'],

    install_requires=[
      # CKAN extensions should not list dependencies here, but in a separate
      # ``requirements.txt`` file.
      #
      # http://docs.ckan.org/en/latest/extensions/best-practices.html#add-third-party-libraries-to-requirements-txt
    ],

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    include_package_data=True,

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points='''
        [ckan.plugins]
        dreddx_theme=ckanext.dreddx_theme.plugin:DreddxThemePlugin
    ''',
)


