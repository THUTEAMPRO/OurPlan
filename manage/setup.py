from setuptools import setup

setup_args = dict(
    name="OurPlan",
    install_requires=[
        'Flask>=0.9',
        'Flask-Login>=0.2.7',
        ]
    )
if __name__ == "__main__":
    setup(**setup_args)
