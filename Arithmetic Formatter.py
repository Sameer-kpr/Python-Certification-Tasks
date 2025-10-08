def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    
    first_line = []
    second_line = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()

       
        if len(parts) != 3:
            return "Error: Invalid problem format."

        first, operator, second = parts

       
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

      
        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."

        
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        
        width = max(len(first), len(second)) + 2

        
        first_line.append(first.rjust(width))
        second_line.append(operator + second.rjust(width - 1))
        dashes.append("-" * width)

        
        if show_answers:
            if operator == "+":
                result = str(int(first) + int(second))
            else:
                result = str(int(first) - int(second))
            results.append(result.rjust(width))

  
    arranged = (
        "    ".join(first_line)
        + "\n"
        + "    ".join(second_line)
        + "\n"
        + "    ".join(dashes)
    )

   
    if show_answers:
        arranged += "\n" + "    ".join(results)

    return arranged
