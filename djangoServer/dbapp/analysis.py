from .models import loggy
from django.apps import apps
import pandas as pd

def getTableData(tablename:str):
    model_table=apps.get_model('dbapp',tablename)
    if model_table:
        queryset=model_table.objects.all()
        df=pd.DataFrame(list(queryset.values()))
        return df
    loggy.error("error in getting table data")
    return None

def analyze(tableData:pd.DataFrame):
    df_rowCount,df_colCount=tableData.shape
    loggy.debug(df_colCount,df_rowCount)