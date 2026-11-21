"""Fine-tuning de una CNN preentrenada (timm) para clasificar expresiones."""
from src.utils import load_config, parse_args, set_seed


def build_model(backbone: str, num_classes: int, pretrained: bool):
    import timm

    return timm.create_model(backbone, pretrained=pretrained, num_classes=num_classes)


def main():
    args = parse_args("Entrenamiento del modelo principal")
    cfg = load_config(args.config)
    set_seed(cfg["seed"])
    # TODO: DataLoaders con aumentos (flip, color jitter, pequeñas rotaciones),
    # pérdida con pesos por clase, early stopping por macro-F1 en validación,
    # guardar el mejor checkpoint y los logits de val/test en results/
    raise NotImplementedError


if __name__ == "__main__":
    main()
