from setuptools import setup, find_packages


setup(
    name='zeit.content.dynamicfolder',
    version='1.2.7.dev0',
    author='gocept, Zeit Online',
    author_email='zon-backend@zeit.de',
    url='http://www.zeit.de/',
    description="vivi Content-Type DynamicFolder",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='BSD',
    namespace_packages=['zeit', 'zeit.content'],
    install_requires=[
        'grokcore.component',
        'jinja2',
        'lxml',
        'mock',
        'plone.testing',
        'setuptools',
        'zeit.cms >= 3.0.dev0',
        'zeit.connector',
        'zeit.content.cp',
        'zeit.content.rawxml',
        'zeit.seo',  # testing only
        'zope.app.locking',
        'zope.component',
        'zope.container',
        'zope.formlib',
        'zope.interface',
        'zope.schema',
        'zope.security',
    ],
    entry_points={
    },
)
