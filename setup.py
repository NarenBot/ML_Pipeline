from setuptools import setup, find_packages
from typing import List


projectName = "housing-predictor"
versionControl = "0.0.2"
authorName = "Narendran Mudadi"
shortDescription = "This project is meant for ML-Pipeline on Housing Predictor."
packageName = ["housing"]


def getRequirements()->List[str]:
    """
    This function is going to return list of all dependencies suitable for this project.
    """
    with open('requirements.txt') as file:
        return file.readlines().remove("-e .")


setup(
    name= projectName, 
    version= versionControl,
    author= authorName,
    description= shortDescription,
    packages= find_packages(),
    install_requires= getRequirements()
    )