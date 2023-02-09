#%%

import sqlalchemy as sa

engine = sa.create_engine("sqlite:///paymepal.db")


with engine.connect() as connection:
    query = "SELECT * FROM users"
    result = connection.execute(query)
    for user in result:
        print(result[2])
    


# %%
