import os
from setuptools import find_packages, setup


def get_version():
    current_dir = os.path.dirname(os.path.realpath(__file__))

    return open(
        os.path.abspath(os.path.join(current_dir, 'VERSION'))
    ).read().strip()


setup(
    name="pants",
    description="Example of a pants project.",
    url="http://www.rapidsos.com",
    author="RapidSOS, Engineering",
    packages=find_packages(),
    version=get_version(),
    classifiers=["Framework :: Pytest"]
)
