# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='smcal',
    version='0.1.0',
    description='smcal smart calculator',
    long_description=readme,
    author='Levente Laszlo',
    author_email='laszlolevente@gmail.com',
    url='https://github.com/llevi/smcal',
    license=license,
    packages=find_packages(),
    scripts=['scripts/smcal']
)

