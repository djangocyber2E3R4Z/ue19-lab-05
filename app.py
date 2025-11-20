import requests
import sys

JOKE_API_URL = "https://v2.jokeapi.dev/joke/Any?type=single"

def fetch_joke():
    """
    Récupère une blague aléatoire depuis JokeAPI.
    """
    try:
        response = requests.get(JOKE_API_URL, timeout=10)
        response.raise_for_status()  
        data = response.json()

        if data.get("error"):
            print("Erreur lors de la récupération de la blague de l'API.", file=sys.stderr)
            sys.exit(1)

        joke = data.get("joke", "Impossible de trouver la blague.")
        print("Votre blague du jour :")
        print("--------------------------")
        print(joke)
        print("--------------------------")

    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion à l'API : {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    fetch_joke()