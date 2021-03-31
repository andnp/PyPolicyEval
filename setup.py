from setuptools import setup, find_packages

setup(
    name='PyPolicyEval',
    url='https://github.com/andnp/PyPolicyEval.git',
    author='Andy Patterson',
    author_email='andnpatterson@gmail.com',
    packages=find_packages(exclude=['tests*', 'scripts*']),
    install_requires=[
        "numpy>=1.19.5",
        "numba>=0.52.0",
        "PyRlEnvs @ git+ssh://git@github.com/andnp/PyRlEnvs@0.2#egg=PyRlEnvs"
    ],
    version=.1,
    license='MIT',
    description='Several utility methods for evaluating policies',
    long_description='todo',
)
