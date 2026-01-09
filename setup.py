from setuptools import setup, find_packages

setup(
    name='neroghost',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'neroghost=neroghost.main:main',
        ],
    },
    install_requires=[
        # coloque libs externas aqui se houver
    ],
    python_requires='>=3.8',
)
