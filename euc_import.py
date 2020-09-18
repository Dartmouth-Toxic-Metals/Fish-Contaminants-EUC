import chen_import
import smithsonian_import
# import ncca_import
# import nrsa_import
# import bu_import
import pandas as pd
import models as m
from sqlalchemy.orm import sessionmaker
import config


def import_institutions():
    Session = sessionmaker(bind=m.engine)
    session = Session()

    path = config.PATH_TO_INSTITUTIONS

    dataframe = pd.read_csv(path)

    for idx, row in dataframe.iterrows():
        new_institution = m.Institution(name=row['name'])
        session.add(new_institution)
        session.commit()


def import_compounds():
    Session = sessionmaker(bind=m.engine)
    session = Session()

    path = config.PATH_TO_COMPOUNDS

    dataframe = pd.read_csv(path)

    for idx, row in dataframe.iterrows():
        new_compound = m.Compound(
            name=row['name'],
            column_metadata={'keys': ['name'], 'tags': [None]}
        )
        session.add(new_compound)
        session.commit()


def initialize_tables():
    m.Base.metadata.drop_all(m.engine)
    m.Base.metadata.create_all(m.engine)


def import_all_locations():
    chen_import.extract_locations()
    chen_import.import_locations()
    smithsonian_import.extract_locations()
    smithsonian_import.import_locations()
    # ncca_import.extract_locations()
    # ncca_import.import_locations()
    # nrsa_import.extract_locations()
    # nrsa_import.import_locations()
    # bu_import.extract_locations()
    # bu_import.import_locations()


def main():
    initialize_tables()
    import_institutions()
    import_compounds()
    import_all_locations()
    chen_import.import_samples()


if __name__ == "__main__":
    main()
