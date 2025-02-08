def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    result = []
    for i in range(repetitions):
        result.append(text[i-repetitions:])
    return '\n'.join(result) + '\n.'

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
