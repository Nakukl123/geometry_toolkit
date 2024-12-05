# setup.py

from setuptools import setup, find_packages

setup(
 name="geometry_toolkit",
 version="0.1.0",
 author="Nakul Malik",
 author_email="nakulmalik103@gmail.com",
 description="A toolkit for basic geometric calculations",
 long_description=open("readme.md").read(),
 long_description_content_type="text/markdown",
 url="https://github.com/Nakukl123/geometry_toolkit",
 packages=find_packages(),
 classifiers=[
 "Programming Language :: Python :: 3",
 "License :: OSI Approved :: MIT License",
 "Operating System :: OS Independent",
 ],
 python_requires=">=3.6",
)