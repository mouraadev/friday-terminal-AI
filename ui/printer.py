import time
from . import banner
from . import gradient

def call_banner():
    print("SYSTEM ONLINE", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(" - F.R.I.D.A.Y. READY FOR COMMAND INPUT.\n")

    print()
    for line in banner.friday_ascii():
        print(gradient.gradient_line(line, banner.start_color(), banner.end_color()))
        time.sleep(0.05)

    print(gradient.rgb(100, 255, 255) + "─" * 70)
    print(gradient.rgb(200, 255, 200) + "        SYSTEM ONLINE – F.R.I.D.A.Y. READY FOR COMMAND INPUT.   ")
    print(gradient.rgb(255, 200, 100) + "        Type 'exit' or 'quit' to terminate session.   ")
    print(gradient.rgb(100, 255, 255) + "─" * 70 + "\033[0m")
