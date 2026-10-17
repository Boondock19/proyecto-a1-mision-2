"""Modelo didáctico para practicar un flujo de desarrollo versionado."""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def entrenar_modelo():
    datos = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(
        datos.data, datos.target, test_size=0.25, random_state=42, stratify=datos.target
    )
    modelo = DecisionTreeClassifier(max_depth=3, random_state=42)
    modelo.fit(x_train, y_train)
    return modelo, x_test, y_test


def predecir_ejemplo():
    modelo, x_test, y_test = entrenar_modelo()
    predicciones = modelo.predict(x_test)
    return int(predicciones[0]), int(y_test[0])


if __name__ == "__main__":
    predicho, real = predecir_ejemplo()
    print(f"Predicción: {predicho} | Clase real: {real}")
