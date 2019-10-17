from setuptools import setup

setup(
    packages=['jenklint'],
    zip_safe=True,
    install_requires=["requests>=2.20.0"],
    entry_points={
        "console_scripts": [
            'jenklint = jenklint.__main__:main'
        ]
    },
)
