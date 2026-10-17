# Proyecto IA — Clasificador de flores
Prototipo de clasificación con el dataset Iris integrado en scikit-learn. Se utiliza para practicar Git/GitHub, no para evaluar calidad predictiva.

## Instalación
```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Ejecución
```bash
python -m src.predictor
python -m unittest discover -s tests -v
```

## Estructura
- `src/predictor.py`: entrenamiento mínimo y predicción.
- `src/metricas.py`: funciones auxiliares para ampliar.
- `tests/`: pruebas de partida.

## Colaboración
Usad ramas `feature/*`, Pull Requests y revisiones de compañeros.
