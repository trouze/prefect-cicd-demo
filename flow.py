import prefect
from prefect import task, Flow
from prefect.tasks.secrets import PrefectSecret
from prefect.storage.github import GitHub

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello world!")

with Flow("hello-flow") as flow:
    git_secret = PrefectSecret("trouzegithub")
    flow.storage = GitHub(repo="trouze/prefect-orion-demo", path="/flow.py", access_token_secret=git_secret)
    hello_task()
