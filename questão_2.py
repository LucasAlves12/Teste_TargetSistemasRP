"""2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
"""

def main():
    while True:
        try:
            string = input("Informe uma string: ")
            count = string.lower().count("a")
            print(f"A letra 'a' aparece {count} vezes na string informada.\n")
        except ValueError:
            print("Por favor, informe uma string válida.")    
        
        continuar = input("Deseja continuar? (S/N): ")
        if continuar.upper() != "S":
            break

if __name__ == "__main__": 
    main()