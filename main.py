def printTree(root: str, directories: list):
    output = f"{root}/\n"
    directory = directories.pop(0)
    while directories:
        output += f"│\n├── {directory}/\n"
        directory = directories.pop(0)
    output += f"│\n└── {directory}/\n"

    print(output)

if __name__ == '__main__':
    sample_data = {
        "root": "src",
        "directories": ["components", "api", "views"]
    }
    printTree(**sample_data)