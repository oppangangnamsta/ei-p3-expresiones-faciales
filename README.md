# Reconocimiento de expresiones faciales para una interacción adaptativa

Práctica 3 · Entornos Inteligentes (AAL) · Grupo de prácticas 3 · Trabajo 3

**Integrantes:** JF, Linxi, David

## Problema

Un espejo inteligente puede adaptar de forma prudente y opcional algunos elementos de la
interacción a partir de la expresión facial observable de la persona. El trabajo estudia:

1. **Fiabilidad** de las predicciones (calibración, abstención).
2. **Diferencias entre personas** (evaluación independiente de sujeto, por grupos y entre datasets).
3. **Situaciones de confusión** (oclusiones, iluminación, pose, resolución).

Una expresión facial **no** se interpreta como el estado emocional real de la persona.

## Estructura

```
configs/     configuración de experimentos (YAML)
data/        datasets (NO se versionan; ver data/README.md)
src/         preprocesado, modelos, entrenamiento, evaluación y calibración
notebooks/   análisis exploratorio y figuras del póster
demo/        prototipo del espejo inteligente (webcam)
results/     métricas (JSON/CSV) y figuras generadas
poster/      póster A2 final (PDF)
```

## Instalación

Recomendado Python 3.11 (algunas dependencias, como MediaPipe, pueden no tener soporte para versiones más nuevas).

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/macOS
pip install -r requirements.txt
```

## Datos

Los datasets no se redistribuyen por sus licencias. Consulta [data/README.md](data/README.md) para
saber cómo obtenerlos y dónde colocarlos.

## Reproducción de los experimentos

```bash
# 1. Detección, recorte y alineado de caras
python -m src.preprocess --config configs/default.yaml

# 2. Método base (landmarks/HOG + SVM)
python -m src.baseline --config configs/default.yaml

# 3. Modelo principal (CNN preentrenada + fine-tuning)
python -m src.train --config configs/default.yaml

# 4. Calibración (temperature scaling) y evaluación
python -m src.calibrate --config configs/default.yaml
python -m src.evaluate --config configs/default.yaml

# 5. Demo del espejo
streamlit run demo/app.py
```

Los resultados se guardan en `results/`.

## Referencias

_(completar: artículos principales y fuentes de los datos)_
