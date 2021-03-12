import setuptools

setuptools.setup(
    name='FuzzySearchPy',
    version='0.0.2',
    packages=setuptools.find_packages(exclude=['tests*']),
    license='WTFPL',
    description='A port of FuzzySearch from JS',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://github.com/doomium-chloride/fuzzy-search-py',
    author='doomium-chloride'
)