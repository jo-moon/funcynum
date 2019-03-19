from setuptools import setup, find_packages

setup(
    name='funcynum',
    version='0.3',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='recursion: a directory of recursive functions. sorting: a directory of functions to sort lists',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/jo-moon/funcynum',
    author='Joanne Moonsamy',
    author_email='joanne.moonsamy@gmail.com'
)
