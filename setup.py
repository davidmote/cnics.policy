from setuptools import setup, find_packages
import os

version = '0.1.0'

setup(
    name='cnics.policy',
    version=version,
    description='The collection of products required for the CNICS website',
    classifiers=[
        'Framework :: Plone',
        'Programming Language :: Python',
        ],
    keywords='',
    author='BEAST Core Development Team',
    author_email='beast@ucsd.edu',
    url='https://github.com/beastcore/cnics.policy',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['cnics'],
    package_dir={'':'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Plone',
        'Pillow',
        'collective.uploadify',
        'collective.indexing',
        'jyu.z3cform.datepicker',
        'plone.app.caching',
        'plone.app.ldap',
        'beast.securelogin',
        'beast.cnics.sequencedb',
        ],
    extras_require=dict(
        test=['plone.app.testing'],
        ),
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
