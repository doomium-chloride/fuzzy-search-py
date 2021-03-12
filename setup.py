import setuptools

setuptools.setup(
    name='FuzzySearchPy',
    version='0.0.3',
    packages=setuptools.find_packages(exclude=['tests*','env*','.vscode*','__pycache__','dist*'], where="src"),
    license='WTFPL',
    description='A port of FuzzySearch from JS',
    long_description=open('readme.md').read(),
    install_requires=['numpy'],
    url='https://github.com/doomium-chloride/fuzzy-search-py',
    author='doomium-chloride'
)