"""Método base: características clásicas (landmarks o HOG) + SVM."""
from src.utils import load_config, parse_args, set_seed


def extract_features(images, kind: str):
    # TODO: "landmarks" -> coordenadas normalizadas de MediaPipe; "hog" -> skimage.feature.hog
    raise NotImplementedError


def main():
    args = parse_args("Método base")
    cfg = load_config(args.config)
    set_seed(cfg["seed"])
    # TODO: extraer características, entrenar sklearn SVC(probability=True) con
    # class_weight="balanced", guardar probabilidades de test en results/ para evaluate.py
    raise NotImplementedError


if __name__ == "__main__":
    main()
