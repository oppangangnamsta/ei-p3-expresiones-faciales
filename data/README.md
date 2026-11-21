# Datos

Esta carpeta no se sube al repositorio (ver `.gitignore`). Cada integrante descarga los datasets
por su cuenta, respetando su licencia, y los coloca con esta estructura:

```
data/
  raw/
    rafdb/      # RAF-DB (acceso bajo acuerdo académico)
    fer2013/    # FER2013 (Kaggle) — alternativa si RAF-DB no llega a tiempo
    kdef/       # KDEF (registro, uso no comercial) — evaluación entre datasets / por sujeto
    ckplus/     # CK+ (solicitud) — opcional
  processed/    # caras recortadas y alineadas (generado por src/preprocess.py)
```

## Origen y licencias

| Dataset | Dónde obtenerlo | Licencia / permisos | Estado |
|---|---|---|---|
| RAF-DB | http://www.whdeng.cn/RAF/model1.html | Solo investigación; requiere firmar acuerdo | _pendiente_ |
| FER2013 | https://www.kaggle.com/datasets/msambare/fer2013 | Uso de investigación | _pendiente_ |
| KDEF | https://kdef.se/ | Uso no comercial; registro | _pendiente_ |
| CK+ | https://www.jeffcohn.net/resources/ | Uso no comercial; solicitud | _opcional_ |

Comprobad los enlaces y las condiciones al solicitar el acceso y anotad aquí la fecha de descarga
y la versión usada.

## Clases

Se usan las 7 expresiones básicas comunes a los datasets: `angry`, `disgust`, `fear`, `happy`,
`neutral`, `sad`, `surprise`. Cada dataset se mapea a esta lista en `src/datasets.py`.
