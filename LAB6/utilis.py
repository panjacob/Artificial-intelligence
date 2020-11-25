import matplotlib.pyplot as plt


def avg_plot(results, title):
    sum = []
    for result in results:
        for i, el in enumerate(result):
            if len(sum) > i:
                sum[i] += el
            else:
                sum.append(el)
    plt.plot(sum)
    plt.title(title)
    plt.show()
