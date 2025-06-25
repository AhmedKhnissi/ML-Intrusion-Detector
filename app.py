# app.py

from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)
clf = joblib.load("rf_model.joblib")

# Charger les colonnes que le modèle attend
feature_columns = clf.feature_names_in_

# ✅ Valeurs par défaut réalistes d'une connexion (potentiellement malveillante)
default_values = {
    'duration': 5,                  # Durée de la connexion en secondes
    'src_bytes': 232,              # Octets envoyés par la source
    'dst_bytes': 815,              # Octets reçus par la source
    'count': 10,                   # Nombre de connexions vers le même hôte
    'srv_count': 5,                # Nombre de connexions vers le même service
    'serror_rate': 0.0,            # Pas d'erreurs SYN
    'same_srv_rate': 1.0,          # Toutes les connexions ont le même service
    'diff_srv_rate': 0.0,          # Aucune connexion vers un service différent
    'protocol_type_tcp': 1,        # TCP
    'flag_SF': 1                   # Flag TCP normal : SYN suivi de FIN
}


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    input_data = default_values.copy()  # valeurs par défaut affichées au premier affichage

    if request.method == "POST":
        try:
            # Récupérer les champs du formulaire
            input_data = {col: float(request.form.get(col, 0)) for col in feature_columns}
            sample = pd.DataFrame([input_data])

            # Prédiction
            prediction = clf.predict(sample)[0]
            result = "🚨 Attaque détectée" if prediction == 1 else "✅ Connexion normale"
        except Exception as e:
            result = f"Erreur : {e}"

    return render_template("index.html", columns=feature_columns, values=input_data, result=result)

if __name__ == "__main__":
    app.run(debug=True)
