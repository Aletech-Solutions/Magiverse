from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit import print_formatted_text, HTML

def print_attributes(obj):
    for key, value in obj.__dict__.items():
        print_formatted_text(HTML(f'<ansicyan>{key.capitalize()}: </ansicyan>{value}<br/>'))
    print_formatted_text(HTML(f'<br/> <br/> <br/>'))
    