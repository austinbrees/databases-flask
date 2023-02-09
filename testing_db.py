#%%

import sqlalchemy as sa

engine = sa.create_engine("sqlite:///paymepal.db")


with engine.connect() as connection:
    query = "SELECT * FROM transactions;"
    
    result = connection.execute(query)
    
    for row in result:
        print(row)



# %%
