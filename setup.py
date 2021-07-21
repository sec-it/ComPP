import setuptools

setuptools.setup(
    name='ComPP',
    version='1.0.3',
    author="Zeecka",
    packages=["ComPP"],
    scripts=["bin/compp"],
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
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation',
        'Topic :: Security'
        ],
)
