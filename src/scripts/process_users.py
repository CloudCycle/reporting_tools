import json
import pandas as pd
with open('data/users.json') as f:
    str = f.read()
    f.close()
obj = json.loads(str)
users = []
for user in obj.get('Users'):
    u = pd.DataFrame(user['Attributes'])
    email = u[u.Name == 'email'].Value.iloc[0]
    if 'cloudcycle' not in email:
        users.append(email)
output = f'UserCount\n{len(users)}'
with open('report.csv','w+') as f:
    f.write(output)
    f.close()

