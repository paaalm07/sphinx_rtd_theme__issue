class DUMMY:
    """Dummy class."""
    def __init__(self):
        pass

    def add(self, a, b):
        """Simple add function."""
        return a + b


if __name__ == "__main__":
    dummy = DUMMY()
    print(dummy.add(5, 3))
