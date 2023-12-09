from .models import loggy,collection
from django.apps import apps
import pandas as pd
import pandas as pd
import plotly.express as px
from PIL import Image
import io

def getTableData(tablename:str):
    model_table=apps.get_model('dbapp',tablename)
    if model_table:
        queryset=model_table.objects.all()
        df=pd.DataFrame(list(queryset.values()))
        return df
    loggy.error("error in getting table data")
    return None

def analyze(tableData:pd.DataFrame):
    fig=px.scatter(tableData,x='os',y='rating')
    
    byteImage=fig.to_image(format="png")
    image=Image.open(io.BytesIO(byteImage))
    image.save('plot1.png')
    
    with open('plot1.png', 'rb') as image_file:
        binary_data = image_file.read()

    col=collection
    col.insert_one({"image_data":binary_data})
    