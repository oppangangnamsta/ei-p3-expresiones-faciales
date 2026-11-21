"""Lógica de adaptación prudente del espejo.

Solo se sugiere algo si la expresión se mantiene con confianza calibrada alta durante
una ventana de tiempo. Las sugerencias describen la expresión observada, no una emoción,
y siempre se pueden ignorar o desactivar.
"""
from collections import deque
from dataclasses import dataclass

import numpy as np

# Sugerencias opcionales: se ofrecen, nunca se aplican solas
SUGGESTIONS = {
    "sad": "Se observa una expresión seria desde hace un rato. ¿Quieres poner algo de música?",
    "angry": "Se observa el ceño fruncido. ¿Prefieres una interfaz más sencilla por ahora?",
    "happy": None,
    "neutral": None,
    "surprise": None,
    "fear": None,
    "disgust": None,
}


@dataclass
class AdaptationPolicy:
    classes: list
    threshold: float = 0.7      # confianza calibrada mínima
    window: int = 30            # nº de frames a promediar (~1-2 s según FPS)
    min_agreement: float = 0.8  # fracción de frames que deben coincidir
    enabled: bool = False       # opt-in: desactivado por defecto

    def __post_init__(self):
        self.history = deque(maxlen=self.window)

    def update(self, probs: np.ndarray | None):
        """Añade las probabilidades de un frame (None si no hay cara) y devuelve una sugerencia o None."""
        if not self.enabled:
            return None
        self.history.append(probs)
        frames = [p for p in self.history if p is not None]
        if len(self.history) < self.window or len(frames) < self.min_agreement * self.window:
            return None  # poca información: abstenerse

        mean = np.mean(frames, axis=0)
        top = int(mean.argmax())
        agreement = np.mean([p.argmax() == top for p in frames])
        if mean[top] < self.threshold or agreement < self.min_agreement:
            return None
        return SUGGESTIONS.get(self.classes[top])
