from setuptools import setup

setup(
    name="market_alert_bot_wa",
    version="1.0.0",
    author="Carlos J. Ramirez",
    author_email="cramirez@mediabros.com",
    description="WhatsApp Market Alert BOT in Python",
    packages=["market_alert_bot_wa"],
    install_requires=["requests", "fastapi", "a2wsgi"],
    zip_safe=False
)
