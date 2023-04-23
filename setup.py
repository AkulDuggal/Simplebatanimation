from setuptools import setup, find_packages

setup(
    name='bat',
    version='0.1',
    packages=find_packages(),
    install_requires=['pip>=22.3.1','setuptools>=65.5.0','wheel>=0.40.0'],
    entry_points={},
    author='akul',
    author_email='akulduggal46@gmail.com',
    description='This is just a test',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AkulDuggal/Simplebatanimation',
    license='free',
    classifiers=[],
)
