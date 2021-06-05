from os import environ
from os.path import dirname, join
from subprocess import run
from typing import Dict, List, Optional


def main():
    def run_command(command: List[str], env: Optional[Dict[str, str]] = None):
        joined_command = " ".join(command)
        working_env = environ.copy()

        if env is None:
            print(f"> {joined_command}")
            run(command, check=True, env=working_env, shell=True)
        else:
            for name, value in env.items():
                working_env[name] = value
            print(f"> {joined_command}  {env}")
            run(command, check=True, env=working_env, shell=True)

    compose_path = join(dirname(__file__), "docker/docker_compose/dev/local_dev_db.yml")

    run_command(["echo", "%cd%"])
    run_command(
        [
            "docker-compose",
            "-f",
            compose_path,
            "up",
            "--build",
            "--remove-orphans",
            "--force-recreate",
        ],
        {
            "BUILDAH_FORMAT": "docker",
            "DOCKER_BUILDKIT": "1",
            "COMPOSE_DOCKER_CLI_BUILD": "1",
        },
    )


if __name__ == "__main__":
    main()
