class TextEditor:
    # Implements undo/redo using two stacks.
    
    def __init__(self):
        """
        Initializes the text list and the undo/redo stacks.
        """
        # self.text will hold the current document
        self.text = [] 
        # undoStack stores operations to be undone
        self.undoStack = []
        # redoStack stores operations to be redone
        self.redoStack = []

    def type(self, char):
        """
        Types a character into the editor.
        This adds the character to the text and pushes the
        operation (the char) onto the undo stack.
        A new 'type' operation clears the redo stack.
        """
        self.text.append(char)
        self.undoStack.append(char)
        # Any new typing clears the redo history
        self.redoStack.clear()
        print(f"Typed: '{char}'")
        self.show()

    def undo(self):
        """
        Undoes the last 'type' operation.
        It pops from the undo stack, removes the char from
        the text, and pushes the char to the redo stack.
        """
        if not self.undoStack:
            print("Cannot undo: Nothing to undo")
            return
            
        charToUndo = self.undoStack.pop()
        self.text.pop() # Remove the last character
        
        # Add this undone operation to the redo stack
        self.redoStack.append(charToUndo)
        print("--- Undo ---")
        self.show()

    def redo(self):
        """
        Redoes the last 'undo' operation.
        It pops from the redo stack, adds the char back to
        the text, and pushes the char back to the undo stack.
        """
        if not self.redoStack:
            print("Cannot redo: Nothing to redo")
            return
            
        charToRedo = self.redoStack.pop()
        self.text.append(charToRedo)
        
        # Add this redone operation back to the undo stack
        self.undoStack.append(charToRedo)
        print("--- Redo ---")
        self.show()

    def show(self):
        """
        Displays the current text.
        """
        print(f"Current Text: {''.join(self.text)}")

# --- Main Program Execution ---
editor = TextEditor()

editor.type('H')
editor.type('e')
editor.type('l')
editor.type('l')

print("\n--- Performing Undo ---")
editor.undo() # Undoes the last 'l'
editor.undo() # Undoes the second 'l'

print("\n--- Performing Redo ---")
editor.redo() # Redoes the second 'l'

print("\n--- Typing again ---")
editor.type('p') # This should clear the redo stack

print("\n--- Trying to Redo (should fail) ---")
editor.redo() # Fails because 'p' cleared the redo stack

print("\n--- Final state ---")
editor.show()
