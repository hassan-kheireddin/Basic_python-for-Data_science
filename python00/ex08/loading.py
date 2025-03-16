def ft_tqdm(listeRange: range) -> None:
    """Custom progress bar generator similar to tqdm."""
    length = len(listeRange)
    if length == 0:
        return
    i = length - 1

    for value in listeRange:
        percent = int((value / i) * 100) if i > 0 else 100
        bar = '█' * (percent // 2)
        bar += ' ' * ((100 // 2) - len(bar))
        str_value = f"{value+1}/{length}"
        print(f"\r{percent:>3}% |{bar}| {str_value}", end="", flush=True)
        yield
        print("\n")
