import os
from setuptools import setup

setup(
    name = "Jira Basic Tool",
    author = "Daisy Liu",
    author_email = "daisy.liu@thecarousell.com",
    description = ("An tool to create serveral bug ticket attaching multiple photos merged"),
    install_requires=[
          'JIRA','requests','Image'
      ]
)