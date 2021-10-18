class DirecTree:
    def __init__(self, root: str):
        self.root = root

    def print_tree(self, directories: list) -> str:
        output = f"{self.root}/\n"
        directory = directories.pop(0)
        while directories:
            output += f"│\n├── {directory}/\n"
            directory = directories.pop(0)
        output += f"│\n└── {directory}/\n"

        return output


if __name__ == "__main__":
    sample_directories = ["components", "api", "views", "helpers"]

    tree_output = DirecTree("src").print_tree(sample_directories)
    print(tree_output)
