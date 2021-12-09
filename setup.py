from setuptools import setup

setup(
    name = "ary",
    version = "0.1.0",
    description = "Project setupper",
    author = "JeffTheK",
    url = "https://github.com/JeffTheK/ary",
    packages = ["ary"],
    entry_points = {
        'console_scripts': [
            'ary = ary.__main__:main'
        ]
    },
    package_data = {
        "ary": [
            "data/**"
        ]
    }
)