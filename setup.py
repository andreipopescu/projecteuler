from setuptools import setup, find_packages


setup(
    version='1.0.0',
    script_name='euler',
    name='euler',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'euler = projecteuler.project.main:main',
        ],
    },
)

