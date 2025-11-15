def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def gradient_line(text, start_color, end_color):
    result = ""
    for i, char in enumerate(text):
        ratio = i / max(len(text) - 1, 1)
        r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
        result += rgb(r, g, b) + char
    
    return result + "\033[0m"