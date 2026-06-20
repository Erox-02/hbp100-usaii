# HBP100-USAII

**AI-powered document understanding with privacy-preserving LLM workflows**

HBP100-USAII is a demonstration application built on top of **HBP100 v2**, a lightweight contextual privacy firewall.

It helps patients, caregivers, and individuals reviewing official documents understand complex information in plain language while protecting sensitive information before external AI processing.

Built for the **USAII Global AI Hackathon 2026**.

---

# Problem

People often receive discharge instructions, insurance approvals, and official documents that are difficult to understand.

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

Original information is restored after processing.

External AI models never see sensitive information in plain form.

---

# Design Philosophy

> Sensitive information should never reach external AI systems unnecessarily.

HBP100-USAII performs privacy-preserving transformations before AI inference and restores original information afterward, allowing users to benefit from AI assistance while trading almost nothing for privacy.

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

# Intended Users & Decision Context

HBP100-USAII is designed for people who need to understand complex documents and determine appropriate next actions without exposing sensitive information.

Examples include:

* A patient recently discharged from a hospital who wants to understand medications, warning symptoms, and follow-up instructions.

* An elderly parent or caregiver trying to understand discharge summaries or laboratory reports on behalf of a family member.

* An individual reviewing insurance approval or reimbursement documents and determining which forms must be submitted before a deadline.

* A caregiver helping another person understand hospital paperwork while preserving privacy.

The system helps users move from:

```text
Confusion
↓
Understanding
↓
Action
```

Medical, legal, and financial decisions remain the responsibility of qualified professionals.

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

Explain the discharge instructions in simple language and create a checklist.
```

---

## Masked Prompt

```text
Patient [NAME_1] (MRN: [MRN_1]) was admitted [HOSPITAL_1] with Type 2 Diabetes Mellitus and mild dehydration.

...

For additional questions, email [EMAIL_1].

...
```

---

## AI Response

* Explain instructions in plain language
* Generate a checklist
* Highlight warning symptoms
* Preserve placeholders

---

## Restored Output

Sensitive values are restored after processing, allowing users to benefit from AI explanations while trading almost nothing for privacy.

External AI models never see sensitive information in plain form.

---

# Screenshots

Screenshots are available in:

```text
/assets
```

---

## Application Screenshots

Home Page

![](assets/home.png)

Original Prompt

![](assets/original-prompt.png)

Masked Prompt

![](assets/masked-prompt.png)

Metadata Vault

![](assets/metadata-vault.png)

LLM Response

![](assets/llm-response.png)

Restored Response

![](assets/restored-response.png)

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
* Placeholder restoration
* Placeholder validation

---

# Performance

## Privacy Pipeline

Average request latency:

**≈388 ms**

(Model preloaded)

Benchmark:

![](assets/privacy-benchmark.png)

---

## End-to-End Pipeline

Privacy masking + LLM inference + restoration

Average response latency:

**≈2.3 seconds**

Benchmark:

![](assets/full-pipeline-benchmark.png)

---

# Platform Compatibility

Browser-based and requires no platform-specific installation.

Tested on:

* Arch Linux (KDE Plasma)
* Windows
* Linux Mint
* Android devices

Screenshots:

Arch Linux

![](assets/arch-linux.png)

Windows

![](assets/windows.png)

Linux Mint

![](assets/linux-mint.png)

Android

![](assets/phone.jpg)

---

# Responsible AI

## Risk

Users may over-rely on AI explanations.

## Mitigation

The system only explains information already present.

It never:

* Diagnoses diseases
* Prescribes medications
* Changes dosages
* Makes legal decisions
* Makes financial decisions

---

# Human-in-the-Loop

HBP100-USAII does not replace professionals.

Final medical, legal, and financial decisions remain with qualified humans.

The system acts as an explanation tool, not a decision-maker.

---

# Limitations

Current limitations include:

* Some entities may not always be detected.
* OCR support is not yet implemented.
* Entity recognition depends on extractor coverage.
* Placeholder numbering follows extraction order rather than textual order.
* Some edge cases may produce imperfect replacements.

## Root Cause

HBP100 v2 uses a hybrid architecture combining:

* Regex-based entity extractors
* TF-IDF vectorizer
* LightGBM classifier

Currently, the machine learning layer and regex extractors operate independently rather than using a fully context-aware overlapping pipeline.

The project prioritizes lightweight deployment and speed over large NER models.

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

## Tools

* Deepseek v3 
* Gpt 5.5

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

Built for the **USAII Global AI Hackathon 2026**

*"Sensitive information should never reach external AI systems unnecessarily."*
