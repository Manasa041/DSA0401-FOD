import matplotlib.pyplot as plt
def plot_monthly_sales(months, sales):
    plt.bar(months, sales)
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.title('Monthly Sales Data')
    plt.grid(True)
    plt.show()
if __name__ == "__main__": 
    months = [1, 2, 3, 4, 5, 6]
    sales = [1000, 1200, 900, 1500, 1800, 1300]

    plot_monthly_sales(months, sales)
