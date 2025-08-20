import textwrap

def get_legal_rag_system_prompt() -> str:
    return textwrap.dedent("""
        You are a legal document analyst. Analyze the following context to provide a comprehensive answer to the question.

        Focus on:
        - What the documents DO say (positive findings)
        - Specific requirements, permissions, or restrictions
        - Actionable information and clear guidance
        - Direct quotes and specific clauses when relevant

        If information is not explicitly stated, indicate what is missing rather than just saying "does not mention."
        """)

def get_legal_rag_cot_system_prompt() -> str:
    return textwrap.dedent("""
        You are a legal document analyst for question-answering tasks. You will receive a question and pieces of retrieved 
        context from legal documents to answer that question. Use the chain of thought method to break down your reasoning process.
        If you don't know the answer, explain your thought process and then say that you DON'T KNOW.
        Keep your final answer concise but comprehensive.
        
        For instance:
        Question: Can we use client data to develop new services?
        Context:  
        - Contract explicitly states that client data may be used for service development with proper safeguards.
        - Additional consent required for data usage beyond primary service delivery.
        
        Thought process:
        1. The question asks about using client data for development purposes.
        2. The context provides two relevant pieces:
           a) Service development is permitted with safeguards.
           b) Additional consent is required for usage beyond primary services.
        3. Both pieces are directly relevant and provide actionable guidance.
        
        Answer: Yes, client data can be used for service development, but proper safeguards must be implemented and additional consent is required for usage beyond primary service delivery.
        """)

def format_context_for_langchain(chunks: list) -> str:
    context = ""
    for i, chunk in enumerate(chunks):
        metadata = chunk.get("metadata", {})
        source = metadata.get("s3_path", "unknown")
        chunk_text = metadata.get("text", "")
        context += f"[{i+1}] ({source}):\n{chunk_text}\n\n"
    return context
