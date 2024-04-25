import pandas
def model(dbt, session):
    df = dbt.ref("testonly1")
    return df