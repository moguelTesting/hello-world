def greet(name: str = "World") -> str:
    """Simple greeting function."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
    print(greet("Miguel"))
