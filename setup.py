from setuptools import find_packages, setup


setup(
    name = 'corpus',
    packages = find_packages('src'),
    package_dir={'': 'src'}
)
