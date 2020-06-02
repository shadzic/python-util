# histogram
def plot_num_hist(country, feature, df):
    '''
    Normalizing my data and plotting a histogram
    '''
    df = df.copy()
    missing_nb = df[pd.isnull(df[feature])].shape[0]
    missing_percent = 100*(missing_nb/df.shape[0])

    df = df[pd.notnull(df[feature])]

    df = 100*(df.groupby([feature]).agg(['count'])['customer_id']/df.shape[0])
    my_lululu = df.reset_index(inplace=False)
    plt.figure(figsize=(20,10)) 
    plt.bar(my_lululu[feature], my_lululu['count'], edgecolor='k', color=config.colors_dict[country])
    plt.title("{1} -- {0} -- {2}% missing".format(feature, country, int(missing_percent)))
    plt.ylabel("Percent")
    plt.xlabel("{0}".format(feature));
    plt.ylim(0,110)
    plt.yticks(np.arange(0, 110, 10))
    plt.xticks(rotation=90)
    plt.xticks(np.arange(min(my_lululu[feature]), max(my_lululu[feature])+1, 1));
