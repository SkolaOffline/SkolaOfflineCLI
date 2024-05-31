def print_modules(modules):
    for x, module in enumerate(modules):
        module = module['module']
        print(f"{x}: {module['moduleId']:<10}")
        # print(f"{x}: {module['moduleName']:<50} {module['moduleId']:<10}")

    print()
    