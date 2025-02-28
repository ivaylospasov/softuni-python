import pandas as pd

# %%
# Create a dictionary with sample data
data = {
    'Column1': range(1, 11),
    'Column2': range(11, 21),
    'Column3': range(21, 31),
    'Column4': range(31, 41),
    'Column5': range(41, 51)
}

# %%
# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# %%
# Display the DataFrame
print(df)