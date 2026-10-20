# Evidencias — Proyecto A1 Misión 2

**Repositorio:** https://github.com/Boondock19/proyecto-a1-mision-2

## 1. Integrantes y aportaciones

| Integrante | Usuario | Aportaciones |
|---|---|---|
| José Matías González Valarezo | `Boondock19` | Commit inicial del repositorio; funciones de métricas en `src/metricas.py` (`contar_aciertos`, `precision`); tests de `precision` y `contar_aciertos` en `tests/test_metricas.py` (rama `feature/tests`); rama `feature/conflicto-1` para el reto de conflicto; resolución del conflicto en `README.md` y merge final a `main`; revisión y merge de los PR #3 y #4. |
| Sarah Benedi Adams | `sbenedi` | Documentación del proyecto en `README.md` (estructura del repositorio, archivos principales, comandos de ejecución y pruebas, pautas de colaboración con ramas y PR) en la rama `feature/documentacion`; rama `feature/conflicto-sarah` para el reto de conflicto; revisión de los PR #1 y #2. |

## 2. Pull Requests revisados

| PR | Rama | Autor | Revisor | Estado |
|---|---|---|---|---|
| [#1 — Nueva función de precisión](https://github.com/Boondock19/proyecto-a1-mision-2/pull/1) | `feature/metricas` | José Matías González | Sarah Benedi | Merged |
| [#2 — Incremento de Tests](https://github.com/Boondock19/proyecto-a1-mision-2/pull/2) | `feature/tests` | José Matías González | Sarah Benedi | Merged |
| [#3 — Feature/documentacion](https://github.com/Boondock19/proyecto-a1-mision-2/pull/3) | `feature/documentacion` | Sarah Benedi | José Matías González | Merged |
| [#4 — Conflicto controlado - rama Sarah](https://github.com/Boondock19/proyecto-a1-mision-2/pull/4) | `feature/conflicto-sarah` | Sarah Benedi | José Matías González | Merged |

En cada PR la otra persona del equipo revisó los cambios y dejó un comentario antes de hacer el merge a `main`. Por ejemplo, en el PR #3 se valoró positivamente la ampliación de la documentación, y en el PR #4 se aprobó el merge sabiendo que provocaría el conflicto controlado del reto.

## 3. Grafo de ramas

Salida de `git log --oneline --graph --all` tras resolver el conflicto y hacer `push`:

```text
*   265e7b2 (HEAD -> main, origin/main, origin/HEAD) solucionados conflictos
|\
| * c8a56f1 (origin/feature/conflicto-1, feature/conflicto-1) correccion de typo
| * 9ef08f0 cambio para generar conflicto
* |   2087668 Merge pull request #4 from Boondock19/feature/conflicto-sarah
|\ \
| |/
|/|
| * b096c11 (origin/feature/conflicto-sarah) Modifica README para reto de conflicto
|/
*   f544524 Merge pull request #3 from Boondock19/feature/documentacion
|\
| *   2885ca8 (origin/feature/documentacion) Merge branch 'main' into feature/documentacion
| |\
| |/
|/|
* |   f353f0b Merge pull request #2 from Boondock19/feature/tests
|\ \
| * | 49ffdf7 (origin/feature/tests) Añade prueba de aciertos no iguales
| * | 30d859e (feature/tests) Agregar esqueleto de evidencias.md
| * | c9a97f6 add a test case for presicion function
| * | 9dd11b0 (origin/feature/metricas) Añade métricas
|/ /
| * 51671cd Explicacion de Estructura y Comandos
|/
* ebddc37 primer commmit del repo
```

**Lectura del grafo:**

- Todo parte del commit inicial `ebddc37`.
- Las ramas `feature/metricas` y `feature/tests` se integraron en `main` mediante el PR #2 (`f353f0b`).
- La rama `feature/documentacion` se sincronizó con `main` (`2885ca8`) y se integró mediante el PR #3 (`f544524`).
- La rama `feature/conflicto-sarah` se integró con el PR #4 (`2087668`), modificando el encabezado del `README.md`.
- En paralelo, la rama `feature/conflicto-1` modificó la misma línea; su merge a `main` generó el conflicto que se resolvió en `265e7b2`.

## 4. Conflicto y resolución

**Causa.** El conflicto se produjo porque dos ramas, `feature/conflicto-sarah` y `feature/conflicto-1`, modificaron la **misma línea** del archivo `README.md` (el encabezado). Primero se integró `feature/conflicto-sarah` en `main` mediante el PR #4. Después, al ejecutar en local:

```bash
git fetch
git pull
git merge feature/conflicto-1
```

Git no pudo combinar automáticamente los cambios y mostró:

```text
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

**Resolución.** Abrimos `README.md`, revisamos las dos versiones marcadas por Git (`<<<<<<<`, `=======`, `>>>>>>>`) y decidimos conservar el encabezado original, que era común a ambas ramas, añadiendo al final del encabezado los nombres de ambas ramas. Así no se perdía el cambio de ninguna de las dos. Después eliminamos los marcadores de conflicto y registramos la resolución en `main`:

```bash
git add .
git commit -m "solucionados conflictos"
git push
```

El resultado es el commit de merge `265e7b2`, que ya está publicado en `origin/main`.

## 5. Resultado de ejecución del proyecto y los tests

**Preparación del entorno** (entorno virtual e instalación de dependencias):

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

Se instalaron correctamente `scikit-learn 1.9.1`, `numpy 2.5.4`, `scipy 1.18.1`, `joblib 1.6.0`, `narwhals 2.27.1`, `cloudpickle 3.1.2` y `threadpoolctl 3.7.0`.

**Ejecución del proyecto:**

```bash
python3 -m src.predictor
```

```text
Predicción: 0 | Clase real: 0
```

El modelo predice correctamente la clase de la muestra evaluada.

**Ejecución de los tests:**

```bash
python3 -m unittest discover -s tests
```

```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

Los 4 tests de `tests/test_metricas.py` pasan correctamente.

## 6. Mejora propuesta para el flujo de trabajo

El ejercicio nos parece muy adecuado para presentar el uso de Git y GitHub a personas que no tienen conocimientos previos sobre estas herramientas, ya que recorre de forma práctica ramas, Pull Requests, revisiones y resolución de conflictos.

Como mejora, en un equipo de más de dos personas añadiríamos una **regla de protección sobre la rama `main`** (*branch protection rule*) que exija la **aprobación de al menos un revisor** en cada Pull Request antes de poder hacer merge. De esta forma ningún cambio llega a la rama principal sin que otra persona lo haya revisado formalmente, y la revisión queda registrada en GitHub como aprobación y no solo como comentario.