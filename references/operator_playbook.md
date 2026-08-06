# Operator Playbook

## Modo Conversacional

Cuando el usuario entregue un brief, responder en etapas. No descargar todo el motor de golpe si el usuario esta explorando. Si pide "completo", crear memoria local y producir todos los artefactos.

## Secuencia De Respuesta

1. Confirmar objetivo.
2. Crear/actualizar caso local.
3. Escribir brief normalizado.
4. Construir mapa social.
5. Crear agentes.
6. Simular rondas.
7. Entrevistar.
8. Mapear causalidad.
9. Prescribir.
10. Disenar experimentos.
11. Validar caso.
12. Entregar resumen final con rutas.

## Comandos Del Usuario

- `/brief`: normalizar o corregir brief.
- `/mapa-social`: construir actores y tensiones.
- `/agentes`: crear o ajustar agentes.
- `/simular`: ejecutar rondas.
- `/entrevistar`: entrevistar agentes.
- `/causal`: generar hipotesis causales.
- `/prescribir`: generar decisiones.
- `/experimentos`: generar pruebas.
- `/war-room`: cerrar con sintesis ejecutiva.
- `/recalibrar`: incorporar datos nuevos y ajustar agentes/hipotesis.

## Recalibracion

Cuando el usuario trae datos reales:

1. Registrar como hechos, no supuestos.
2. Comparar contra patrones simulados.
3. Ajustar confianza de hipotesis.
4. Mantener lo contradicho como aprendizaje, no borrarlo.
5. Proponer nueva ronda o experimento.

## Completo Vs Exploratorio

Completo requiere archivos y validacion. Exploratorio puede responder solo en chat.

No declarar completo si `validate_case.py` falla, salvo que expliques exactamente que falta.

