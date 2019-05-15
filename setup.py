from setuptools import setup, find_packages

setup(
    name='EventCounter',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Package to count food on your event',
    long_description=open('README.md').read(),
    url='https://github.com/zheka-kudr/EventCounter',
    author='Yauheni Kudrytski',
    author_email='235306@student.pwr.edu.pl'
)
