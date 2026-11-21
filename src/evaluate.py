"""Evaluación: métricas globales, por sujeto/grupo, entre datasets y robustez."""
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix, f1_score

from src.datasets import CLASSES
from src.utils import load_config, parse_args


def global_metrics(labels: np.ndarray, preds: np.ndarray) -> dict:
    return {
        "accuracy": float((labels == preds).mean()),
        "macro_f1": float(f1_score(labels, preds, average="macro")),
        "confusion_matrix": confusion_matrix(labels, preds, labels=range(len(CLASSES))).tolist(),
        "report": classification_report(labels, preds, target_names=CLASSES, output_dict=True, zero_division=0),
    }


def metrics_by_group(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """Macro-F1 por persona o por grupo demográfico. df necesita columnas label, pred y group_col."""
    return (
        df.groupby(group_col)
        .apply(lambda g: pd.Series({"n": len(g), "macro_f1": f1_score(g["label"], g["pred"], average="macro")}))
        .reset_index()
    )


# Perturbaciones para estudiar situaciones de confusión
PERTURBATIONS = ["occlusion_eyes", "occlusion_mouth", "low_light", "blur", "low_resolution"]


def perturb(image, kind: str):
    # TODO: implementar cada perturbación de PERTURBATIONS
    raise NotImplementedError


def main():
    args = parse_args("Evaluación")
    cfg = load_config(args.config)
    # TODO: evaluar baseline y modelo principal sobre cada test_dataset,
    # por sujeto (KDEF), por grupo (RAF-DB), con perturbaciones y por ángulo de cabeza;
    # guardar tablas y figuras en results/
    raise NotImplementedError


if __name__ == "__main__":
    main()
