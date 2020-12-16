from setuptools import setup
from setuptools import find_packages

name = 'get-gecko-driver'
version = '0.1.0'

with open('README.md', 'r') as fh:
    long_description = fh.read()

requires = [
    'bs4>=0.0.1',
    'requests>=2.25.0',
    'colorama>=0.4.4',
    'urllib3>=1.26.2'
]

setup(
    name=name,
    version=version,
    author='Zairon Jacobs',
    author_email='zaironjacobs@gmail.com',
    description='A tool to download GeckoDriver.',
    long_description=long_description,
    url='https://github.com/zaironjacobs/get-gecko-driver',
    download_url='https://github.com/zaironjacobs/get-gecko-driver/archive/v' + version + '.tar.gz',
    keywords=['gecko', 'geckodriver', 'download', 'web', 'driver', 'tool', 'get'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [name + '=get_gecko_driver.app:main'],
    },
    install_requires=requires,
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Natural Language :: English'
    ],
    python_requires='>=3',
)
