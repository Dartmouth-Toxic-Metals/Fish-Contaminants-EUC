import pandas as pd
import models as m
from sqlalchemy.orm import sessionmaker
import config


Session = sessionmaker(bind=m.engine)
session = Session()

path = config.PATH_TO_INSTITUTIONS

dataframe = pd.read_csv(path)

for idx, row in dataframe.iterrows():

    new_institution = m.Institution(name=row['name'])
    session.add(new_institution)
    session.commit()
