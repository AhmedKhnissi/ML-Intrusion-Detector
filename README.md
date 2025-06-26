# 🔐 Network Intrusion Detection System (IDS) with Machine Learning

Ce projet implémente un **système de détection d'intrusion (IDS)** basé sur l'apprentissage automatique, capable d'identifier les connexions réseau malveillantes grâce au jeu de données **NSL-KDD**.

L'application propose :
- Entraînement d’un modèle de classification supervisé (Random Forest),
- Évaluation du modèle,
- Prédiction sur de vraies connexions issues du dataset de test,
- Interface web intuitive avec Flask pour simuler des connexions réseau.

---

## 📁 Structure de base du projet
```jsx
data_fetch.py # Téléchargement et chargement des datasets NSL-KDD (train & test)
model_train.py # Préparation, entraînement, évaluation et sauvegarde du modèle Random Forest
predict_demo.py # Démonstration de prédiction sur une ligne du dataset de test
app.py # Application Flask pour prédire visuellement une connexion réseau
templates / index.html # Interface HTML Bootstrap pour l'application Flask
rf_model.joblib # Modèle sauvegardé (généré après exécution de model_train.py)
```


---

## 📦 Jeu de données

Utilisation du jeu de données **NSL-KDD**, disponible sur [GitHub – Jehuty4949](https://github.com/Jehuty4949/NSL_KDD).

- `KDDTrain+.csv` : dataset d’entraînement
- `KDDTest+.csv` : dataset de test

---

## ⚙️ Entraînement du modèle

L’entraînement est réalisé avec un **Random Forest Classifier** après un prétraitement (encodage one-hot, mapping des labels, séparation X/y).

**Exécution :**

```bash
python model_train.py

