# SimLab-lite

SimLab-lite is a conversational social marketing simulation engine for Codex, ChatGPT Code and Claude.

It is not an app, backend or dashboard. It is a lightweight operating system for marketing war rooms: build a small simulated market, run social reaction rounds, interview agents, map causal hypotheses and end with decisions plus experiments.

## What It Does

- Turns a marketing brief into a structured social simulation.
- Creates 15-30 synthetic market agents.
- Runs 3-5 social reaction rounds.
- Interviews promoters, skeptics, blockers, influencers and ambiguous agents.
- Builds causal hypotheses from simulated behavior.
- Prescribes strategic moves and experiments.
- Stores local session memory in case folders.

## Repository Structure

```text
SKILL.md
agents/openai.yaml
references/
  workflow.md
  agent_bank.md
  causal_prescriptive.md
  operator_playbook.md
scripts/
  create_case.py
  validate_case.py
  write_demo_case.py
assets/
  templates/
  demo_case/
```

## Quick Use

Use the skill in Codex with a prompt like:

```text
Simulemos socialmente esta campaña de marketing.
Quiero 18 agentes, 5 rondas, entrevistas, mapa causal, prescripciones y experimentos.
Guarda memoria local del caso.
```

## Create A Case

```bash
python scripts/create_case.py mi-campana --root cases --agents 18
```

## Validate A Case

```bash
python scripts/validate_case.py cases/mi-campana --json
```

## Demo

The included demo case validates as complete:

```bash
python scripts/validate_case.py assets/demo_case --json
```

Expected result:

```json
{
  "status": "complete",
  "completion_score": 100
}
```

## Philosophy

The simulation generates hypotheses.  
The causal layer organizes mechanisms.  
The prescriptive layer decides what to test.

Do not treat synthetic agents as real-world evidence. Use this to think better before spending money on campaigns.

