import prefect
from prefect import task, Flow
from prefect.storage import GitHub
from prefect.tasks.secrets import PrefectSecret

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello world!")

with Flow("hello-flow") as flow:
    hello_task()

flow.storage = GitHub(repo="trouze/prefect-orion-demo",path="/flow.py",access_token_secret="trouzegithub")
