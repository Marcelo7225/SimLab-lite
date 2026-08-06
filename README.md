# SimLab-lite

> Motor conversacional de simulación social para marketing.
> Diseñado para usarse dentro de Codex, ChatGPT Code o Claude, sin app, sin backend y sin dashboard obligatorio.

SimLab-lite convierte un brief de marketing en una simulación social estructurada: crea agentes pequeños, corre rondas de reacción, entrevista perfiles clave, organiza hipótesis causales y termina en un war room estratégico con decisiones y experimentos.

No pretende adivinar el mercado. Sirve para pensar mejor antes de gastar dinero, ordenar supuestos, detectar fricción social y diseñar pruebas con disciplina causal.

Ahora también incluye un **Research Report Strategist**: un especialista que transforma la simulación en un informe ejecutivo de investigación, pensado para presentar el trabajo a clientes o equipos directivos.

## Qué Es

```text
Brief de marketing
       |
       v
Mapa social del mercado
       |
       v
15-30 agentes sintéticos
       |
       v
Rondas de reacción social
       |
       v
Entrevistas a agentes clave
       |
       v
Hipótesis causales
       |
       v
Decisiones + experimentos
       |
       v
War room estratégico final
       |
       v
Informe ejecutivo de investigación
```

## Para Qué Sirve

SimLab-lite es útil cuando necesitas explorar preguntas como:

- Qué audiencia podría activar o bloquear una campaña.
- Qué objeciones aparecerían antes de invertir pauta.
- Qué mensaje puede cambiar intención, confianza o urgencia.
- Qué segmentos reaccionan distinto ante precio, promesa, canal o prueba social.
- Qué experimentos conviene correr primero.
- Qué decisiones estratégicas tienen mayor potencial y menor riesgo.
- Cómo explicar el rigor de la simulación en un informe vendible para cliente.

## Lo Que Incluye

| Componente | Función |
|---|---|
| `SKILL.md` | Instrucciones principales para que Codex use el simulador como skill conversacional. |
| `agents/openai.yaml` | Configuración de agente para Codex/OpenAI. |
| `references/workflow.md` | Flujo completo de operación por fases. |
| `references/agent_bank.md` | Banco de 24 arquetipos de agentes de marketing. |
| `references/causal_prescriptive.md` | Marco causal y prescriptivo para decisiones y experimentos. |
| `references/research_reporting.md` | Guía del especialista en informes ejecutivos de investigación. |
| `references/operator_playbook.md` | Guía práctica para correr sesiones, recalibrar y cerrar casos. |
| `assets/templates/` | Plantillas locales para cada sesión. |
| `assets/demo_case/` | Caso de demostración ya completo. |
| `scripts/create_case.py` | Crea una carpeta de caso con memoria local. |
| `scripts/validate_case.py` | Valida si un caso está completo. |
| `scripts/write_demo_case.py` | Genera el caso demo incluido. |

## Instalación

### Opción 1: Usarlo como repo normal

Clona el repositorio:

```bash
git clone https://github.com/Marcelo7225/SimLab-lite.git
cd SimLab-lite
```

Verifica que todo funcione:

```bash
python scripts/validate_case.py assets/demo_case --json
```

Si ves `"status": "complete"` y `"completion_score": 100`, el simulador está listo.

### Opción 2: Instalarlo como skill local de Codex

Clona el repo dentro de tu carpeta de skills:

```bash
cd ~/.codex/skills
git clone https://github.com/Marcelo7225/SimLab-lite.git social-marketing-sim
```

Luego abre Codex y pídele algo como:

```text
Usa social-marketing-sim.
Simulemos una campaña de marketing para una nueva oferta B2B.
Quiero 20 agentes, 5 rondas, entrevistas, mapa causal, decisiones y experimentos.
Incluye informe ejecutivo de investigación para cliente.
```

Codex leerá el `SKILL.md`, usará las referencias necesarias y podrá crear archivos locales por sesión.

### Opción 3: Usarlo en Claude o ChatGPT Code sin instalar skill

También puedes usarlo como paquete de instrucciones:

1. Clona o descarga este repositorio.
2. Abre el archivo `SKILL.md`.
3. Copia sus instrucciones principales en tu conversación.
4. Adjunta o referencia estos archivos cuando quieras más estructura:
   - `references/workflow.md`
   - `references/agent_bank.md`
   - `references/causal_prescriptive.md`
   - `references/operator_playbook.md`
5. Pide que cree una carpeta de caso usando las plantillas de `assets/templates/`.

Prompt recomendado:

```text
Quiero correr SimLab-lite como motor conversacional.
Usa el flujo del SKILL.md y las referencias del repo.
Crea una simulación social de marketing con memoria local por sesión,
agentes sintéticos, rondas, entrevistas, hipótesis causales,
prescripciones y war room final.
Si el caso es para presentar a cliente, genera también el informe ejecutivo de investigación.
```

## Uso Rápido

Crear un caso vacío:

```bash
python scripts/create_case.py mi-campana --root cases --agents 18
```

Validar el caso:

```bash
python scripts/validate_case.py cases/mi-campana --json
```

Validar el demo:

```bash
python scripts/validate_case.py assets/demo_case --json
```

Generar de nuevo el demo:

```bash
python scripts/write_demo_case.py
```

## Estructura De Un Caso

Cada sesión puede vivir en una carpeta local con esta forma:

```text
cases/mi-campana/
  00_brief.md
  01_social_map.md
  02_agents.json
  03_rounds.jsonl
  04_interviews.md
  05_causal_map.md
  06_prescriptions.md
  07_experiments.md
  08_war_room_final.md
  09_research_report.md
  CASE_INDEX.md
  session.json
  memory/
    facts.json
    assumptions.json
    unresolved_questions.json
    decisions.jsonl
    checkpoints.jsonl
```

## Flujo De Trabajo

1. **Brief**
   Define oferta, mercado, audiencia, objetivo, restricciones y señales disponibles.

2. **Mapa social**
   Identifica grupos, tensiones, canales, incentivos, fricciones y presión social.

3. **Agentes**
   Crea entre 15 y 30 perfiles pequeños con motivaciones, objeciones, contexto y sensibilidad a mensajes.

4. **Rondas**
   Simula exposición, reacción, conversación, contagio, bloqueo, reconsideración y decisión.

5. **Entrevistas**
   Pregunta a promotores, escépticos, bloqueadores, ambiguos e influenciadores qué cambió y qué no.

6. **Causalidad**
   Traduce patrones en hipótesis: variable de intervención, mecanismo, resultado esperado, moderadores y riesgos.

7. **Prescripción**
   Convierte hipótesis en decisiones, secuencia táctica y experimentos medibles.

8. **War room**
   Cierra con una lectura estratégica viva, pero disciplinada: qué hacer, qué no hacer, qué probar y qué observar.

9. **Informe de investigación**
   Explica qué se hizo, cómo funcionó la simulación, qué agentes participaron, qué ocurrió en las rondas, qué revelaron las entrevistas, qué hipótesis causales surgieron y qué experimentos A/B se recomiendan.

## Salida Final Esperada

Un buen cierre de SimLab-lite debe incluir:

- Decisiones recomendadas.
- Decisiones descartadas o pospuestas.
- Hipótesis causales priorizadas.
- Experimentos de marketing.
- Segmentos sensibles.
- Mensajes con potencial.
- Objeciones críticas.
- Riesgos de interpretación.
- Señales que deberían medirse en el mundo real.
- Informe ejecutivo de investigación cuando el resultado deba vender, justificar o presentar el rigor del trabajo.

## Principios

- La simulación no es evidencia real.
- Los agentes sintéticos no reemplazan clientes.
- La causalidad se formula como hipótesis, no como certeza.
- La prescripción debe terminar en experimentos observables.
- La memoria local existe para que la sesión no se vuelva humo conversacional.

## Ejemplo De Prompt Completo

```text
Usa SimLab-lite para simular socialmente esta campaña:

Oferta: asesoría de automatización comercial para pymes B2B.
Mercado: Colombia.
Objetivo: generar demos calificadas.
Audiencia: dueños, gerentes comerciales y líderes de operación.
Canales: LinkedIn, WhatsApp, referidos y email.
Restricción: presupuesto limitado, máximo 4 semanas.

Quiero:
- 20 agentes.
- 5 rondas de reacción social.
- Entrevistas a perfiles extremos y ambiguos.
- Mapa causal.
- Decisiones prescriptivas.
- 5 experimentos.
- War room final con disciplina causal.
- Informe ejecutivo de investigación para cliente.
```

## Estado Del Proyecto

SimLab-lite está pensado como versión limpia y ligera, inspirada en ideas de simulación social y sistemas causales/prescriptivos, pero enfocada en uso conversacional.

No incluye interfaz gráfica, servidor, base de datos ni ejecución estadística pesada. Su valor está en la estructura: ayuda a pensar una campaña como un sistema social, no solo como una lista de copies.
