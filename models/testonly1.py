import pandas
def model(dbt, session):
    df = dbt.ref("testonly3")
    return df