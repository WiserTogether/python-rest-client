import os
from setuptools import setup, find_packages

ROOT = os.path.abspath(os.path.dirname(__file__))

setup(
    name='python-rest-client',
    version='0.0.svn.13.1',
    description='Python REST Client.',
    long_description=open(os.path.join(ROOT, 'README.rst')).read(),
    author="Ben O'Steen",
    author_email='',
    maintainer='Erik LaBianca',
    maintainer_email='erik.labianca@gmail.com',
    url='https://github.com/easel/python-rest-client',
    license='FedoraCommons',
    include_package_data=True,
    packages=('python_rest_client',),
    install_requires=['httplib2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Fedora Commons',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
