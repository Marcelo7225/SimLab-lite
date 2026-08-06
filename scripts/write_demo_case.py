#!/usr/bin/env python
"""Write a complete demo case for validating the social-marketing-sim workflow."""

from __future__ import annotations

import json
from pathlib import Path


def write(path: Path, content: str) -> None:
    path.write_text(content.strip() + "\n", encoding="utf-8")


def main() -> int:
    case_dir = Path(__file__).resolve().parents[1] / "assets" / "demo_case"
    case_dir.mkdir(parents=True, exist_ok=True)

    write(case_dir / "00_brief.md", """
# Brief Operativo

## Identificacion

- case_name: Educacion Online Colombia
- brand: Plataforma educativa anonima
- product_or_offer: Cursos cortos certificados para profesionales de 25-40 anos
- market: Colombia
- date: 2026-08-06

## Decision

- decision_to_inform: Que mensaje y canal priorizar para aumentar leads calificados.
- business_goal: Aumentar leads calificados sin deteriorar confianza.
- decision_deadline: Proxima planeacion de campana.

## Estimulo

- stimulus_type: Mensaje de campana
- stimulus_description: "Certificados que ayudan a demostrar habilidades reales ante empleadores."
- current_message: Certificacion practica para avanzar profesionalmente.
- alternative_messages: Prueba de habilidades, empleabilidad, portafolio, mentorias.

## Audiencia

- target_audience: Profesionales colombianos de 25-40 anos que buscan mejorar empleabilidad.
- known_segments: profesionales presionados, investigadores silenciosos, escepticos de certificados, aspiracionales selectivos.
- excluded_segments: estudiantes sin intencion laboral inmediata.

## Mercado

- competitors: Platzi, Coursera, diplomados universitarios, YouTube.
- substitutes: tutoriales gratis, experiencia laboral, bootcamps, cursos internos de empresa.
- category_context: Alta oferta de educacion online y fatiga frente a promesas de empleabilidad.
- cultural_context: La confianza aumenta con prueba social local, casos concretos y respaldo profesional.

## Restricciones

- channels: LinkedIn, Meta, Google Search, WhatsApp.
- budget_level: medio.
- timing: campana de 4-6 semanas.
- legal_or_brand_constraints: Evitar prometer empleo garantizado.

## Evidencia Disponible

- user_provided: Objeciones sobre certificados, tiempo y empleabilidad.
- research: No aportada.
- customer_comments: No aportados.
- sales_data: No aportada.
- campaign_data: No aportada.
- assumptions: El certificado aislado no basta; debe probar habilidad aplicable.
- unknowns: Precio, marca, historial de reputacion, tasa de conversion base.

## Objeciones Esperadas

- objection_1: "Otro certificado mas no me ayuda a conseguir trabajo."
- objection_2: "No tengo tiempo para empezar y abandonar."
- objection_3: "Prefiero algo reconocido o gratis."
""")

    write(case_dir / "01_social_map.md", """
# Mapa Social

## Actores

- Compradores: profesionales 25-40 con deseo de movilidad laboral.
- Usuarios: personas que tomarian cursos fuera del horario laboral.
- Influenciadores: expertos de LinkedIn, reclutadores, pares que ya estudiaron.
- Bloqueadores: escepticos de certificados, decisores financieros personales, comparadores contra gratis.
- Decisores: el propio profesional y, en algunos casos, su pareja/familia por presupuesto.
- Competidores: Platzi, Coursera, universidades, bootcamps.
- Sustitutos: YouTube, experiencia laboral, proyectos propios.

## Segmentos Iniciales

| Segmento | Motivacion | Objecion | Canal | Peso estimado |
|---|---|---|---|---|
| Profesional presionado | empleabilidad y ahorro de tiempo | onboarding lento | LinkedIn/Search | medio |
| Investigador silencioso | aprender antes de entregar datos | formularios tempranos | SEO/YouTube | alto |
| Esceptico informado | evitar promesas falsas | certificado generico | LinkedIn/reviews | medio |
| Aspiracional selectivo | senal de progreso | marca poco prestigiosa | Instagram/LinkedIn | medio |
| Decisor financiero personal | controlar gasto | ROI incierto | WhatsApp/Search | medio |

## Relaciones De Influencia

- Reclutadores y expertos legitiman si hablan de habilidades observables.
- Pares confiables reducen riesgo si muestran resultado concreto.
- Escepticos pueden contaminar comentarios si el claim suena a empleo garantizado.
- Google Search captura intencion cuando la persona ya compara opciones.

## Narrativas

- Favorable: "No es solo certificado; es evidencia de habilidad."
- Neutral: "Puede servir si es corto y aplicable."
- Critica: "Los certificados online no pesan si no hay experiencia."
- Competidora: "Una plataforma reconocida tiene mas senal."

## Tensiones

- Funcional: habilidad real vs diploma decorativo.
- Emocional: esperanza de progreso vs miedo a ser enganado.
- Economica: inversion moderada vs alternativas gratis.
- Cultural: confianza local vs marca generica.
- Reputacional: prometer empleabilidad puede sonar manipulador.

## Puntos

- Contagio: casos reales de personas contratadas o promovidas.
- Friccion: falta de tiempo, precio, credibilidad.
- Malentendido: interpretar certificado como promesa de empleo.
- Validacion: reclutador o experto mostrando criterios de habilidad.
""")

    agents = []
    archetypes = [
        ("A01", "Profesional presionada", "Profesional presionado", "compradora probable", "LinkedIn"),
        ("A02", "Investigador silencioso", "Investigador silencioso", "neutral", "Google Search"),
        ("A03", "Esceptico de certificados", "Esceptico informado", "esceptico", "LinkedIn"),
        ("A04", "Aspiracional selectiva", "Aspiracional selectivo", "receptiva", "Instagram"),
        ("A05", "Decisor financiero personal", "Decisor financiero", "bloqueador economico", "Google Search"),
        ("A06", "Recomendado confiado", "Recomendado confiado", "comprador por referido", "WhatsApp"),
        ("A07", "Compradora tecnica", "Comprador tecnico", "evaluadora", "web/demo"),
        ("A08", "Cazador de promociones", "Cazador de promociones", "sensible a precio", "Meta"),
        ("A09", "Influenciador experto", "Influenciador experto", "influenciador", "LinkedIn"),
        ("A10", "Reclutadora pragmatica", "Influenciador interno", "validadora", "LinkedIn"),
        ("A11", "Usuario saturado", "Usuario saturado", "indiferente", "Instagram"),
        ("A12", "Planificador largo plazo", "Planificador de largo plazo", "analitico", "LinkedIn"),
        ("A13", "Experimentador curioso", "Experimentador curioso", "early adopter", "TikTok"),
        ("A14", "Cliente reactivado", "Usuario reactivado", "dudoso", "email"),
        ("A15", "Comparador racional", "Optimizador de valor", "comparador", "YouTube"),
        ("A16", "Par confiable", "Par confiable", "influenciador cercano", "WhatsApp"),
        ("A17", "Minimalista funcional", "Minimalista funcional", "pragmatico", "web"),
        ("A18", "Detractor reputacional", "Detractor reputacional", "bloqueador narrativo", "comentarios"),
    ]
    for i, (aid, name, segment, role, channel) in enumerate(archetypes, start=1):
        agents.append({
            "agent_id": aid,
            "name": name,
            "segment": segment,
            "role": role,
            "motivations": ["mejorar empleabilidad", "reducir incertidumbre"],
            "objections": ["certificado generico", "falta de tiempo", "ROI poco claro"],
            "influence_level": 0.8 if "Influenciador" in name or "Reclutadora" in name or "Par" in name else 0.4,
            "risk_sensitivity": 0.75,
            "price_sensitivity": 0.8 if "financiero" in role or "precio" in role else 0.5,
            "channel_habits": [channel],
            "baseline_belief": "Quiere evidencia concreta antes de dejar datos o pagar.",
            "decision_trigger": "Prueba local de habilidad aplicable y resultado plausible.",
            "likely_reaction": "interes condicionado" if i not in [3, 5, 18] else "resistencia inicial",
            "notes": "Agente sintetico para simulacion, no dato real."
        })
    (case_dir / "02_agents.json").write_text(json.dumps({
        "case_name": "Educacion Online Colombia",
        "agent_count": len(agents),
        "agents": agents
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    rounds = []
    for round_num, stimulus, pattern in [
        (1, "Mensaje base centrado en certificado para empleabilidad.", "Interes inicial, pero certificado aislado genera sospecha."),
        (2, "Conversacion social comparando contra Platzi, Coursera y YouTube.", "La confianza depende de reconocimiento y evidencia concreta."),
        (3, "Objeciones: tiempo, precio y promesa de empleo.", "El claim se polariza si parece garantizar trabajo."),
        (4, "Ajuste: portafolio verificable + mini proyecto + aval de reclutador.", "Sube confianza en pragmaticos y escepticos moderados."),
        (5, "Secuencia propuesta: contenido educativo -> caso local -> WhatsApp consultivo.", "Mejor adopcion cuando se reduce presion comercial inicial."),
    ]:
        rounds.append({
            "round": round_num,
            "stimulus": stimulus,
            "agent_reactions": [
                {"agent_id": "A01", "reaction": "interes", "reason": "ve utilidad si ahorra tiempo", "quote": "Si me muestran que salgo con algo demostrable, lo miro.", "behavioral_signal": "clic a landing", "confidence": "media"},
                {"agent_id": "A03", "reaction": "duda", "reason": "rechaza certificados decorativos", "quote": "Certificado no es lo mismo que habilidad.", "behavioral_signal": "lee pruebas antes de actuar", "confidence": "alta"},
                {"agent_id": "A09", "reaction": "condicional", "reason": "solo recomendaria si hay sustancia", "quote": "Mostraria el proyecto final, no el diploma.", "behavioral_signal": "podria compartir si hay caso tecnico", "confidence": "media"},
                {"agent_id": "A18", "reaction": "critica", "reason": "detecta promesa inflada", "quote": "Otra marca vendiendo empleabilidad facil.", "behavioral_signal": "comentario negativo", "confidence": "media"}
            ],
            "emergent_patterns": [pattern],
            "narrative_shift": pattern,
            "assumptions_changed": [],
            "causal_mechanisms_tested": ["prueba_social -> confianza", "claridad_de_habilidad -> intencion", "promesa_excesiva -> desconfianza"],
            "notes": "Ronda sintetica para validar flujo."
        })
    (case_dir / "03_rounds.jsonl").write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rounds) + "\n", encoding="utf-8")

    write(case_dir / "04_interviews.md", """
# Entrevistas A Agentes

## Seleccion

- Promotores: A01, A04
- Escepticos: A03, A15
- Bloqueadores: A18
- Influenciadores: A09, A10
- Ambiguos: A02

### INT-01 A01
- agent_id: A01
- segmento: Profesional presionado
- pregunta: Que te haria dejar tus datos?
- respuesta: "Un ejemplo claro de proyecto final y cuanto tiempo real me toma."
- interpretacion: La claridad operativa desbloquea accion.
- pista_causal: claridad_de_esfuerzo -> menor_friccion -> lead.
- confianza: media

### INT-02 A04
- agent_id: A04
- segmento: Aspiracional selectivo
- pregunta: Que te atrae?
- respuesta: "Me sirve si se ve profesional y no como curso masivo barato."
- interpretacion: La senal de estatus sobrio importa.
- pista_causal: identidad_profesional -> valor_percibido -> interes.
- confianza: media

### INT-03 A03
- agent_id: A03
- segmento: Esceptico informado
- pregunta: Que te frena?
- respuesta: "Que vendan certificado como si fuera empleo."
- interpretacion: El claim de empleabilidad debe matizarse.
- pista_causal: promesa_excesiva -> desconfianza -> rechazo.
- confianza: alta

### INT-04 A15
- agent_id: A15
- segmento: Optimizador de valor
- pregunta: Como comparas?
- respuesta: "Contra Coursera y YouTube. Si pago, necesito acompanamiento o proyecto revisado."
- interpretacion: El pago necesita valor diferencial.
- pista_causal: diferenciacion -> justificacion_precio -> conversion.
- confianza: media

### INT-05 A18
- agent_id: A18
- segmento: Detractor reputacional
- pregunta: Que criticarias publicamente?
- respuesta: "Que prometan futuro laboral sin hacerse cargo."
- interpretacion: Riesgo de backlash si el mensaje exagera.
- pista_causal: claim_absoluto -> reaccion_critica -> dano_confianza.
- confianza: media

### INT-06 A09
- agent_id: A09
- segmento: Influenciador experto
- pregunta: Que recomendarias?
- respuesta: "Mostrar rubrica, proyecto final y criterio de reclutadores."
- interpretacion: Autoridad tecnica puede legitimar.
- pista_causal: autoridad_experta -> credibilidad -> intencion.
- confianza: alta

### INT-07 A10
- agent_id: A10
- segmento: Reclutadora pragmatica
- pregunta: Que validas?
- respuesta: "No miro solo certificado; miro evidencia de habilidad y comunicacion del proyecto."
- interpretacion: El mensaje debe hablar de demostracion, no de diploma.
- pista_causal: evidencia_habilidad -> relevancia_laboral -> confianza.
- confianza: alta

### INT-08 A02
- agent_id: A02
- segmento: Investigador silencioso
- pregunta: Cuando darias tus datos?
- respuesta: "Despues de leer temario, ver resultados y comparar precio."
- interpretacion: Landing abierta antes de captura mejora confianza.
- pista_causal: informacion_sin_presion -> confianza -> lead.
- confianza: media

## Sintesis

- Que convencio: proyecto verificable, aval experto, claridad de tiempo.
- Que freno: promesa de empleo, certificado generico, precio sin diferenciacion.
- Que sono falso: empleabilidad garantizada o demasiado facil.
- Que prueba falta: casos locales y ejemplos de proyectos.
- Que cambio desbloquea accion: pasar de "certificado" a "evidencia de habilidad aplicable".
""")

    write(case_dir / "05_causal_map.md", """
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
""")

    write(case_dir / "06_prescriptions.md", """
# Prescripciones

## Decisiones Recomendadas

### Decision 1
- Que hacer: Reposicionar el claim principal hacia "demuestra habilidades con un proyecto verificable".
- Razon social: agentes escepticos y reclutadores rechazaron el certificado aislado.
- Razon causal: claridad_de_habilidad -> confianza -> lead_calificado.
- Segmento: profesionales presionados y escepticos moderados.
- Canal: LinkedIn y Search.
- Riesgo: sonar demasiado tecnico para aspiracionales.
- Experimento: A/B certificado vs proyecto verificable.

### Decision 2
- Que hacer: Incluir pieza con reclutador/experto explicando que evidencia mira.
- Razon social: influenciador experto y reclutadora legitimaron criterios concretos.
- Razon causal: autoridad_experta -> credibilidad -> intencion.
- Segmento: comparadores y escepticos.
- Canal: LinkedIn, webinar corto, landing.
- Riesgo: experto poco creible o demasiado corporativo.
- Experimento: pieza con experto vs pieza de marca.

### Decision 3
- Que hacer: Abrir temario, proyecto ejemplo y tiempos antes de pedir datos.
- Razon social: investigador silencioso evita formularios tempranos.
- Razon causal: informacion_sin_presion -> confianza -> lead.
- Segmento: investigadores silenciosos.
- Canal: SEO/Search/landing.
- Riesgo: menos leads brutos de corto plazo.
- Experimento: landing abierta vs gated.

### Decision 4
- Que hacer: Usar WhatsApp consultivo solo despues de senal de interes.
- Razon social: presion comercial temprana activa rechazo.
- Razon causal: control_usuario -> menor_friccion -> conversacion_calificada.
- Segmento: pragmaticos y sensibles a riesgo.
- Canal: WhatsApp.
- Riesgo: respuesta lenta deteriora confianza.
- Experimento: CTA "ver proyecto" vs "hablar con asesor".

### Decision 5
- Que hacer: Evitar claims de empleo garantizado.
- Razon social: detractor y escepticos lo convierten en narrativa negativa.
- Razon causal: promesa_excesiva -> desconfianza -> rechazo_publico.
- Segmento: escepticos, expertos, detractores.
- Canal: todos.
- Riesgo: perder fuerza comercial si se matiza demasiado.
- Experimento: claim de empleabilidad matizado vs claim fuerte en pretest.

## No Hacer

- Evitar: vender "certificado = empleo".
- Porque: activa desconfianza y comparacion desfavorable.
- Senal de alerta: comentarios preguntando por garantias de empleo.

## Priorizacion

| Prioridad | Accion | Segmento | Impacto esperado | Incertidumbre | Esfuerzo |
|---|---|---|---|---|---|
| 1 | Claim proyecto verificable | profesionales/escepticos | alto | media | medio |
| 2 | Autoridad reclutador | comparadores | medio-alto | media | medio |
| 3 | Landing abierta | investigadores | medio | media | bajo |
| 4 | WhatsApp consultivo | pragmaticos | medio | media | medio |
| 5 | Pretest anti-backlash | escepticos | defensivo alto | baja | bajo |
""")

    write(case_dir / "07_experiments.md", """
# Experimentos

## Experimento 1
- Hipotesis: Si el claim enfatiza proyecto verificable, aumentaran leads calificados frente a claim de certificado.
- Segmento: profesionales 25-40.
- Variante A: "Obten un certificado profesional."
- Variante B: "Construye un proyecto que demuestre tu habilidad ante empleadores."
- Canal: Google Search / landing.
- Metrica primaria: lead calificado.
- Metrica secundaria: clic a proyecto ejemplo.
- Tamano minimo recomendado: minimo dos semanas o trafico suficiente para senal direccional.
- Criterio de decision: escalar B si mejora calidad sin deteriorar volumen critico.
- Senal de fallo: aumento de rebote o menor comprension.
- Riesgo de interpretacion: diferencia puede deberse a creatividad, no solo claim.

## Experimento 2
- Hipotesis: Si un reclutador explica criterios de habilidad, subira confianza en escepticos.
- Segmento: escepticos y comparadores.
- Variante A: anuncio de marca.
- Variante B: video corto con reclutador.
- Canal: LinkedIn.
- Metrica primaria: tasa de conversion a lead.
- Metrica secundaria: comentarios cualitativos positivos.
- Tamano minimo recomendado: 2 creatividades por 10 dias.
- Criterio de decision: escalar si B mejora conversion y sentimiento.
- Senal de fallo: baja credibilidad del vocero.
- Riesgo de interpretacion: autoridad del vocero no generaliza.

## Experimento 3
- Hipotesis: Si la landing permite explorar sin formulario, aumentara confianza y calidad de lead.
- Segmento: investigadores silenciosos.
- Variante A: formulario temprano.
- Variante B: temario/proyecto abierto antes del formulario.
- Canal: Search/SEO.
- Metrica primaria: lead calificado.
- Metrica secundaria: tiempo en pagina y retorno.
- Tamano minimo recomendado: 2 semanas.
- Criterio de decision: mantener B si calidad sube aunque volumen bruto baje moderadamente.
- Senal de fallo: caida fuerte de leads sin mejora de calidad.
- Riesgo de interpretacion: tracking de calidad incompleto.

## Experimento 4
- Hipotesis: Si WhatsApp se ofrece despues de ver proyecto, la conversacion sera mas calificada.
- Segmento: pragmaticos sensibles a riesgo.
- Variante A: CTA directo a asesor.
- Variante B: CTA ver proyecto, luego WhatsApp.
- Canal: landing/WhatsApp.
- Metrica primaria: conversaciones calificadas.
- Metrica secundaria: tiempo de respuesta y show rate.
- Tamano minimo recomendado: 100 conversaciones.
- Criterio de decision: escalar B si reduce preguntas basicas repetidas.
- Senal de fallo: menos conversaciones sin mejora de calidad.
- Riesgo de interpretacion: calidad depende del asesor.

## Experimento 5
- Hipotesis: Un claim matizado de empleabilidad reducira backlash sin perder interes.
- Segmento: audiencia fria en Meta/LinkedIn.
- Variante A: "Mejora tu empleabilidad con certificados."
- Variante B: "Demuestra habilidades aplicables con proyectos revisables."
- Canal: Meta/LinkedIn.
- Metrica primaria: sentimiento de comentarios.
- Metrica secundaria: CTR y lead.
- Tamano minimo recomendado: pretest con comentarios monitoreados.
- Criterio de decision: usar B si mantiene CTR y reduce objeciones.
- Senal de fallo: B no comunica beneficio.
- Riesgo de interpretacion: bajo volumen de comentarios.

## Senales De Monitoreo

- Positiva: preguntas sobre proyecto final y temario.
- Negativa: comentarios sobre promesas falsas de empleo.
- Saturacion: caida de CTR con frecuencia alta.
- Backlash: menciones comparando negativamente con certificados sin valor.
""")

    write(case_dir / "08_war_room_final.md", """
# War Room Final

## 1. Situacion

La campana busca aumentar leads calificados para cursos certificados en Colombia. La tension principal es que el certificado puede atraer atencion, pero tambien activar desconfianza si se percibe como promesa laboral vacia.

## 2. Lectura Social

El mercado simulado no rechaza la educacion online; rechaza la promesa generica. Los agentes mas valiosos quieren evidencia de habilidad, claridad de tiempo y una razon para pagar frente a alternativas gratuitas o mas reconocidas.

## 3. Narrativas Emergentes

- Favorable: "Esto me ayuda a demostrar una habilidad."
- Condicional: "Me sirve si es corto, serio y aplicable."
- Critica: "Otro certificado que promete empleo."
- Competidora: "Una marca reconocida pesa mas."

## 4. Hipotesis Causales

- H1: Proyecto verificable aumenta confianza mas que certificado aislado.
- H2: Autoridad de reclutador traduce el curso a valor laboral.
- H3: Informacion abierta reduce defensa comercial.
- H4: Promesa excesiva aumenta rechazo publico.

## 5. Segmentos Prioritarios

Priorizar profesionales presionados, investigadores silenciosos y escepticos moderados. No optimizar primero para cazadores de promociones, porque pueden subir volumen sin calidad.

## 6. Decisiones Recomendadas

1. Cambiar claim hacia proyecto/habilidad verificable.
2. Usar reclutador o experto como validador.
3. Abrir temario y ejemplo antes de capturar datos.
4. Usar WhatsApp como continuacion consultiva, no presion inicial.
5. Eliminar cualquier promesa de empleo garantizado.

## 7. Experimentos

Correr cinco pruebas: claim, autoridad experta, landing abierta, secuencia WhatsApp y pretest anti-backlash.

## 8. Riesgos

- Sonar generico frente a competidores reconocidos.
- Generar comentarios negativos por empleabilidad exagerada.
- Capturar leads de baja calidad con descuento.
- Perder volumen si se abre demasiado la landing sin CTA claro.

## 9. Senales De Monitoreo

- Lead calificado por canal.
- Clics a proyecto ejemplo.
- Preguntas sobre tiempo/resultado.
- Comentarios sobre credibilidad.
- Conversion de WhatsApp a cita o pago.

## 10. Proxima Ronda

Probar tres mensajes: certificado, proyecto verificable y aval de reclutador. Recalibrar agentes con resultados reales de CTR, comentarios y calidad de lead.
""")

    write(case_dir / "CASE_INDEX.md", """
# Case Index

- case_name: Educacion Online Colombia
- current_stage: complete
- last_updated: 2026-08-06
- owner: social-marketing-sim

## Archivos

- [x] 00_brief.md
- [x] 01_social_map.md
- [x] 02_agents.json
- [x] 03_rounds.jsonl
- [x] 04_interviews.md
- [x] 05_causal_map.md
- [x] 06_prescriptions.md
- [x] 07_experiments.md
- [x] 08_war_room_final.md

## Supuestos Activos

- La marca no tiene reputacion negativa previa conocida.
- El precio es medio.
- La calidad de lead importa mas que volumen bruto.

## Decisiones Pendientes

- Elegir primer claim A/B.
- Elegir vocero experto o reclutador.
- Definir metrica operacional de lead calificado.

## Proxima Accion

- Ejecutar experimento 1 y 2 en pequeno presupuesto.
""")

    print(str(case_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

