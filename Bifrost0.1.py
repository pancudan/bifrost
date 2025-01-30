import tkinter as tk
from tkinter import ttk

class BasicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bifrost 0.1")
        self.root.geometry("800x600")
        
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header
        ttk.Label(main_frame, 
                text="Bifrost - Text Extraction", 
                font=('Arial', 16)).pack(pady=10)
        
        # Dummy buttons
        ttk.Button(main_frame, 
                 text="Upload Image (Coming Soon)").pack(pady=5)
        
        ttk.Button(main_frame,
                 text="Capture Screenshot (Coming Soon)").pack(pady=5)
        
        # Status bar
        self.status = ttk.Label(main_frame, text="Ready")
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

if __name__ == "__main__":
    root = tk.Tk()
    app = BasicApp(root)
    root.mainloop()