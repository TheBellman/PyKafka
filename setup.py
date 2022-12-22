import os
from setuptools import setup, find_packages

with open("README.md") as stream:
    long_description = stream.read()

# read in the dependencies from the virtualenv requirements file
dependencies = []
filename = os.path.join("requirements.txt")
with open(filename, 'r') as stream:
    for line in stream:
        package = line.strip().split('#')[0]
        if package:
            dependencies.append(package)

setup(
    name='PyKafka',
    version='1.0.0a1',
    description='Simple demonstration of Kafka with Avro',
    long_description=long_description,
    author='Robert Hook',
    author_email='rahook@gmail.com',
    url='https://github.com/TheBellman/PyKafka',
    license='License :: OSI Approved :: Apache Software License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
    ],
    project_urls={
        'Documentation': 'https://github.com/TheBellman/PyKafka',
        'Source': 'https://github.com/TheBellman/PyKafka',
    },
    packages=find_packages(include=['pykafka', 'pykafka.*']),
    install_requires=dependencies,
    python_requires='>=3.9.*',
    entry_points={
        "console_scripts": [
            "PyKafka=pykafka.PyKafka:main",
        ]
    },
)
