# Notas Técnicas del Proyecto

## Revisión QA - Luis (P3)

### Verificaciones realizadas
- Ausencia de tokens o credenciales en el repositorio
- Rutas relativas en el script para garantizar reproducibilidad
- Comentarios técnicos explicando el por qué de cada decisión
- Dataset de acceso público correctamente citado
- Archivo .gitignore configurado correctamente

### Observaciones del Peer Review
- Se recomienda usar fillna() con interpolación en versiones futuras
- Agregar gráfico comparativo por décadas en próximas iteraciones

### Dataset utilizado
- Fuente: datahub.io/core/global-temp
- Origen: GISTEMP (NASA) y GCAG
- Licencia: Dominio público
- Formato: CSV
