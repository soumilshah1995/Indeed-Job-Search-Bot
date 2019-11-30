from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="indeedjobsearch",
    version="6.2.0",
    description="""
        Searches 150 + job from indeed websites in 5 seconds    
     """,
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/soumilshah1995/Indeed-Job-Search-Bot/blob/master/README.md",
    author="Soumil Nitin Shah",
    author_email="soushah@my.bridgeport.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["indeedjobsearch"],
    include_package_data=True,
    install_requires=["pandas", "bs4", "requests"]
)