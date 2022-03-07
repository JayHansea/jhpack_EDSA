from setuptools import setup, find_packages

setup(
    name='jhpack',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Tochukwu\'s first python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/<package-name>',
    author='Tochukwu Ezeokafor',
    author_email='ezeokafortochukwu@gmail.com'
)