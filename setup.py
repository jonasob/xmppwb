# Always prefer setuptools over distutils
# from setuptools import setup, find_packages
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='xmppwb',
    version='0.2.0',
    description='XMPP Webhook Bridge',
    long_description=long_description,

    url='https://github.com/saqura/xmppwb',

    author='saqura',
    author_email='saqura@saqura.xyz',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Communications :: Chat',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    py_modules=["xmppwb"],
    install_requires=['aiohttp', 'pyyaml', 'slixmpp'],
    entry_points={
        'console_scripts': [
            'xmppwb=xmppwb:main',
        ],
    },
)