try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from EventManager import VERSION


setup(
    name="EventManager",
    version=".".join(VERSION),
    description="My take on a pythonic, and simple event system.",
    author="Jeppe Klitgaard",
    author_email="jeppe@dapj.dk",
    url="https://github.com/dkkline/EventManager",
    packages=["EventManager"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
    ]
)
