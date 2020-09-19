import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easyAPI-greatusername", 
    version="0.0.2",
    author="greatusername",
    author_email="alexander.destefano@gmail.com",
    description="An easier way to use a JSON api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mathstar13/easyAPI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.1',
)