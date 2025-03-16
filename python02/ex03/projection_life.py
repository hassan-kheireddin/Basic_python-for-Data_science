import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    loads the files income_per_person_gdppercapita_ppp_inflation_adjusted.csv
    and life_expectancy_years.csv, and displays the projection of
    life expectancyin relation to the gross national product of the year 1900
    for each country.
    """
    try:
        inflationData = \
            load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        lifeExpectancy = load("life_expectancy_years.csv")
        if lifeExpectancy.empty or inflationData.empty:
            raise AssertionError("File is Empty")
    except (Exception, AssertionError) as error:
        print(f"{error.__class__.__name__}: File DataBase not present")
        exit()

    inflationData = inflationData[['country', '1900']]
    inflationData = inflationData.rename(columns={'1900': 'inflation'})
    lifeExpectancy = lifeExpectancy[['country', '1900']]
    lifeExpectancy = lifeExpectancy.rename(columns={'1900': 'lifeExpectancy'})

    data = pd.merge(inflationData, lifeExpectancy, on='country', how='inner')
    data.dropna(subset=['inflation', 'lifeExpectancy'], inplace=True)

    plt.scatter(data['inflation'], data['lifeExpectancy'])
    plt.title('1900')
    plt.xlabel('Gross Domestic Product')
    plt.ylabel('Life Expectancy')
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.show()


if __name__ == "__main__":
    main()
