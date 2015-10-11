from setuptools import setup

setup_args = dict(
    name="OurPlan",
    install_requires=[
        'Flask>=0.9',
        'Flask-Login>=0.2.7',
        'Flask-Bootstrap>=3.0.3.1',
        'Flask-Mail==0.9.0',
        'Flask-Migrate==1.1.0',
        'Flask-Moment==0.2.0',
        'Flask-SQLAlchemy==1.0',
        'Flask-Script==0.6.6',
        'Flask-WTF==0.9.4',
        'Jinja2==2.7.1',
        'Mako==0.9.1',
        'MarkupSafe==0.18',
        'SQLAlchemy==0.8.4',
        'WTForms==1.0.5',
        'Werkzeug==0.9.4',
        'alembic==0.6.2',
        'blinker==1.3',
        'itsdangerous==0.23'
        ]
    )
if __name__ == "__main__":
    setup(**setup_args)
