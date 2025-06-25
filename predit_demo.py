import pandas as pd
import joblib
from data_fetch import load_nsl_kdd_test

# 1. Charger le modèle entraîné
clf = joblib.load("rf_model.joblib")

# 2. Charger les données de test (depuis GitHub)
df_test = load_nsl_kdd_test()

# 3. Prétraitement
df_test["label"] = df_test["label"].apply(lambda x: 0 if x == "normal" else 1)
df_test = pd.get_dummies(df_test, columns=["protocol_type", "service", "flag"])

# 4. Aligner les colonnes avec celles attendues par le modèle
X_all = df_test.drop(columns=["label", "difficulty"])
X_model = pd.DataFrame(columns=clf.feature_names_in_)
X_model = pd.concat([X_model, X_all], ignore_index=True).fillna(0)

# 5. Prédiction sur une ligne de test
sample = X_model.iloc[0:1]
prediction = clf.predict(sample)[0]

print("🔍 Prédiction sur une vraie connexion :", "✅ Normal" if prediction == 0 else "🚨 Attaque")
