import pandas as pd

data = pd.read_excel(r'demo.xlsx', sheet_name='test', header=1)
print("列数：", data.shape[1])
print("行数：", data.shape[0])

template = """
    {{
        123456{value}, {first},
        dafdadfa,
    }},  """

res = ""
for row in range(data.shape[0]):
    res = res + template.format(first=data['索引号'][row], value=data['三级模块'][row])

s = """
char a[] = {{
    {res}
}};
"""

print(s.format(res=res))