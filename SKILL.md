---
name: social-marketing-sim
description: "Use when the user asks Codex to run a conversational social marketing simulation: simular campanas, ofertas, posicionamiento, lanzamientos, pricing, rebranding, crisis, audiencias, buyer personas dinamicas, war rooms de marketing, entrevistas a agentes, hipotesis causales, prescripcion de acciones o experimentos. Creates session-local case files when useful, with 15-30 agents, social rounds, interviews, causal hypotheses and actionable war room output. Do not build an app/backend unless separately requested."
---

# Social Marketing Sim

## Objetivo

Convertir un brief de marketing en un mercado social simulado, pequeno y conversacional. Generar agentes, simular reacciones por rondas, entrevistar actores clave, formular hipotesis causales y cerrar con decisiones/experimentos.

No presentar predicciones como certezas. Separar siempre: observacion simulada, inferencia causal y prescripcion.
Los archivos locales son memoria de sesion, no una app, backend, dashboard o base de datos.

## Flujo Base

1. **Brief**: estructurar decision, oferta, audiencia, estimulo, canales, restricciones y evidencia.
2. **Mapa social**: identificar segmentos, influenciadores, bloqueadores, narrativas, tensiones y canales de opinion.
3. **Agentes**: crear 15-30 agentes plausibles y balanceados.
4. **Simulacion**: correr 3-5 rondas de reaccion social.
5. **Entrevistas**: entrevistar promotores, escepticos, bloqueadores, influenciadores y ambiguos.
6. **Causal**: ordenar patrones como hipotesis de mecanismos causa-efecto.
7. **Prescripcion**: recomendar decisiones con razon social, razon causal, riesgo y experimento.
8. **War room final**: sintetizar lectura social, narrativas, segmentos prioritarios, decisiones, experimentos y senales de monitoreo.

## Memoria Local

Si el caso va a continuar o el usuario pide construir "completo", crear una carpeta de caso con `scripts/create_case.py`. Usar `cases/<case-slug>/` salvo que el usuario indique otra ruta.

Estructura esperada:

```text
00_brief.md
01_social_map.md
02_agents.json
03_rounds.jsonl
04_interviews.md
05_causal_map.md
06_prescriptions.md
07_experiments.md
08_war_room_final.md
CASE_INDEX.md
```

Validar con `scripts/validate_case.py` antes de declarar completo.

## Recursos

- Leer `references/workflow.md` para ejecutar un caso end-to-end.
- Leer `references/agent_bank.md` al crear agentes o balancear arquetipos.
- Leer `references/causal_prescriptive.md` al formular mapa causal, recomendaciones o experimentos.
- Leer `references/operator_playbook.md` cuando el usuario pida construir el simulador completo, continuar una sesion o recalibrar.
- Usar `assets/templates/` como plantillas de archivos de caso.
- Usar `assets/demo_case/` como ejemplo end-to-end validado.
- Usar `scripts/create_case.py` para inicializar casos.
- Usar `scripts/validate_case.py` para verificar completitud estructural.

## Reglas Operativas

- Hacer maximo 5 preguntas antes de avanzar; si falta informacion, marcar supuestos.
- Separar hechos del usuario, supuestos, inferencias y desconocidos.
- Usar 15-30 agentes por defecto; si el usuario no define cantidad, usar 18.
- Incluir promotores, pragmaticos, neutrales, escepticos, bloqueadores e influenciadores.
- En cada ronda registrar reacciones, razones, citas plausibles, senales comportamentales y patrones emergentes.
- Entrevistar minimo 7 agentes: 2 promotores, 2 escepticos, 1 bloqueador, 1 influenciador, 1 ambiguo.
- Toda recomendacion debe tener: evidencia simulada, mecanismo causal, riesgo y experimento.
- Mantener tono de war room estrategico: directo, vivo, no fantasioso.
- Evitar recomendaciones genericas que no esten conectadas a comportamiento simulado.

## Cierre

Solo declarar un simulador/caso "completo" cuando existan:

- Brief operativo.
- Mapa social.
- 15+ agentes.
- 3+ rondas.
- Entrevistas.
- Mapa causal.
- Prescripciones.
- Experimentos.
- War room final.
