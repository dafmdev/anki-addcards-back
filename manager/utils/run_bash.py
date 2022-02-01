import os


def create_environment_variables(AWS_KEY: dict) -> None:
    for k, v in AWS_KEY.items():
        os.environ[k] = v
