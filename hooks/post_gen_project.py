from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

# -----------------------------------------------------------------------------
# Utility functions
# -----------------------------------------------------------------------------


def remove_open_source_files():
    """Remove open source files from generated project."""
    file_names = ["CONTRIBUTORS.txt", "LICENSE"]
    for file_name in file_names:
        Path(PROJECT_DIRECTORY / file_name).unlink()


def remove_gplv3_files():
    """Remove GPL v3 files from generated project."""
    file_names = ["COPYING"]
    for file_name in file_names:
        Path(PROJECT_DIRECTORY / file_name).unlink()


def remove_file(filepath):
    """Remove file from generated project."""
    Path(PROJECT_DIRECTORY / filepath).unlink()


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


def main():
    """Main entry point."""

    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_open_source_files()

    if "{{ cookiecutter.open_source_license}}" != "GPLv3":
        remove_gplv3_files()

    print(SUCCESS + "Project initialized, keep up the good work!" + TERMINATOR)


if __name__ == "__main__":
    main()
