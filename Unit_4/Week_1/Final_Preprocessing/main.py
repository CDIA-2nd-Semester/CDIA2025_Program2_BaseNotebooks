from data.load import load_data
from data.preprocessing import preprocess_data


def main():
    df=load_data('csv/WineQT.csv')
    preprocessed_df=preprocess_data(df)
    

if __name__ == "__main__":
    main()
    


