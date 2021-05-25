from os import environ
from subprocess import run
from typing import List, Optional, Dict


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

    run_command(["echo", "%cd%"])
    run_command(["black", "."])
    run_command(["isort", "."])
    run_command(["pytest", "--black", "--isort", "--pylint", "--mypy", "--cov", "."])


if __name__ == "__main__":
    main()
