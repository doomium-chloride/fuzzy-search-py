import setuptools

setuptools.setup(
    name='FuzzySearchPy',
    version='0.0.7',
    package_dir={"": "FuzzySearchPy"},
    packages=setuptools.find_packages(where="FuzzySearchPy"),
    license='WTFPL',
    description='A port of FuzzySearch from JS',
    long_description=open('readme.md').read(),
    url='https://github.com/doomium-chloride/fuzzy-search-py',
    author='doomium-chloride',
    author_email='evilsmellingliquid@gmail.com'
)