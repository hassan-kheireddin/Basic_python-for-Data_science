import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def conv_pop(population_str):
    """
    Converts population from string with 'B' (billions), 'M' (millions),
    or 'k' (thousands) to numeric value.If the value is empty or missing,
    it replaces it with a default scientific notation value.
    """
    if isinstance(population_str, str) and population_str.strip():
        if 'B' in population_str:
            return float(population_str.replace('B', '').strip()) * 1e9
        if 'M' in population_str:
            return float(population_str.replace('M', '').strip()) * 1e6
        if 'k' in population_str:
            return float(population_str.replace('k', '').strip()) * 1e3
        return float(population_str)


def main():
    """
    Load population data, filter for Lebanon and France,
    and display a line graph.
    """
    try:
        dataset = load("population_total.csv")
        if dataset.empty:
            raise AssertionError("File is Empty")
    except (Exception, AssertionError) as error:
        print(f"Error: {error}")
        return

    first_country = 'Belgium'
    second_country = 'France'
    data_first = dataset[dataset['country'] == first_country]
    data_second = dataset[dataset['country'] == second_country]
    years = data_first.columns[1:-50].astype(int)

    pop_first = [conv_pop(val) for val in data_first.values[0][1:-50]]
    pop_second = [conv_pop(val) for val in data_second.values[0][1:-50]]

    df = pd.DataFrame({
        first_country: pop_first,
        second_country: pop_second
    }, index=years)

    df.plot(title="Population Projections", color=['blue', 'green'])
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.yticks(ticks=[20e6, 40e6, 60e6], labels=['20M', '40M', '60M'])
    plt.xticks(years[::40])
    plt.legend(fontsize=8, loc="lower right")
    plt.show()


if __name__ == "__main__":
    main()
