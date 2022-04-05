from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='mindmap',
   version='1.0',
   description='MindMap test',
   license="Mine",
   long_description=long_description,
   author='Slasri',
   packages=['src']
)