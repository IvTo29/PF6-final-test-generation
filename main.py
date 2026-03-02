import json
import requests


def dish_fetch(num):
    response = requests.get(f"https://api-colombia.com/api/v1/TypicalDish/{num}")
    informacion = response.json()

    plato = {
        "id": num,
        "name": informacion["name"],
        "description": informacion["description"]
    }

    return plato


def main():
    print("Hello learners!")
    num = int(input("Ingrese el numero del plato: "))
    resultado = dish_fetch(num)

    print("Numero:", resultado["id"])
    print("Nombre:", resultado["name"])
    print("Descripcion:", resultado["description"])


if __name__=="__main__":
    main()