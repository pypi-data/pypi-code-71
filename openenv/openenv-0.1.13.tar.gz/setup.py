import setuptools

# Read the README.md content as the long_description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openenv", # Replace with your own username
    version="0.1.13",
    author="Jianfeng Hou",
    author_email="frankderekdick@gmail.com",
    description="A Python package consisting of open-source implemented environments for reinforcement learning.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neo-derek/open-env",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
    ],
)
