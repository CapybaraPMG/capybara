from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="capybara",
    version="0.1.0",
    author="geexphil",
    description="Event apps in Flask Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CapybaraPMG/capybara",
    python_requires=">=3.6",
    packages=find_packages(),
)
