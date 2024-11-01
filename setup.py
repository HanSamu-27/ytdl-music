from setuptools import setup, find_packages

setup(
    name='ytdl-music',
    version='6.6.6',
    description='Descarga de Audios Para YT',
    author='@Samush$_',
    author_email='samutrrs.fs@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
