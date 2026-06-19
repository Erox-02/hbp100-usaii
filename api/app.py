import os
import re
from typing import Dict, Any, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from hbp100 import mask, restore, metadata_vault
from prompt import SYSTEM_PROMPT

app = FastAPI(
    title="hbp100 Privacy Firewall API",
    description="Ultra-light privacy firewall for LLM prompts",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://hbp-100.vercel.app",
        "https://your-frontend.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
groq_client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
) if GROQ_API_KEY else None

class ChatRequest(BaseModel):
    prompt: str
    use_real_llm: bool = False
    use_privacy: bool = True

class ChatResponse(BaseModel):
    original_prompt: str
    masked_prompt: str
    metadata: Dict[str, Any]
    llm_response_masked: Optional[str] = None
    llm_response_restored: Optional[str] = None
    has_pii: bool

def call_llm(masked_prompt: str, metadata: Dict[str, Any]) -> str:
    if not GROQ_API_KEY or not groq_client:
        raise HTTPException(status_code=500, detail="LLM not configured. Add GROQ_API_KEY to environment.")
    
    if metadata:
        allowed_text = ", ".join(metadata.keys())
    else:
        allowed_text = "No placeholders are allowed in the response."
    
    user_message = f"""Allowed placeholders you can use in your response:
{allowed_text}

User message:
{masked_prompt}"""
    
    try:
        completion = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            temperature=0,
            max_tokens=1000,
        )
        return completion.choices[0].message.content or ""
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM error: {str(e)}")

def validate_placeholders(response: str, metadata: Dict[str, Any]) -> str:
    pattern = r'\[[A-Z_]+_\d+\]'
    placeholders = re.findall(pattern, response)
    for ph in placeholders:
        if ph not in metadata:
            return f"[ERROR: Hallucinated placeholder {ph} detected.]"
    return response

@app.post("/", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        original_prompt = request.prompt
        metadata_vault.clear()

        if request.use_privacy:
            masked_prompt = mask(request.prompt)
        else:
            masked_prompt = request.prompt

        metadata = metadata_vault.show()

        if request.use_real_llm:
            llm_response_masked = call_llm(masked_prompt, metadata)
            llm_response_masked = validate_placeholders(llm_response_masked, metadata)
            
            if request.use_privacy:
                llm_response_restored = restore(llm_response_masked)
            else:
                llm_response_restored = llm_response_masked
        else:
            llm_response_masked = f"MOCK MODE:\n\n{masked_prompt}"

            if request.use_privacy:
                llm_response_restored = restore(llm_response_masked)
            else:
                llm_response_restored = llm_response_masked

        return ChatResponse(
            original_prompt=original_prompt,
            masked_prompt=masked_prompt,
            metadata=metadata,
            llm_response_masked=llm_response_masked,
            llm_response_restored=llm_response_restored,
            has_pii=len(metadata) > 0
        )
    
    except HTTPException:
        raise
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "hbp100 Privacy Firewall",
        "version": "2.0.0"
    }

@app.get("/warmup")
async def warmup():
    return {"status": "warm"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
