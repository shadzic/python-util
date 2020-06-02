import scipy.stats as stats

def TwoSampleTtest(a, b, pvalue=0.05):
    '''
    Compare equality of means for two vectors
    Input:
    a, b: numeric vectors for which means are compared
    pvalues: significance level
    '''
    res = stats.ttest_ind(a, b)
    print('T-statistic is {}'.format(res[0]))
    print('P-value is {}'.format(res[1]))
    if res[1] < pvalue:
        conclusion = 'Means are statistically different'
        print(conclusion)
    else:
        conclusion = 'Means are not statistically different'
        print(conclusion)
        
    return(res[0], res[1], conclusion, a.mean(), b.mean())
    
    
def TestMeans(df, testvars, outcome):
    '''
    Compare equality of means for list of variables.
    
    Input: 
    df: dataset with tested variables and groups
    testvars: numerical variables to compare,
    outcome: variables that defines 2 groups
    '''
    results = []
    for var in testvars:
        print(var)
        res = TwoSampleTtest(df[df[outcome]][var], df[~df[outcome]][var], pvalue=0.05/len(testvars))
        # /len(testvars) is the Bonferroni correction
        
        print(res)
        print('='*80)
        results.append(res)
    
    df_results = pd.DataFrame(results, columns=['T-stat', 'p-value', 'conclusion', 'mean_1', 'mean_0'], index=testvars)
    return(df_results)
