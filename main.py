import tkinter as tk
from tkinter import ttk

class FeatureHighlightSection:
    def __init__(self, root):
        self.root = root
        self.root.title("Feature Highlight Section")

        # Frame uchun yaratish
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Header uchun yaratish
        self.header = tk.Label(self.frame, text="Feature Highlights", font=("Arial", 18, "bold"))
        self.header.pack(pady=10)

        # Iconlar uchun yaratish
        self.icons = [
            {"icon": "fa fa-star", "text": "Feature 1"},
            {"icon": "fa fa-heart", "text": "Feature 2"},
            {"icon": "fa fa-lock", "text": "Feature 3"},
            {"icon": "fa fa-bell", "text": "Feature 4"},
            {"icon": "fa fa-cog", "text": "Feature 5"},
        ]

        # Iconlar uchun loop
        for icon in self.icons:
            # Frame uchun yaratish
            icon_frame = tk.Frame(self.frame)
            icon_frame.pack(pady=5)

            # Icon uchun yaratish
            icon_label = ttk.Label(icon_frame, text=f"&#xf0{icon['icon'].split(' ')[1]}", font=("Arial", 24))
            icon_label.pack(side=tk.LEFT, padx=5)

            # Text uchun yaratish
            text_label = ttk.Label(icon_frame, text=icon['text'])
            text_label.pack(side=tk.LEFT, padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = FeatureHighlightSection(root)
    root.mainloop()
