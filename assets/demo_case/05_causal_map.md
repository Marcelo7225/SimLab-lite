# Mapa Causal

## DAG Textual

```text
exposicion_al_mensaje -> claridad_de_habilidad -> confianza -> lead_calificado
prueba_social_local -> reduccion_de_riesgo -> confianza
autoridad_reclutador -> credibilidad -> intencion
promesa_excesiva -> desconfianza -> rechazo_publico
precio -> friccion -> abandono
informacion_sin_presion -> confianza -> lead
```

## Hipotesis Causales

### H1
- Hipotesis: Si el mensaje cambia de certificado a evidencia de habilidad, podria aumentar leads calificados porque reduce la percepcion de diploma decorativo.
- Mecanismo: claridad_de_habilidad -> confianza -> lead.
- Evidencia simulada: R4, INT-03, INT-07.
- Prediccion observable: mayor clic a temario/proyecto y mas conversaciones calificadas.
- Que la falsaria: no mejora conversion frente al mensaje base.
- Segmentos afectados: profesional presionado, esceptico informado, reclutadora.
- Confusores: reputacion previa de marca, precio, reconocimiento.
- Como validar: A/B landing con claim certificado vs proyecto verificable.
- Confianza: media.

### H2
- Hipotesis: Si se incorpora autoridad de reclutador o experto, podria aumentar confianza porque traduce el curso a criterios laborales.
- Mecanismo: autoridad_experta -> credibilidad -> intencion.
- Evidencia simulada: R4, INT-06, INT-07.
- Prediccion observable: mayor engagement en LinkedIn y mejor tasa de lead calificado.
- Que la falsaria: baja diferencia entre piezas con/sin autoridad.
- Segmentos afectados: escepticos, comparadores, profesionales.
- Confusores: autoridad percibida del experto.
- Como validar: pieza LinkedIn con reclutador vs pieza de marca.
- Confianza: media-alta.

### H3
- Hipotesis: Si el flujo exige datos demasiado temprano, podria bajar conversion porque activa defensa comercial en investigadores silenciosos.
- Mecanismo: informacion_sin_presion -> confianza -> lead.
- Evidencia simulada: INT-08, R5.
- Prediccion observable: mas retorno a landing y leads de mayor calidad si hay contenido abierto.
- Que la falsaria: gating temprano convierte igual o mejor.
- Segmentos afectados: investigadores silenciosos, comparadores.
- Confusores: calidad del contenido abierto.
- Como validar: landing abierta vs gated.
- Confianza: media.

### H4
- Hipotesis: Si el mensaje promete empleabilidad de forma absoluta, podria aumentar rechazo publico porque parece manipulador.
- Mecanismo: promesa_excesiva -> desconfianza -> comentario critico.
- Evidencia simulada: R3, INT-03, INT-05.
- Prediccion observable: mayor tasa de comentarios negativos o preguntas defensivas.
- Que la falsaria: no hay deterioro de sentimiento.
- Segmentos afectados: escepticos, detractores, expertos.
- Confusores: redaccion exacta y reputacion.
- Como validar: pretest cualitativo y monitoreo de comentarios.
- Confianza: alta.

## Variables

- Tratamientos: claim, prueba social, autoridad experta, gating, oferta.
- Mediadores: confianza, claridad, riesgo percibido, relevancia laboral.
- Outcomes: lead calificado, clic a temario, consulta WhatsApp, comentario negativo.
- Confusores: precio, marca, categoria, timing laboral.
- Senales proxy: preguntas sobre proyecto, tasa de rebote, sentimiento en comentarios.
