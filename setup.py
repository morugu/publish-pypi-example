from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='publish-pypi-example',
    packages=['pypi_example', 'pypi_example/extention/'],
    version='0.0.2',
    license='MIT',
    install_requires=['requests'],
    author='Shoya Shiraki',
    author_email='shoya.shiraki@gmail.com',
    url='https://github.com/morugu/publish-pypi-example',
    description='Publish PyPI example',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='PyPI Python',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
