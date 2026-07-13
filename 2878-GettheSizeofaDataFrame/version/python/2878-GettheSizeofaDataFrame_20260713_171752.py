# Last updated: 13/07/2026, 17:17:52
1import pandas as pd
2
3def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
4    return(employees[:3])
5    