import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
    

with open("requirements.txt", "r") as fh:
    requirements = fh.read()
    
setuptools.setup(
    name = "preprocess_csl",
    version = "0.1.0",
    author = "Jubayer Al Mahmud",
    author_email = "jubayear.iu0708@gmail.com",
    description = "A simple text preprocessing package for CSL data", 
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Jubayer07/preprocess_csl",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    #python_requires = ">=3.6",
    #python_requires=">=3.6,<3.14",
    python_requires=">=3.6",
    install_requires = requirements,
    include_package_data=True
)        