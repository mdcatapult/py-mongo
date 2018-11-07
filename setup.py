# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='klein_mongo',
      version='0.1.1',
      description='MongoDB integration',
      url='http://gitlab.mdcatapult.io/informatics/klein/klein_mongo',
      author='Matt Cockayne',
      author_email='matthew.cockayne@md.catapult.org.uk',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'klein_config',
          'pymongo'
      ],
      zip_safe=True)