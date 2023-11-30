#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lib = dir(hidden_4)

    for name in sorted(lib):
        if not name.startswith("__"):
            print(name)
