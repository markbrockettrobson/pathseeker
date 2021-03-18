import os


def main():
    def run_command(command: str):
        print(f"> {command}")
        os.system(command)

    run_command("echo %cd%")
    run_command("python -m black .")
    run_command("python -m isort .")
    run_command("python -m pytest --black --isort --pylint --mypy --cov .")


if __name__ == "__main__":
    main()
