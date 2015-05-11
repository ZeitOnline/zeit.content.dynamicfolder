from setuptools import setup, find_packages


setup(
    name='zeit.content.dynamicfolder',
    version='0.1.0.dev0',
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
        'plone.testing',
        'setuptools',
        'zeit.cms',
        'zeit.connector',
        'zope.container',
        'zope.interface',
        'zope.schema',
        'zope.security',
    ],
    entry_points={
    },
)
