import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    It extract the data for specific country and plot it on graph
    """
    try:
        ds = load("life_expectancy_years.csv")
        if ds is None or ds.empty:
            raise AssertionError("File is Empty")
    except (Exception, AssertionError) as error:
        print(f"Error: {error}")
        return
    country_name = "France"
    ds_country = ds[ds['country'] == country_name]
    if ds_country.empty:
        print(f"No data available for {country_name}")
        return
    print(ds_country)
    years = ds_country.columns[1:]
    expectancy_years = ds_country.values[0][1:]

    plt.plot(years, expectancy_years)
    plt.title(f'{country_name} Life Expectancy Projections')
    plt.xlabel('Year')
    plt.xticks(years[::40])
    plt.ylabel('Life expectancy')
    plt.yticks(range(30, 100, 10))
    plt.show()


if __name__ == "__main__":
    main()
