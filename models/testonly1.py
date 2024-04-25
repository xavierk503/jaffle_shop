import pandas
def model(dbt, session):
    df = dbt.ref("testonly3")
    print('testonly')
    return df