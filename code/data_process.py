
import os
import time
import pandas as pd


def data_cleaning(input_folder, output_folder):
    idex = 0
    for input_csv in os.listdir(input_folder):
        if idex == 1:
            break
        input = input_folder+input_csv
        df = pd.read_csv(input, comment='#', delim_whitespace=True)

        df_new_rs = df.loc[df["Uploaded_variation"].astype(str).str.contains("rs")]
        df_new = df_new_rs.loc[df["CDS_position"] == '-']
        df_new = df_new.loc[df["Protein_position"] == '-']
        # print (df_new)
        file_o = output_folder + input_csv
        df_new.to_csv(file_o, sep='\t', encoding='utf-8', index=False)

        # idex=idex +1


if __name__=="__main__":
    input_folder = '../output/'
    output_folder = '../final_output/'
    start = time.time()

    data_cleaning(input_folder,output_folder)

    end = time.time()
    print'time elapsed :' + str(end - start)



