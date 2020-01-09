try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup

    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

from poly import has_cuda
import platform

def cuda_and_linux():
    return has_cuda() and platform.system() == "Linux"

requirements = [
    "tensorflow-gpu" if has_cuda() else "tensorflow",
    "numba",
    "spacy",
    "keras",
    "sklearn",
    "networkx",
    "pandas",
    "numpy"
]

if has_cuda():
    requirements = requirements + ["pyCuda"]

if cuda_and_linux():
    requirements = requirements + [
        "cuDF",
        "cuML",
        "cuSpacial",
        "cuGraph"
    ]
elif platform.system() == "Windows":
    pass
elif platform.system() == "Darwin":
    requirements = requirements + ["plaidml", "plaidml-keras"]


setup(
    name = "poly",
    version = "0.0.1",
    url = 'https://github.com/mattpaletta/poly',
    packages = find_packages(),
    include_package_data = True,
    install_requires = requirements,
    author = "Matthew Paletta",
    author_email = "mattpaletta@gmail.com",
    description = "Automatic GPU Acceleration for Python Library.",
    license = "BSD",
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications',
    ],
)
