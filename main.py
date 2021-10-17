def print_tree(root: str, directories: list) -> str:
    output = f"{root}/\n"
    directory = directories.pop(0)
    while directories:
        output += f"│\n├── {directory}/\n"
        directory = directories.pop(0)
    output += f"│\n└── {directory}/\n"

    return output


if __name__ == "__main__":
    sample_data = {"root": "src", "directories": ["components", "api", "views"]}
    tree_output = print_tree(**sample_data)
    print(tree_output)
