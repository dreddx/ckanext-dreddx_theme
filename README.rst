=============
ckanext-dreddx_theme
=============

A plugin with custom theme elements

------------
To-do
------------

* Probably better way to add custom styles to default `main.css` - currently just moved default styles to `dreddx.css`

------------
Installation
------------

To install ckanext-dreddx_theme:

1. Activate your CKAN virtual environment

2. Clone repo to `/usr/lib/ckan/default/src`

3. `cd` into `ckanext-dreddx_theme`

4. Run `python setup.py develop`

Configure CKAN

1. Add ``dreddx_theme`` to the ``ckan.plugins`` setting in your CKAN
   config file

2. Change `ckan.site_logo` to `/images/dreddx_logo.jpeg`

3. Restart CKAN
