from setuptools import setup

setup(
    name="flaskr",
    packages=["ratetask"],
    include_package_data=True,
    install_requires=[
        "flask",
        "python-dotenv",
        "psycopg2",
        "voluptuous",
    ],
)
