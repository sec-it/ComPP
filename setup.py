import setuptools

setuptools.setup(
    name='ComPP',
    version='1.0.1',
    author="Zeecka",
    packages=["ComPP"],
    scripts=["bin/ComPP"],
    install_requires=["argparse", "colorama"],
    license='MIT License',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url = 'https://github.com/sec-it/ComPP',
    project_urls = {
        "Source": "https://github.com/sec-it/ComPP",
        "Tracker": "https://github.com/sec-it/ComPP/issues"
    },
    package_data={
        "ComPP": ["*"]
    },
    python_requires=">=3.7",
)
