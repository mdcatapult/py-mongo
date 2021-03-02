# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


__version__ = ''
exec(open("./src/version.py").read())
if __version__ == '':
    raise RuntimeError("unable to find application version")

setup(name='klein_mongo',
      version=__version__,
      description='MongoDB integration',
      url='http://gitlab.mdcatapult.io/informatics/klein/klein_mongo',
      author='Medicines Discovery Catapult',
      author_email='SoftwareEngineering@md.catapult.org.uk',
      license='MIT',
      packages=find_packages('src'),
      package_dir={'':'src'},
      install_requires=[
          'klein_config~=3.0',
          'pymongo[srv]~=3.11',
      ],
      zip_safe=True)
