import pandas as pd

student_data = {'name': ['Adigun', 'Jag', 'Mathew', 'James', 'Yunusa'],
                'gender': ['male', 'male', 'male', 'male', 'male'],
                'age': ['22', '25', '32', '44', '21'],
                'level': ['200', '300', '100', '200', '400']}
matricNumber = ['e45767', 'e023245', 'e27863', 'e98678', 'e37658']
result = pd.DataFrame(student_data, index=matricNumber)
print(result)
