# ue19-1ab-05 : Application Python "Blague du jour"

## 📝 Description du projet

Ce dépôt contient une application Python simple qui interroge l'API publique **[JokeAPI](https://jokeapi.dev/)** pour récupérer et afficher une blague aléatoire (de type *Single*) directement dans la console.

Le projet est structuré pour être facilement **déployable et exécutable via Docker**, conformément aux pratiques modernes de conteneurisation.

## 🚀 Fonctionnalités

* **Interrogation d'API :** Utilisation de la librairie `requests` pour effectuer des requêtes HTTP GET.
* **Affichage :** Affiche une blague aléatoire de type `Any` / `single` (une seule ligne).
* **Conteneurisation :** Fournit un `Dockerfile` pour créer une image Docker légère du programme.

## 🛠️ Fichiers du dépôt

| Fichier | Description |
| :--- | :--- |
| `README.md` | Le présent fichier : description du projet, fonctionnalités, et instructions d'installation/lancement. |
| `app.py` | Le code source Python qui interroge l'API JokeAPI. |
| `requirements.txt` | Liste des dépendances Python requises (`requests`). |
| `Dockerfile` | Le script pour construire l'image Docker du conteneur. |

## 📦 Howto : Installation et Lancement

Le moyen privilégié pour lancer cette application est via Docker. Les instructions pour une exécution locale sont également fournies.

### 🐳 1. Exécution via Docker (Recommandée)

Cette méthode nécessite que **Docker** soit installé sur votre système.

1.  **Cloner le dépôt :**
    ```bash
    git clone [VOTRE LIEN GITHUB]
    cd ue19-1ab-05
    ```

2.  **Construire l'image Docker :**
    Utilisez le `Dockerfile` pour construire l'image. Nous lui donnons le tag `blague-app`.
    ```bash
    docker build -t blague-app .
    ```

3.  **Lancer le conteneur :**
    Exécutez le conteneur. Le flag `--rm` supprime le conteneur une fois l'exécution terminée.
    ```bash
    docker run --rm blague-app
    ```

### 🐍 2. Exécution Locale (Sans Docker)

Cette méthode nécessite **Python 3** et **pip** installés sur votre système.

1.  **Créer et activer un environnement virtuel (Optionnel, mais recommandé) :**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Ou .\venv\Scripts\activate pour Windows
    ```

2.  **Installer les dépendances :**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Lancer le programme :**
    ```bash
    python app.py
    ```

## 🔗 Dépendances

Les dépendances sont listées dans le fichier `requirements.txt` :

* `requests` : Utilisé pour effectuer des requêtes HTTP et interroger l'API.

## 📞 Contact

Si vous avez des questions ou rencontrez des problèmes, veuillez ouvrir une issue sur ce dépôt.


