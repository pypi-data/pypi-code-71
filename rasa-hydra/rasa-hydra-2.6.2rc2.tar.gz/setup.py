import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

# Avoids IDE errors, but actual version is read from version.py
__version__ = None
with open("dialog_manager/version.py") as f:
    exec (f.read())

# Get the long description from the README file
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

tests_requires = [
    "pytest~=5.0",
    "pytest-cov~=2.7",
    "pytest-localserver~=0.5.0",
    "pytest-sanic~=1.0.0",
    "responses~=0.9.0",
    "freezegun~=0.3.0",
    "nbsphinx>=0.3",
    "aioresponses~=0.6.0",
    "moto~=1.3.8",
    "fakeredis~=1.4",
]

install_requires = [
    "requests>=2.20",
    "boto3~=1.9",
    "matplotlib~=3.0",
    "attrs>=18",
    "jsonpickle~=1.1",
    "redis~=3.5.0",
    "pymongo[tls,srv]~=3.8",
    "numpy==1.16.4",
    "scipy~=1.2",
    "tensorflow~=1.15.0",
    "tensorflow-datasets~=3.2.0",
    # absl is a tensorflow dependency, but produces double logging before 0.8
    # should be removed once tensorflow requires absl > 0.8 on its own
    "absl-py~=0.9.0",
    # setuptools comes from tensorboard requirement:
    # https://github.com/tensorflow/tensorboard/blob/1.14/tensorboard/pip_package/setup.py#L33
    "setuptools >= 41.0.0",
    "tensorflow-probability~=0.7.0",
    "tensor2tensor~=1.14.0",
    "gym<=0.15.4",
    "apscheduler~=3.0",
    "tqdm~=4.0",
    "networkx~=2.3.0",
    "fbmessenger~=6.0",
    "pykwalify~=1.7.0",
    "coloredlogs~=10.0",
    "scikit-learn~=0.20.2",
    "ruamel.yaml~=0.15.0",
    "scikit-learn~=0.20.0",
    "slackclient~=1.3",
    "python-telegram-bot~=11.0",
    "twilio~=6.0",
    "webexteamssdk~=1.1",
    "mattermostwrapper~=2.0",
    "rocketchat_API~=0.6.0",
    "colorhash~=1.0",
    "pika~=1.0.0",
    "jsonschema~=3.0",
    "packaging~=19.0",
    "gevent~=1.4",
    "pytz~=2019.1",
    "python-dateutil~=2.8",
    "rasa-sdk~=1.5.0",
    "colorclass~=2.2",
    "terminaltables~=3.1",
    "sanic==19.12.2",
    "sanic-cors==0.9.9.post1",
    "sanic-jwt~=1.3",
    # needed because of https://github.com/huge-success/sanic/issues/1729
    "multidict==4.6.1",
    "aiohttp~=3.5",
    "questionary>=1.1.0",
    "python-socketio~=4.6.1",
    # the below can be unpinned when python-socketio pins >=3.9.3
    "python-engineio~=3.14.2",
    "pydot~=1.4",
    "pymssql==2.1.4",
    "async_generator~=1.10",
    "SQLAlchemy~=1.3.0",
    "kafka-python~=1.4",
    "sklearn-crfsuite~=0.3.6",
    "prompt-toolkit==2.0.10",
    #"jaeger_client~=4.2.0",
    "opentracing_instrumentation~=3.2.1",
    "psycopg2-binary~=2.8.2",
    "prometheus_client~=0.7.1",
    "sanic_prometheus~=0.2.1",
    "aredis~=1.1.5",
    "aioredis~=1.3.1",
    "redis-py-cluster==2.1.0",
    "json-logging~=1.2.7",
    "pyinstrument~=3.2.0",
    "PyJWT~=1.7",
    "gast==0.2.2",
    "cloudpickle~=1.2.0",
    "h2==3.0.0",
    "dopamine-rl~=3.0.0",
    "h5py~=2.10.0",
    "tensorflow-hub~=0.10.0"
]

extras_requires = {
    "test": tests_requires,
    "spacy": ["spacy>=2.1,<2.2"],
    "convert": ["tensorflow_text~=1.15.1", "tensorflow_hub~=0.6.0"],
    "mitie": ["mitie"],
    "sql": ["psycopg2~=2.8.2", "SQLAlchemy~=1.3"],
}

setup(
    name="rasa-hydra",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        # supported python versions
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.6",
    packages=find_packages(exclude=["tests", "tools", "docs", "contrib"]),
    entry_points={"console_scripts": ["rasa=rasa.__main__:main"]},
    version=__version__,
    install_requires=install_requires,
    tests_require=tests_requires,
    extras_require=extras_requires,
    include_package_data=True,
    description="Forked from the open source machine learning framework, Rasa",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Versay Solutions, LLC",
    author_email="",
    maintainer="Chiajun Tai",
    maintainer_email="ctai@versay.com",
    keywords="nlp machine-learning machine-learning-library bot bots "
    "botkit rasa-hydra conversational-agents conversational-ai chatbot"
    "chatbot-framework bot-framework",
)

print ("\nWelcome to Rasa-Hydra!")
print (
    "If you have any questions, please visit the official Rasa documentation page: https://rasa.com/docs/"
)
print("or join the community discussions on https://forum.rasa.com/")
