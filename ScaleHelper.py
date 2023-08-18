#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 09:40:13 2023

@author: dibasaliani
"""
import matplotlib.pyplot as plt

class ScaleHelper:
    def __init__(self):
        self.scales = {
            'c major': ('C', []),
            'g major': ('G', ['F']),
            'd major': ('D', ['F#', 'C#']),
            'a major': ('A', ['F#', 'C#', 'G#']),
            'e major': ('E', ['F#', 'C#', 'G#', 'D#']),
            'b major': ('B', ['F#', 'C#', 'G#', 'D#', 'A#']),
            'f# major': ('F#', ['F#', 'C#', 'G#', 'D#', 'A#', 'E#']),
            'c# major': ('C#', ['F#', 'C#', 'G#', 'D#', 'A#', 'E#', 'B#']),
            'a minor': ('A', []),
            'e minor': ('E', ['D#']),
            'b minor': ('B', ['D#', 'F#']),
            'f# minor': ('F#', ['D#', 'F#', 'G#']),
            'c# minor': ('C#', ['D#', 'F#', 'G#', 'C#']),
        }

    def analyze_scale(self, scale_name):
        scale_name_lower = scale_name.lower()
        if scale_name_lower in self.scales:
            root_note, accidentals = self.scales[scale_name_lower]
            accidentals_formatted = ', '.join(accidentals) if accidentals else "None"
            return f"Scale: {scale_name_lower.capitalize()}\nRoot Note: {root_note}\nAccidentals: {accidentals_formatted}"
        else:
            return "Scale not recognized. Please enter a valid scale name."

    def visualize_scale(self, scale_name):
        scale_name_lower = scale_name.lower()
        if scale_name_lower in self.scales:
            root_note, accidentals = self.scales[scale_name_lower]

            keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
            keyboard = ['black' if note.endswith('#') else 'white' for note in keys]
            scale_keyboard = [keyboard[keys.index(note)] for note in [root_note] + accidentals if note in keys]

            plt.figure(figsize=(10, 2))
            plt.bar(keys, [1] * len(keys), color=scale_keyboard)
            plt.xlabel('Notes')
            plt.ylabel('Presence')
            plt.title(f'{scale_name_lower.capitalize()} Scale Visualization')
            plt.show()
        else:
            print("Scale not recognized. Please enter a valid scale name.")

def main():
    scale_helper = ScaleHelper()

    while True:
        action = input("Enter 'analyze', 'visualize', or 'exit': ").strip().lower()

        if action == 'exit':
            print("Goodbye!")
            break
        elif action == 'visualize':
            scale_input = input("Enter a scale name to visualize: ").strip()
            scale_helper.visualize_scale(scale_input)
        elif action == 'analyze':
            scale_input = input("Enter a scale name to analyze: ").strip()
            result = scale_helper.analyze_scale(scale_input)
            print(result)
            print()
        else:
            print("Invalid action. Please enter 'analyze', 'visualize', or 'exit'.")

if __name__ == "__main__":
    main()



