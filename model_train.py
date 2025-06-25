# model_train.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

from data_fetch import load_nsl_kdd

# 1. Chargement
df = load_nsl_kdd()

# 2. Simplification : 0 = normal, 1 = attaque
df["label"] = df["label"].apply(lambda x: 0 if x == "normal" else 1)

# 3. Encodage des colonnes catégorielles
df = pd.get_dummies(df, columns=["protocol_type", "service", "flag"])

# 4. Séparation X / y
X = df.drop(columns=["label", "difficulty"])
y = df["label"]

# ✅ 5. Split en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Modèle
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# 7. Évaluation
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# 8. Sauvegarde
joblib.dump(clf, "rf_model.joblib")
print("✅ Modèle sauvegardé sous 'rf_model.joblib'")
