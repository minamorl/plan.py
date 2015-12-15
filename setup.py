from setuptools import setup, find_packages

app_name = "plan"

setup(
    name="plan-py",
    author="minamorl",
    author_email="minamorl@minamorl.com",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['{app_name} = {app_name}.__main__:main'.format(app_name=app_name)]
    },
)
