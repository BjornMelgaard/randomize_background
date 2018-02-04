from setuptools import setup
import os

setup(
    name="randomize_background",
    version="0.0.1",
    author='Sergey Homa',
    author_email="melgaardbjorn@gmail.com",
    packages=[
        'main',
    ],
    entry_points={
        "console_scripts": [
            "randomize_background=main.__main__:main"
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
    ],
    description='randomize_background ~/wallpallers/*',
)
