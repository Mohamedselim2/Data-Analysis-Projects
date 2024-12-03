import tkinter as tk
from tkinter import scrolledtext
import re
from Compiler.tokenizer import Tokenizer
from Compiler.parser import Parser
from Compiler.code_generator import CodeGenerator
from Compiler.virtual_machine import VirtualMachine

def main():
    # Colors and fonts based on the design
    BG_COLOR = "#1E292D"
    TITLE_COLOR = "#27E29E"
    INPUT_BG_COLOR = "#FDFBED"
    FONT = ("Courier", 12)


    # Syntax Highlighter Class
    class SyntaxHighlighter:
        def __init__(self, text_widget):
            self.text_widget = text_widget

            # Configure tags for syntax highlighting
            self.text_widget.tag_configure("keyword", foreground="#FF79C6", font=("Courier", 12, "bold"))  # Bold keywords
            self.text_widget.tag_configure("number", foreground="#BD93F9", font=("Courier", 12))           # Regular numbers
            self.text_widget.tag_configure("operator", foreground="#F20D50", font=("Courier", 12))         # Regular operators
            self.text_widget.tag_configure("variable", foreground=BG_COLOR, font=("Courier", 12, "italic")) # Italic variables

            # Define syntax patterns
            self.patterns = [
                (r'\b(if|else|int|float)\b', 'keyword'),
                (r'\b\d+\b', 'number'), 
                (r'[+\-*/=<>;{}]', 'operator'),
                (r'\b(?!if|else|int|float\b)[a-zA-Z_][a-zA-Z0-9_]*\b', 'variable')  # Variables (light blue)
            ]


        def highlight(self, event=None):
            # Remove all existing tags
            for tag in ["keyword", "number", "operator", "variable"]:
                self.text_widget.tag_remove(tag, "1.0", "end")

            # Apply highlighting
            content = self.text_widget.get("1.0", "end-1c")
            for pattern, tag in self.patterns:
                for match in re.finditer(pattern, content):
                    start = f"1.0+{match.start()}c"
                    end = f"1.0+{match.end()}c"
                    self.text_widget.tag_add(tag, start, end)


    # Function to handle compilation and execution
    def compile_and_run():
        source_code = source_code_input.get("1.0", tk.END).strip()
        if not source_code:
            result_label.config(text="Error: No source code provided.")
            return

        try:
            # Tokenization
            tokenizer = Tokenizer(source_code)
            tokens = []
            tokens_output.delete("1.0", tk.END)
            token = tokenizer.get_next_token()
            while token:
                tokens.append(token)
                tokens_output.insert(tk.END, f"{token}\n")
                token = tokenizer.get_next_token()

            # Parsing
            parser = Parser(tokens)
            ast = parser.parse()

            # Code generation
            code_gen = CodeGenerator()
            instructions = code_gen.generate(ast)

            # Display generated assembly
            assembly_output.delete("1.0", tk.END)
            for instruction in instructions:
                assembly_output.insert(tk.END, f"{instruction}\n")

            # Execution
            vm = VirtualMachine()
            output = vm.execute(instructions)

            # Display execution output
            execution_output.delete("1.0", tk.END)
            for line in output:
                execution_output.insert(tk.END, f"{line}\n")

            result_label.config(text="Compilation and execution successful!")

        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")


    # Initialize main window
    root = tk.Tk()
    root.title("Simple Compiler GUI")
    root.configure(bg=BG_COLOR)
    root.geometry("850x600")

    # Title Labels
    tk.Label(root, text="Source Code", bg=BG_COLOR, fg=TITLE_COLOR, font=("Courier", 14, "bold")).grid(row=0, column=0, padx=10, pady=5, sticky="w")
    tk.Label(root, text="Execution Output", bg=BG_COLOR, fg=TITLE_COLOR, font=("Courier", 14, "bold")).grid(row=2, column=0, padx=10, pady=5, sticky="w")
    tk.Label(root, text="Tokens", bg=BG_COLOR, fg=TITLE_COLOR, font=("Courier", 14, "bold")).grid(row=2, column=1, padx=10, pady=5, sticky="w")
    tk.Label(root, text="Generated Assembly", bg=BG_COLOR, fg=TITLE_COLOR, font=("Courier", 14, "bold")).grid(row=2, column=2, padx=10, pady=5, sticky="w")

    # Source Code Input
    source_code_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg=INPUT_BG_COLOR, font=FONT, height=10, width=80)
    source_code_input.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")

    # Add syntax highlighter
    highlighter = SyntaxHighlighter(source_code_input)
    source_code_input.bind('<KeyRelease>', highlighter.highlight)

    # Execution Output
    execution_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg=INPUT_BG_COLOR, font=FONT, height=8, width=40)
    execution_output.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")

    # Tokens Output
    tokens_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg=INPUT_BG_COLOR, font=FONT, height=8, width=20)
    tokens_output.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")

    # Generated Assembly Output
    assembly_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg=INPUT_BG_COLOR, font=FONT, height=8, width=20)
    assembly_output.grid(row=3, column=2, padx=10, pady=5, sticky="nsew")

    # Compile & Run Button
    compile_button = tk.Button(root, text="Compile & Run", command=compile_and_run, bg=TITLE_COLOR, font=("Courier", 12, "bold"), fg="black")
    compile_button.grid(row=0, column=2, padx=10, pady=5, sticky="e")

    # Result Label (for displaying error or success messages)
    result_label = tk.Label(root, text="", bg=BG_COLOR, fg=TITLE_COLOR, font=FONT)
    result_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    # Configure grid to allow resizing
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(3, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()