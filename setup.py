import os
from setuptools import setup

setup(
    name = "Jira Basic Tool",
    author = "Daisy Liu",
    author_email = "daisy.liu@thecarousell.com",
    description = ("An demonstration of how to create bug with Jira python library"),
    install_requires=[
          'JIRA','requests'
      ]
)