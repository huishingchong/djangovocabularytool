UNDERLINE_SYMBOL = "-"


def print_title(logline):
    print(logline)
    print(len(logline) * UNDERLINE_SYMBOL)


def print_blank_line():
    print("")


def print_overview(
    installed,
    packages_not_needed_by_other,
    packages_needed_by_other,
    package_dependencies,
):
    print_title("Installed packages:")
    print(", ".join(sorted(installed)))
    print_blank_line()

    print_title("No package depends on these packages:")
    print(", ".join(sorted(packages_not_needed_by_other)))
    print_blank_line()

    print_title("These packages are needed by other packages:")
    for package, needed_by in sorted(packages_needed_by_other.items()):
        print(f"Package {package} is needed by: {', '.join(needed_by)}")
    print_blank_line()

    print_title("These packages depend on other packages:")
    for package, package_dependencies in sorted(package_dependencies.items()):
        print(
            f"Package {package} depends on: {', '.join(package_dependencies)}",
        )
    print_blank_line()
