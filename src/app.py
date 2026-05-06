"""Simple sample application for the workshop."""


def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    if not name:
        raise ValueError("Name must not be empty")
    return f"Hello, {name}! Welcome to the AIDLC Workflows Workshop."


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


if __name__ == "__main__":
    print(greet("Nexon"))
    print(f"1 + 2 = {add(1, 2)}")
