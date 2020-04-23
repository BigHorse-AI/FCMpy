import setuptools

def readme():
    with open("README.md", "r") as fh:
        return fh.read()


with open('DEPENDS.txt') as fid:
    INSTALL_REQUIRES = []
    for line in fid.readlines():
        if line == '' or line[0] == '#' or line[0].isspace():
            continue
        INSTALL_REQUIRES.append(line.strip())

setuptools.setup(
    name="fcmbci",
    version="0.0.1",
    author="Samvel Mkhitaryan",
    author_email="mkhitarian.samvel@gmail.com",
    description="Fuzzy Cognitive Maps for Behavior Change Interventions and Evaluation",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/SamvelMK/FcmBci.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=INSTALL_REQUIRES
)