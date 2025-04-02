import pandas as pd

class Transformer:
    def __init__(self, data):
        self.data = data

    def create_dataframe(self):
        # Convert the JSON data to a pandas DataFrame
        return pd.DataFrame(self.data)

    def group_data(self, df, group_by_columns, agg_functions=None):
        """
        Group DataFrame by specified columns and apply aggregation functions
        Args:
            df: pandas DataFrame
            group_by_columns: list of columns to group by
            agg_functions: dict of column:function pairs for aggregation
        """
        if agg_functions is None:
            # Default to counting records if no aggregation specified
            return df.groupby(group_by_columns).size().reset_index(name='count')
        
        return df.groupby(group_by_columns).agg(agg_functions).reset_index()

if __name__ == "__main__":
    pass