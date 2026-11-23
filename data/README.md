# Datos

Esta carpeta no se sube al repositorio (ver `.gitignore`). Cada integrante descarga los datasets
por su cuenta, respetando su licencia, y los coloca con esta estructura:

```
data/
  raw/
    fer2013/    # dataset principal (Kaggle)
      train/<clase>/*.jpg
      test/<clase>/*.jpg
    kdef/       # KDEF (registro, uso no comercial): evaluación entre datasets y por persona
    rafdb/      # RAF-DB (opcional, acuerdo académico)
  processed/    # generado por src/preprocess.py
```

## FER2013 (dataset principal)

Kaggle: https://www.kaggle.com/datasets/msambare/fer2013

Descarga manual: botón *Download* en Kaggle, y descomprimir el zip en `data/raw/fer2013/` de forma
que queden las carpetas `train/` y `test/`.

Con la CLI de Kaggle (necesita tu token en `~/.kaggle/kaggle.json`, ver https://www.kaggle.com/docs/api):

```bash
kaggle datasets download -d msambare/fer2013 -p data/raw/fer2013 --unzip
```

Características a tener en cuenta (van al póster, apartado *limitaciones*):
- ~28.7k imágenes de train y ~7.2k de test, 48×48 en escala de grises, caras ya recortadas.
- 7 clases muy desbalanceadas (`disgust` tiene ~4 veces menos ejemplos que la siguiente).
- Etiquetas con ruido (recogidas de búsquedas web): el techo de accuracy humana ronda el 65 %.
- **Sin identificador de persona**: no permite evaluación independiente de sujeto. Para eso se usa KDEF.
- Sin partición de validación: `src/datasets.py` separa un 10 % estratificado de train.

## Otros datasets

| Dataset | Dónde obtenerlo | Licencia / permisos | Uso | Estado |
|---|---|---|---|---|
| FER2013 | https://www.kaggle.com/datasets/msambare/fer2013 | Investigación | Entrenamiento y test | _pendiente_ |
| KDEF | https://kdef.se/ | No comercial; registro | Test entre datasets y por persona | _pendiente_ |
| RAF-DB | http://www.whdeng.cn/RAF/model1.html | Investigación; acuerdo | Opcional (análisis por grupos) | _opcional_ |

Anotad aquí la fecha de descarga y la versión usada de cada uno.

## Clases

Se usan las 7 expresiones básicas: `angry`, `disgust`, `fear`, `happy`, `neutral`, `sad`,
`surprise`. Coinciden con los nombres de carpeta de FER2013; el resto de datasets se mapea a esta
lista en `src/datasets.py`.
