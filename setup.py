import setuptools

setuptools.setup(
    name="aoc",
    version="0.1.0",
    author="mnc",
    author_email="mnc@mnc.at",
    description="Advent of Code tools",
    install_requires=[
        'requests',
    ],
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'aoc=aoc.aoc:main',
            'get_input=aoc.get_input:main',
        ],
    },
)
