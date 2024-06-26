from setuptools import setup, find_packages
                    
setup(
name="sysall",
version="1.1.13",
author="LixNew",
author_email="lixnew12@gmail.com",
description="Tools to facilitate the use/manipulation of data in the Windows environment",
long_description=open("README.md", encoding="utf-8").read(),
long_description_content_type="text/markdown",
url="https://github.com/LixNew2/SysAll",
packages=find_packages("src"),
package_dir={"": "src"},
classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
],
python_requires=">=3.7",
install_requires=[
    "WMI",
    "getmac",
    "psutil",
    "py-cpuinfo",
    "requests"
],
)

