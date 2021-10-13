root = "src"
directories = ["components", "api", "views"]

output = f"{root}/\n"
directory = directories.pop(0)
while directories:
    output += f"│\n├── {directory}/\n"
    directory = directories.pop(0)
output += f"│\n└── {directory}/\n"

print(output)
