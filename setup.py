import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nba_player",
    version="0.6.4",
    author="Avyay Varadarajan",
    author_email="avyayv@gmail.com",
    description="Get all NBA player data into JSON format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avyayv/python_nba_players",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
