# Last updated: 13/07/2026, 17:15:34
1import pandas as pd
2def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
3    return pd.DataFrame(data = student_data, columns = ['student_id','age'])
4