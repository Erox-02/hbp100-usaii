# HBP100-USAII

**AI-powered document understanding with privacy-preserving LLM workflows**

HBP100-USAII is a demonstration application built on top of **HBP100 v2**, a lightweight contextual privacy firewall.

It helps patients, families, and caregivers understand medical and insurance documents in plain language while protecting sensitive information before external AI processing.

---

## Problem

People often receive discharge instructions, insurance approvals, and healthcare documents that are difficult to understand.

Many turn to AI for explanations, but sharing these documents can expose sensitive information such as:

* Names
* Emails
* Phone numbers
* Medical record numbers
* Dates
* Hospital names

HBP100-USAII allows users to obtain AI-generated explanations without exposing personal information externally.

---

## Solution

Documents are processed through HBP100 before reaching the language model.

Sensitive information is replaced with placeholders.

The LLM generates explanations and checklists using only masked text.

Original information is restored locally after processing.

---

## Workflow

```text
Official letter/Hospital report
        ↓
HBP100 v2
        ↓
Entity Extractors
        ↓
LightGBM Policy Engine
        ↓
Placeholder Generator
        ↓
Metadata Vault
        ↓
Masked Prompt
        ↓
Groq Llama-3.3-70B
        ↓
Explanation + Checklist
        ↓
Placeholder Validation
        ↓
Restoration
        ↓
Final Response
```

---

## Features

* Privacy-preserving AI explanations
* Plain-language summaries
* Checklist generation
* Placeholder validation
* Metadata vault
* Reversible masking
* Human-in-the-loop design
* Medical safety guardrails
* Mobile friendly web interface
* FastAPI backend
* Vercel deployment

---

## Example

### Input

```text
Patient John Doe (MRN: 48291) was diagnosed with Type 2 Diabetes.

Prescribed Metformin 500mg BID.

Schedule a follow-up appointment within 7 days.

Contact patient Sarah Johnson at (555) 123-4567.

Explain the treatment plan in simple language and create a checklist.
```

---

### Masked Prompt

```text
Patient [NAME_1] (MRN: [MRN_1])

...

Contact patient [PHONE_1]

...
```

---

### AI Response

* Explain instructions in plain language
* Generate checklist
* Highlight warnings
* Preserve placeholders

---

### Restored Output

Sensitive values are restored locally.

No sensitive information leaves the device.

---

## Architecture

### Frontend

* React
* Vite
* Tailwind CSS

### Backend

* FastAPI
* Groq API
* HBP100 v2

### AI Components

* TF-IDF
* LightGBM policy engine
* Placeholder validator
* Llama-3.3-70B

---

## Performance

### Privacy Engine Only

Average request latency:

**≈388 ms**

(preloaded model)

---

### Full Pipeline

Privacy masking + Groq inference + restoration

Average response latency:

**≈2.3 seconds**

---

## Responsible AI

### Risk

Users may over-rely on AI explanations.

### Mitigation

The system only explains information already present.

It never:

* Diagnoses diseases
* Prescribes medication
* Changes dosages
* Makes legal or financial decisions

---

## Human-in-the-Loop

HBP100-USAII does not replace professionals.

Final medical, legal, and financial decisions remain with qualified humans.

The system acts as an explanation tool, not a decision-maker.

---

## Built With

### Frontend

* React
* Vite
* Tailwind CSS

### Backend

* FastAPI

### AI

* Groq
* Llama-3.3-70B
* Hbp100-v2

### Privacy Engine

* Hbp100-v2
* Regex Extractors

---

## Core Package

HBP100 v2

https://github.com/Erox-02/humming-bird-v2

---

## Repository

https://github.com/Erox-02/hbp100-usaii

---

## License

MIT License

---

## Author

Dipanjan Dutta

---

Built for the USAII Global AI Hackathon 2026.
