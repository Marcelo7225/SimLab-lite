# Workflow End-to-End

## Intake

Capturar o inferir:

- Marca/producto/oferta.
- Decision a informar.
- Audiencia inicial.
- Estimulo a probar.
- Canales.
- Objeciones.
- Competidores/sustitutos.
- Restricciones.
- Evidencia disponible.

Si hay ambiguedad, hacer maximo 5 preguntas. Si el usuario pide avanzar, declarar supuestos.

## Archivos De Caso

Usar `scripts/create_case.py <case-slug> --root <path>` para crear estructura.

Mantener `CASE_INDEX.md` actualizado con etapa actual, supuestos activos y proxima accion.

El caso tambien puede incluir:

```text
session.json
memory/facts.json
memory/assumptions.json
memory/decisions.jsonl
memory/checkpoints.jsonl
memory/unresolved_questions.json
```

Estos archivos son memoria local de sesion. Si no existen, crearlos al iniciar un caso completo.

## Etapas

### 1. Brief

Escribir `00_brief.md` con:

- Decision.
- Estimulo.
- Audiencia.
- Mercado.
- Restricciones.
- Evidencia.
- Objeciones.
- Supuestos.

### 2. Mapa Social

Escribir `01_social_map.md` con:

- Actores.
- Segmentos.
- Relaciones de influencia.
- Narrativas.
- Tensiones.
- Puntos de contagio/friccion.

### 3. Agentes

Escribir `02_agents.json`.

Requisitos:

- `agent_count` entre 15 y 30.
- Cada agente incluye motivaciones, objeciones, influencia, riesgo, precio, canales, creencia base y gatillo.
- Distribucion minima: promotores, pragmaticos, neutrales, escepticos, bloqueadores, influenciadores.

### 4. Rondas

Escribir una linea JSON por ronda en `03_rounds.jsonl`.

Rondas sugeridas:

1. Exposicion inicial.
2. Conversacion social y comparacion.
3. Objeciones y fricciones.
4. Ajuste de mensaje/oferta.
5. Resultado simulado.

Cada ronda debe incluir patrones emergentes y desplazamiento narrativo.

### 5. Entrevistas

Escribir `04_interviews.md`.

Entrevistar:

- 2 promotores.
- 2 escepticos.
- 1 bloqueador.
- 1 influenciador.
- 1 ambiguo.

### 6. Causal

Escribir `05_causal_map.md`.

Cada hipotesis:

- Si X, podria mover Y porque Z.
- Evidencia simulada.
- Segmentos afectados.
- Confusores.
- Senales reales para validar.
- Confianza.

### 7. Prescripcion

Escribir `06_prescriptions.md`.

Cada decision:

- Que hacer.
- Razon social.
- Razon causal.
- Segmento/canal.
- Riesgo.
- Experimento.

### 8. Experimentos

Escribir `07_experiments.md`.

Cada experimento:

- Hipotesis.
- Segmento.
- Variante A/B.
- Canal.
- Metrica primaria/secundaria.
- Criterio de decision.
- Riesgo de interpretacion.

### 9. War Room Final

Escribir `08_war_room_final.md` con:

1. Lectura social.
2. Narrativas emergentes.
3. Hipotesis causales.
4. Segmentos prioritarios.
5. Decisiones recomendadas.
6. Experimentos.
7. Riesgos.
8. Senales de monitoreo.
9. Proxima ronda.

## Checkpoints No Bloqueantes

Usar checkpoints como decisiones registradas, no como frenos:

| Checkpoint | Momento | Default |
|---|---|---|
| CP-00 | inicio | crear nueva sesion |
| CP-01 | brief normalizado | continuar con supuestos |
| CP-02 | poblacion | continuar con agentes v1 |
| CP-03 | antes de rondas | usar estimulo inferido |
| CP-04 | despues de ronda 3 | continuar |
| CP-05 | antes de entrevistas | entrevistar extremos |
| CP-06 | antes de prescripcion | riesgo medio |
| CP-07 | cierre | cerrar si cumple criterios |

Formato:

```json
{"checkpoint_id":"CP-04","stage":"round_simulation","blocking":false,"default_action":"continue","decision_taken":"default","timestamp":""}
```

## Definicion De Completo

Una simulacion esta completa solo si existe una cadena:

```text
brief -> supuestos -> mapa social -> agentes -> rondas -> entrevistas -> causalidad -> prescripciones -> experimentos -> war room
```

Minimos:

- 15 agentes.
- 3 rondas, ideal 5.
- 7 entrevistas.
- 3 hipotesis causales.
- 5 prescripciones o decisiones.
- 5 experimentos.
- Riesgos y senales de monitoreo.

Cada experimento debe responder:

1. Que hipotesis prueba.
2. Que prescripcion valida o refuta.
3. Que mecanismo causal intenta mover.
4. Que segmento afecta.
5. Que metrica decide.
6. Que accion tomar si gana, falla o queda inconcluso.
