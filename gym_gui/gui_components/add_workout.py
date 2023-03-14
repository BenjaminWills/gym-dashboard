from tkinter import Toplevel, Tk, Canvas, StringVar, OptionMenu

from typing import Dict, List


class Add_workout(Toplevel):
    def __init__(self, master_root: Tk):
        self.root = master_root

        super().__init__(master_root)
        self.title("Add a workout")

        # Canvas
        canvas = Canvas(self, width=300, height=450)
        canvas.grid(columnspan=3, rowspan=6)

        # Make dropdown box
        splits = self.get_splits()
        split_menu = StringVar()
        split_menu.set("Select a split")

        menu = OptionMenu(self, split_menu, *splits)
        menu.grid(row=0, column=1)

    def get_splits(self):
        return ["full body", "push pull legs"]

    def get_full_body_split(self) -> Dict[int, List[str]]:
        return {
            1: [
                "back squat",
                "db press",
                "leg curl",
                "pulldown",
                "bicep curl",
                "leg raise",
            ],
            2: [
                "bench press",
                "cable flye",
                "rdl",
                "db row",
                "arnold press",
                "pressdown",
                "shrug",
            ],
            3: [
                "pullup",
                "db row",
                "leg press",
                "calf raise",
                "upright row",
                "hammer curl",
                "push up",
            ],
            4: ["run"],
            5: [
                "deadlift",
                "dip",
                "hip thrust",
                "leg extension",
                "pullover",
                "lateral raise",
                "skullcrusher",
            ],
            6: [
                "overhead press",
                "lateral raise",
                "cable row",
                "hip abduction",
                "incline curl",
                "crunch",
                "calf raise",
            ],
            7: ["run"],
            8: ["rest"],
        }
