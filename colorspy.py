for i in range(256):
    print(f"\033[38;5;{i}m{i}. Couleur \033[0m", end=" ")
    print(f"Code ANSI : {i}")
    if i % 16 == 15:
        print()  # Nouvelle ligne chaque 16 couleurs
