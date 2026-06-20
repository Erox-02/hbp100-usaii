# HBP100-USAII

**AI-powered document understanding with privacy-preserving LLM workflows**

HBP100-USAII is a demonstration application built on top of **HBP100 v2**, a lightweight contextual privacy firewall.

It helps patients, families, and caregivers understand medical and insurance documents in plain language while protecting sensitive information before external AI processing.

Built for the **USAII Global AI Hackathon 2026**.

---

# Problem

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

# Solution

Documents are processed through HBP100 before reaching the language model.

Sensitive information is replaced with placeholders.

The LLM generates explanations and checklists using only masked text.

Original information is restored locally after processing.

No sensitive information leaves the privacy layer.

---

# Workflow

```text
Official Letter / Hospital Report / Insurance Document
                        ↓
                    HBP100 v2
                        ↓
               Entity Extractors
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

# Features

* Privacy-preserving AI explanations
* Plain-language summaries
* Checklist generation
* Placeholder validation
* Metadata vault
* Reversible masking
* Human-in-the-loop design
* Medical safety guardrails
* Mobile-friendly web interface
* FastAPI backend
* Vercel deployment

---

# Example

## Input

```text
Patient John Doe (MRN: 48291) was admitted to City General Hospital with Type 2 Diabetes Mellitus and mild dehydration.

Laboratory findings showed HbA1c of 8.2% and blood glucose of 198 mg/dL.

The patient was prescribed Metformin 500 mg twice daily with meals and Lisinopril 10 mg once daily.

Instructions included maintaining hydration, following a diabetic diet, and monitoring blood glucose levels twice daily.

Seek immediate medical attention if severe dizziness, chest pain, shortness of breath, or persistent vomiting occurs.

For additional questions, email johndoe1975@gmail.com.

Explain the discharge instructions in simple language and create a checklist, but do not provide medical advice or change medications.
```

---

## Masked Prompt

```text
Patient [NAME_1] (MRN: [MRN_1]) was admitted [HOSPITAL_1] with Type 2 Diabetes Mellitus and mild dehydration.

Laboratory findings showed HbA1c of 8.2% and blood glucose of 198 mg/dL.

The patient was prescribed Metformin 500 mg twice daily with meals and Lisinopril 10 mg once daily.

Instructions included maintaining hydration, following a diabetic diet, and monitoring blood glucose levels twice daily.

Seek immediate medical attention if severe dizziness, chest pain, shortness of breath, or persistent vomiting occurs.

For additional questions, email [EMAIL_1].

Explain the discharge instructions in simple language and create a checklist, but do not provide medical advice or change medications.

```

---

## AI Response

* Explain instructions in plain language
* Generate a checklist
* Highlight warnings
* Preserve placeholders

---

## Restored Output

Sensitive values are restored , *user trades almost nothing for privact*.

Original information never leaves the privacy layer.

---

# Live Demo

Frontend

https://hbp100-usaii.vercel.app

Core Package

https://github.com/Erox-02/humming-bird-v2

Repository

https://github.com/Erox-02/hbp100-usaii

---

# Architecture

## Frontend

* React
* Vite
* Tailwind CSS

## Backend

* FastAPI
* Groq API
* HBP100 v2

## AI Components

* TF-IDF vectorizer
* LightGBM classifier
* Placeholder validator
* Groq Llama-3.3-70B

## Privacy Engine

* HBP100 v2
* Modular entity extractors
* Placeholder generation
* Metadata vault
* Restoration engine

---

# Performance

## Privacy Pipeline

Average request latency:

**≈388 ms**

(Model preloaded)

---

## End-to-End Pipeline

Privacy masking + LLM inference + restoration

Average response latency:

**≈2.3 seconds**

---

# Responsible AI

## Risk

Users may over-rely on AI explanations.

## Mitigation

The system only explains information already present.

It never:

* Diagnoses diseases
* Prescribes medication
* Changes dosages
* Makes legal or financial decisions

---

# Human-in-the-Loop

HBP100-USAII does not replace professionals.

Final medical, legal, and financial decisions remain with qualified humans.

The system acts as an explanation tool, not a decision-maker.

---

# Built With

## Frontend

* React
* Vite
* Tailwind CSS

## Backend

* FastAPI

## AI

* Groq API
* Llama-3.3-70B

## Privacy Engine

* HBP100 v2
* Regex extractors
* TF-IDF vectorizer
* LightGBM classifier
* Metadata vault

---

# Core Package

**HBP100 v2**

https://github.com/Erox-02/humming-bird-v2

---

# Repository

https://github.com/Erox-02/hbp100-usaii

---

# License

MIT License

---

# Author

**Dipanjan Dutta**

---

Built for the **USAII Global AI Hackathon 2026**.

*"Sensitive information should never reach external AI systems unnecessarily."*
