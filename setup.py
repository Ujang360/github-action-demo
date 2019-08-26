from distutils.core import setup

setup(
    name='PyTestDemo',
    version='1.0',
    packages=['pytest_demo'],
    license='MIT',
    entry_points={
        'console_scripts': [
            'runme=pytest_demo:cli',
        ]
    }
)
