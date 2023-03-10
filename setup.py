from typing import List

from setuptools import find_packages, setup


HYPEN_E_DOT = "-e ."


def get_requirements(filepath: str) -> List[str]:
    """
    this function returns list of requirements
    :param filepath:
    :return:
    """
    with open(filepath) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements


setup(
    name="ml_project",
    version="0.0.1",
    author="Tamil",
    author_email="tamilselvan402@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
