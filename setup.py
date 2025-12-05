from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name="beets-copyartifacts3",
    version="0.1.6",
    description="beets plugin to copy non-music files to import path",
    long_description=readme,
    author='Adam Miller',
    author_email='adam@adammiller.io',
    url='https://github.com/adammillerio/beets-copyartifacts',
    download_url='https://github.com/adammillerio/beets-copyartifacts.git',
    license='MIT',
    platforms='ALL',

    packages=['beetsplug'],
    namespace_packages=['beetsplug'],
    install_requires=['beets>=2.4.0'],

    classifiers=[
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ]
)
