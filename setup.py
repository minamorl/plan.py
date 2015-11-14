from setuptools import setup, find_packages

app_name = "plan"

setup(
    name="plan-py",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['{app_name} = {app_name}.__main__:main'.format(app_name=app_name)]
    },
)
