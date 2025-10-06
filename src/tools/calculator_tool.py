from langchain_core.tools import tool

@tool
def engineering_calculations(expression: str) -> str:
    """Perform engineering calculations using the ship's computer core.
    
    Use this tool when the crew needs:
    - Mathematical operations (addition, subtraction, multiplication, division)
    - Scientific calculations
    - Unit conversions
    - Any numeric computations
    
    Args:
        expression: A mathematical expression to evaluate (e.g., "2 + 2", "15 * 7", "100 / 4")
        
    Returns:
        The calculated result
        
    Examples:
        - "2 + 2" returns "4"
        - "15 * 7" returns "105"
        - "sqrt(16)" returns "4.0"
    """
    try:
        # Safe eval for basic math
        # In production, you'd use a proper math parser like numexpr
        import math

        # Make math functions available
        safe_dict = {
            "sqrt": math.sqrt,
            "pow": math.pow,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log,
            "abs": abs,
            "round": round,
        }

        # Evaluate the expression
        result = eval(expression, {"__builtins__": {}}, safe_dict)

        return f"Calculatiion complete: {expression} = {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero. Please check your calculations."
    except Exception as e:
         return f"Engineering system error: Unable to compute '{expression}'. Please verify the expression format."