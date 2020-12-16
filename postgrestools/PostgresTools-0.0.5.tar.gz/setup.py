from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='PostgresTools',
  version='0.0.5',
  description='Tools to copy database',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Rafael Cardoso',
  author_email='rmcardoso@outlook.com.br',
  license='MIT', 
  classifiers=classifiers,
  keywords='PostgresTools', 
  packages=find_packages(),
  install_requires=[''] 
)
