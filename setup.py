from setuptools import setup, find_packages


def readfile(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines()


readme = readfile('README.rst')
requires = readfile('requirements.txt')
version = readfile('VERSION')[0].strip()

setup(
    name='sphinxcontrib-book',
    version=version,
    url='https://github.com/AstroMatt/sphinxcontrib-book',
    download_url='https://pypi.org/project/sphinxcontrib-book/',
    license='MIT',
    author='Matt Harasymczuk',
    author_email='matt@astrotech.io',
    description=readme[1],
    long_description='\n'.join(readme[3:]),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)