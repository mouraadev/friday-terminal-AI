from config.prompts import *

def get_prompt_for_mode(mode):
    if mode == "stark":
        return stark_prompt
    
    elif mode == "teacher":
        return teacher_prompt
    
    else:
        return system_prompt
    
