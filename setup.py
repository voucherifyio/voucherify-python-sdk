import sys
import os
from setuptools import setup

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'voucherify'))

__version__ = '2.1.0'
__pypi_username__ = 'voucherify'
__pypi_packagename__ = 'voucherify'
__github_username__ = 'voucherifyio'
__github_reponame__ = 'voucherify-python-sdk'

long_description = '''
    The Voucherify REST SDK provides Python APIs to create, process and manage vouchers.
    1. https://github.com/voucherifyio/voucherify-python-sdk/ - README and Samples
    2. https://voucherify.readme.io/ - API Reference
  '''

setup(
    name=__pypi_packagename__,
    version=__version__,
    author='Voucherify',
    author_email='it@voucherify.io',
    packages=['voucherify'],
    scripts=[],
    url='https://github.com/' + __github_username__ + '/' + __github_reponame__,
    license='MIT',
    description='The Voucherify REST SDK provides Python APIs to create, process and manage vouchers.',
    long_description=long_description,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=['requests>=1.0.0', 'six>=1.0.0'],
    keywords=['voucherify', 'rest', 'sdk']
)
