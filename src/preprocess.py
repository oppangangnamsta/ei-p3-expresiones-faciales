"""Detección de cara, recorte y alineado con MediaPipe.

Guarda las caras procesadas en data/processed/<dataset>/ y un CSV con las imágenes
en las que no se detectó cara (también es un resultado: fallos del detector).
"""
from src.utils import load_config, parse_args, set_seed


def detect_and_align(image):
    """Devuelve la cara recortada y alineada por los ojos, o None si no hay cara."""
    # TODO: mediapipe FaceMesh/FaceDetection -> rotar según los ojos -> recortar con margen
    raise NotImplementedError


def main():
    args = parse_args("Preprocesado de caras")
    cfg = load_config(args.config)
    set_seed(cfg["seed"])
    # TODO: recorrer cada dataset de cfg["data"], aplicar detect_and_align y guardar
    raise NotImplementedError


if __name__ == "__main__":
    main()
