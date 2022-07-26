from multiprocessing import AuthenticationError
from setuptools import setup

setup(
    name="randomrecommender",
    version=0.1,
    description="A simple random movie recommender package",
    author = "Arjun",
    author_email="arjunharidas@hotmail.com",
    url="https://github.com/Ajax121/randomrec",
    packages=["randomrecommender"],
    package_data={"randomrecommender":["data/*.txt"]},
    install_requires = ["numpy","pandas"],
    )