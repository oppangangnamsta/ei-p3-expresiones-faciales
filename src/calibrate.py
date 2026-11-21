"""Calibración por temperature scaling y medidas de fiabilidad."""
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.special import log_softmax, softmax

from src.utils import load_config, parse_args


def fit_temperature(val_logits: np.ndarray, val_labels: np.ndarray) -> float:
    """Temperatura que minimiza la NLL en validación (Guo et al., 2017)."""

    def nll(t):
        return -log_softmax(val_logits / t, axis=1)[np.arange(len(val_labels)), val_labels].mean()

    return minimize_scalar(nll, bounds=(0.05, 10.0), method="bounded").x


def expected_calibration_error(probs: np.ndarray, labels: np.ndarray, n_bins: int = 15) -> float:
    conf = probs.max(axis=1)
    correct = probs.argmax(axis=1) == labels
    bins = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    for lo, hi in zip(bins[:-1], bins[1:]):
        mask = (conf > lo) & (conf <= hi)
        if mask.any():
            ece += mask.mean() * abs(correct[mask].mean() - conf[mask].mean())
    return ece


def risk_coverage(probs: np.ndarray, labels: np.ndarray):
    """Error frente a cobertura al abstenerse en las predicciones menos seguras."""
    order = np.argsort(-probs.max(axis=1))
    errors = (probs.argmax(axis=1) != labels)[order]
    coverage = np.arange(1, len(labels) + 1) / len(labels)
    risk = np.cumsum(errors) / np.arange(1, len(labels) + 1)
    return coverage, risk


def apply_temperature(logits: np.ndarray, t: float) -> np.ndarray:
    return softmax(logits / t, axis=1)


def main():
    args = parse_args("Calibración")
    cfg = load_config(args.config)
    # TODO: cargar logits de val/test guardados por train.py, ajustar T en val,
    # guardar T y ECE antes/después en results/, dibujar diagrama de fiabilidad
    raise NotImplementedError


if __name__ == "__main__":
    main()
