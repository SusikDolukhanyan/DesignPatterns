
class Command:
    def execute(self):
        pass

    def undo(self):
        pass

class TextEditor:
    def __init__(self):
        self.text = ""

    def add_text(self, new_text):
        self.text += new_text

    def remove_text(self, length):
        self.text = self.text[:-length]

    def show_text(self):
        return self.text

class AddTextCommand(Command):
    def __init__(self, editor, text):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.add_text(self.text)

    def undo(self):
        self.editor.remove_text(len(self.text))


class RemoveTextCommand(Command):
    def __init__(self, editor, length):
        self.editor = editor
        self.length = length

    def execute(self):
        self.editor.remove_text(self.length)

    def undo(self):
        pass

class CommandManager:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo_command(self):
        if self.history:
            command = self.history.pop()
            command.undo()

if __name__ == "__main__":
    editor = TextEditor()

    manager = CommandManager()

    
    add_hello = AddTextCommand(editor, "Hello, ")
    add_world = AddTextCommand(editor, "World!")
    remove_text = RemoveTextCommand(editor, 6)  

    
    manager.execute_command(add_hello)
    print(f"Text after adding 'Hello, ': {editor.show_text()}")

    manager.execute_command(add_world)
    print(f"Text after adding 'World!': {editor.show_text()}")

    
    manager.undo_command()
    print(f"Text after undoing 'World!': {editor.show_text()}")

    
    manager.execute_command(remove_text)
    print(f"Text after removing 6 characters: {editor.show_text()}")
