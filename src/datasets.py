"""Carga de datasets y mapeo de sus etiquetas a las 7 clases comunes.

Cada loader devuelve un DataFrame con columnas:
    path      ruta a la imagen (recortada en data/processed)
    label     índice en CLASSES
    subject   identificador de persona (None si el dataset no lo tiene)
    split     train | val | test
    + metadatos opcionales (edad, género, pose...) para el análisis por grupos
"""
from pathlib import Path

import pandas as pd

CLASSES = ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]

# Etiquetas originales de RAF-DB (1..7) -> nombre de clase común
RAFDB_LABELS = {1: "surprise", 2: "fear", 3: "disgust", 4: "happy", 5: "sad", 6: "angry", 7: "neutral"}

# Códigos de expresión en los nombres de fichero de KDEF
KDEF_LABELS = {"AF": "fear", "AN": "angry", "DI": "disgust", "HA": "happy", "NE": "neutral", "SA": "sad", "SU": "surprise"}


def load_rafdb(raw_dir: str) -> pd.DataFrame:
    # TODO: leer list_patition_label.txt y, si se usa, las anotaciones demográficas
    raise NotImplementedError


def load_fer2013(raw_dir: str, val_fraction: float = 0.1, seed: int = 42) -> pd.DataFrame:
    """Versión de Kaggle (msambare/fer2013): fer2013/{train,test}/<clase>/*.jpg.

    Las imágenes ya son caras recortadas de 48x48 en gris. No hay ID de persona, así que
    el análisis entre personas se hace con KDEF. La validación se separa de train de forma
    estratificada.
    """
    from sklearn.model_selection import train_test_split

    root = Path(raw_dir) / "fer2013"
    rows = []
    for split in ("train", "test"):
        for label, name in enumerate(CLASSES):
            for path in sorted((root / split / name).glob("*.jpg")):
                rows.append({"path": str(path), "label": label, "subject": None, "split": split})
    df = pd.DataFrame(rows)
    if df.empty:
        raise FileNotFoundError(f"No se encontraron imágenes en {root}; ver data/README.md")

    train_idx = df.index[df["split"] == "train"]
    _, val_idx = train_test_split(
        train_idx, test_size=val_fraction, stratify=df.loc[train_idx, "label"], random_state=seed
    )
    df.loc[val_idx, "split"] = "val"
    return df


def load_kdef(raw_dir: str) -> pd.DataFrame:
    # TODO: parsear nombres tipo AF01ANS.JPG -> sesión, sexo, sujeto, expresión, ángulo
    raise NotImplementedError


LOADERS = {"rafdb": load_rafdb, "fer2013": load_fer2013, "kdef": load_kdef}


def load_dataset(name: str, raw_dir: str, **kwargs) -> pd.DataFrame:
    return LOADERS[name](raw_dir, **kwargs)
