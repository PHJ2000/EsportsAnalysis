from pynput.keyboard import Key, Listener
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class main:#94,59,79,33,7,10,272,56,21,6,9,0,0,2,27
    def __init__(self):
        self.key_frequency = { "q": 94,
                               "w": 59,
                               "e": 79,
                               "r": 33,
                               "d": 7,
                               "f": 10,
                               "a": 272,
                               "1": 56,
                               "2": 21,
                               "3": 6,
                               "4": 9,
                               "5": 0,
                               "6": 0,
                               "7": 2,
                               "s": 27,
                               }
        self.flag = 1

    def on_release(self, key):
        data = str(key)[1:-1].lower()
        if key == Key.enter:
            self.flag *= -1
        if self.flag == 1 and data in self.key_frequency.keys() :
            self.key_frequency[data] += 1
        
        print(f'{key} release')
        if key == Key.f4:
            return False

    def convert_df(self):
        return pd.DataFrame(self.key_frequency, index=[0])
    
 
    def visualize(self):
        key_df = self.convert_df()
        x = np.arange(len(key_df.columns))
        plt.figure(figsize=(6,6))
        plt.title('Keyboard Frequency')
        plt.grid(axis='y')
        plt.xticks(x, key_df.columns)
        plt.bar(x, key_df.iloc[-1])
        plt.show()

    def run(self):
        print('Recording start ..\n')
        with Listener(on_release=self.on_release) as listener:
            listener.join()
       # self.save_df()
        self.visualize()

if __name__ == '__main__' :
    main().run()