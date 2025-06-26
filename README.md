# 🔐 Network Intrusion Detection System (IDS) with Machine Learning

Ce projet implémente un **système de détection d'intrusion (IDS)** basé sur l'apprentissage automatique, capable d'identifier les connexions réseau malveillantes grâce au jeu de données **NSL-KDD**.

L'application propose :
- Entraînement d’un modèle de classification supervisé (Random Forest),
- Évaluation du modèle,
- Prédiction sur de vraies connexions issues du dataset de test,
- Interface web intuitive avec Flask pour simuler des connexions réseau.

---

## 📁 Structure de base du projet

data_fetch.py # Téléchargement et chargement des datasets NSL-KDD (train & test)
model_train.py # Préparation, entraînement, évaluation et sauvegarde du modèle Random Forest
predict_demo.py # Démonstration de prédiction sur une ligne du dataset de test
app.py # Application Flask pour prédire visuellement une connexion réseau
templates / index.html # Interface HTML Bootstrap pour l'application Flask
rf_model.joblib # Modèle sauvegardé (généré après exécution de model_train.py)

