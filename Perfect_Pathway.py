import tkinter as tk
from tkinter import messagebox, ttk
import networkx as nx
import random
import matplotlib.pyplot as plt
from typing import List, Dict, Optional, Tuple




NODE_TYPES = {
    "Building":["A Building", "B Building", "E Building", "F Building", "I Building", "J Building"],
    "Junction": ["C Junction", "G Junction", "K Junction"],
    "Enemy camp":["D Enemy Camp","H Enemy Camp"],
    "Home": ["Home Node"]

}

ROLES = [ "Army", "Volunteer", "Rescuer"]
WINDOW_TITLE = "Perfect Pathway"
WINDOW_SIZE = "800*600"
FONT_FAMILY ="Helvetica"
TITLE_FONT = (FONT_FAMILY, 16)
NORMAL_FONT = (FONT_FAMILY, 12)

MIN_CONNECTIONS = 2
MAX_CONNECTIONS = 3
MIN_COST = 1
MAX_COST = 10

class PerfectPathway:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)
        self.root.geometry(WINDOW_SIZE)

        self.G:Optional[nx.graph] = None
        self.home_node = "Home Node"
        self.destination_node: Optional[str] = None
        self.selected_role: Optional[str] = None

        self.setup_ui()

        
    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        welcome_label = ttk.Label(main_frame, text="chose a role", padding="10")
        welcome_label.pack(pady=10)

        role_frame = ttk.LabelFrame(main_frame, text="chose a Role", padding="10")
        role_frame.pack(fill=tk.X, pady=10)
        
        
        for role in ROLES:
            role_button = ttk.Button(role_frame, text=role,
                                     command=lambda r=role: self.choose_role(r))
            role_button.pack(side=tk.LEFT, padx=5)

            self.role_label = ttk.Label(main_frame,  text="Role selected: None ",font= NORMAL_FONT )


    def choose_role(self, role: str):
        self.selected_role = role
        self.role_label.config(text=f"Role Selected: {role} ")
        self.initialize_army_graph()
