"""Carga de datasets y mapeo de sus etiquetas a las 7 clases comunes.

Cada loader devuelve un DataFrame con columnas:
    path      ruta a la imagen (recortada en data/processed)
    label     índice en CLASSES
    subject   identificador de persona (None si el dataset no lo tiene)
    split     train | val | test
    + metadatos opcionales (edad, género, pose...) para el análisis por grupos
"""
import pandas as pd

CLASSES = ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]

# Etiquetas originales de RAF-DB (1..7) -> nombre de clase común
RAFDB_LABELS = {1: "surprise", 2: "fear", 3: "disgust", 4: "happy", 5: "sad", 6: "angry", 7: "neutral"}

# Códigos de expresión en los nombres de fichero de KDEF
KDEF_LABELS = {"AF": "fear", "AN": "angry", "DI": "disgust", "HA": "happy", "NE": "neutral", "SA": "sad", "SU": "surprise"}


def load_rafdb(raw_dir: str) -> pd.DataFrame:
    # TODO: leer list_patition_label.txt y, si se usa, las anotaciones demográficas
    raise NotImplementedError


def load_fer2013(raw_dir: str) -> pd.DataFrame:
    # TODO: leer las carpetas train/test de la versión de Kaggle
    raise NotImplementedError


def load_kdef(raw_dir: str) -> pd.DataFrame:
    # TODO: parsear nombres tipo AF01ANS.JPG -> sesión, sexo, sujeto, expresión, ángulo
    raise NotImplementedError


LOADERS = {"rafdb": load_rafdb, "fer2013": load_fer2013, "kdef": load_kdef}


def load_dataset(name: str, raw_dir: str) -> pd.DataFrame:
    return LOADERS[name](raw_dir)
