import setuptools

setuptools.setup(
    name='ComPP',
    version='1.0',
    author="Zeecka",
    packages=["ComPP"],
    scripts=["bin/ComPP"],
    install_requires=["argparse", "colorama"],
    license='MIT License',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    package_data={
        "ComPP": ["*"]
    },
    python_requires=">=3.7",
)
