import pandas as pd
import numpy as np


# Saiyam Lakhanpal
# Github- https://github.com/Saiyamlakhanpal

class topsis:
    r_no = '101917188'

    def __init__(self, input_file, weight_str, impact_str, out_file):
        self.input_file = input_file
        self.weight_str = weight_str
        self.impact_str = impact_str
        self.out_file = out_file

    def calculate(self):
        weights = self.weight_str.split(',')
        try:
            weights = [int(i) for i in weights]
        except ValueError:
            print("Weights should only be numbers\n")
            exit()

        impacts = self.impact_str.split(',')
        for i in impacts:
            if i != '+' and i != '-':
                print("impacts should be either + or -")
                exit()

        try:
            read_file = pd.read_excel(self.input_file)
            read_file.to_csv(r_no + '-data.csv', index=None, header=True)
            df = pd.read_csv(r_no + "-data.csv")
        except FileNotFoundError:
            print("File not found")
            exit()

        if len(df.columns) < 3:
            print("Input file must contain three or more columns.\n")
            exit()

        check = {len(df.columns)-1, len(weights), len(impacts)}
        if len(check) != 1:
            print(
                "Number of weights, number of impacts and number of indicators must be same.\n")
            exit()

        for col in df.iloc[:, 1:]:
            for i in df[col]:
                if isinstance(i, float) == False:
                    print("columns must contain numeric values only\n")
                    exit()

        arr = np.array(df.iloc[:, 1:])

        root_sum_of_squares = np.sqrt(np.sum(arr**2, axis=0))

        arr = np.divide(arr, root_sum_of_squares)
        arr = arr*weights

        ideals = np.zeros((arr.shape[1], 2))
        for i in range(len(impacts)):
            l = np.zeros(2)
            if impacts[i] == '+':
                l[0] = max(arr[:, i])
                l[1] = min(arr[:, i])
            elif impacts[i] == '-':
                l[0] = min(arr[:, i])
                l[1] = max(arr[:, i])
            ideals[i, 0] = l[0]
            ideals[i, 1] = l[1]
        ideals = ideals.T

        distances = np.zeros((arr.shape[0], 2))

        for i in range(arr.shape[0]):
            best_dist = np.linalg.norm(arr[i, :] - ideals[0, :])
            worst_dist = np.linalg.norm(arr[i, :] - ideals[1, :])
            distances[i, 0] = best_dist
            distances[i, 1] = worst_dist

        performance_score = np.divide(
            distances[:, 1], np.add(distances[:, 0], distances[:, 1]))

        rank = np.zeros(arr.shape[0])

        temp = list(performance_score)
        count = 1
        for i in range(len(performance_score)):
            ind = np.argmax(temp)
            rank[ind] = count
            count += 1
            temp[ind] = -99

        df_out = df
        df_out['Topsis Score'] = performance_score
        df_out['Rank'] = rank
        df_out.to_csv(self.out_file, index=None)
        print("Completed succesfully! Check " +
              self.out_file+" for the output\n")
