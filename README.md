# Proyecto IA — Clasificador de flores cambias de matiasss
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


## Estructura 
- `src/predictor.py`: entrenamiento mínimo y predicción. Carga los datos Iris, los divide en entrenamiento y prueba, entrena el modelo y realiza prediccion
- `src/metricas.py`: funciones auxiliares para ampliar. Contiene las funciones para evaluar el modelo, como contar los aciertos entre las predicciones y los valores reales
- `tests/`: pruebas de partida. Contiene las pruebas automaticas para comprobar que las funciones de metricas funcionan bien
- `__init__.py/`: indica que src puede utilizarse como paquete de Python
- .gitignore: evita que Git incluya archivos innecesarios
- README.md: explica el proyecto, estructura y como utilizarlo
- requirements.txt: lista las dependencias necesarias para ejecutar el proyecto


## Comandos
- pip install -r requirements.txt Instala las dependencias
- Python -m src.predictor Ejecuta el modelo y muestra una predicción
- pytest Ejecuta las pruebas automáticas
- git status Muestra los cambios realizados
- git add . Prepara los archivos para guardarlos en Git
- git commit -m "Añade modelo y métricas" Guarda los cambios en un commit
- git branch Muestra las ramas existentes
- git switch -c feature/documentacion Crea una rama nueva y cambia a ella
- git push -u origin feature/documentacion Sube la rama al repositorio remoto