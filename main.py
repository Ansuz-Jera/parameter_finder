from matplotlib import pyplot as plt
from filter import*
from scipy.optimize import curve_fit


def exponential(x, a, b, c):
    return a * np.exp(-b * x) + c


if __name__ == '__main__':
    file_path = 'C:\\Users\\Jazur\\Downloads\\EJ_PRES.csv'
    df_data = pd.read_csv(file_path, header=None, usecols=[1, 3, 4], skiprows=[0]).dropna()
    df_data.columns = [*{(i + 1) for i in range(len(df_data.columns))}]
    
    # Find the difference in the data to find the increases or decreases
    diff_point = np.diff(np.diff(df_data[2]))
    inflection = np.where(np.abs(diff_point) > 0.005)

    dff = inflection[0]

    df_1 = df_data[2].truncate(before=dff[0], after=dff[1]).values
    df_2 = df_data[2].truncate(before=dff[1], after=dff[2]).values
    df_3 = df_data[2].truncate(before=dff[2], after=dff[3]).values
    df_4 = df_data[2].truncate(before=dff[3], after=len(df_data)).values

    df_total = [df_1, df_2, df_3, df_4]

    for func, data in enumerate(df_total):
        x_data = np.linspace(0, 4, data.size)
        y_data = data
        plt.plot(x_data, y_data, label='data from function %d' % (func + 1))

        # Fit for the parameters a, b, c of the function func:
        popt, pcov = curve_fit(exponential, x_data, y_data)
        plt.plot(x_data, exponential(x_data, *popt), 'b--', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
        print()

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
