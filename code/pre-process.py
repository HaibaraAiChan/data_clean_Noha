import os

import time



def data_cleaning(input_folder,output_folder):
    idex = 0
    for input_csv in os.listdir(input_folder):
        if idex == 1:
            break
        input = input_folder+input_csv
        file = open(input, 'r+')
        file_o = open(output_folder + input_csv, 'w')
        handler = file.read()
        file_o.write(handler.replace("#Uploaded_variation", "Uploaded_variation"))
        file.close()
        file_o.close()

if __name__=="__main__":
    input_folder = '../results/'
    output_folder = '../output/'
    start = time.time()

    data_cleaning(input_folder, output_folder)

    end = time.time()
    print'time elapsed :' + str(end - start)
