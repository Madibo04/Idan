import pandas as pd
import numpy as np

# numpy array with random values

a = np.random.rand(2, 6)
print(a)
# reshaping the array

print(a.reshape(6, 2))

# A pandas dataframe indexed by student
# matric number and containing the name, age, gender and level

student_data = {'Name': ['Emmanuel James', 'Afolabi Rukayat',
                         'Micheal Oliver', 'Ishola Kehinde',
                         'Ogunjimi Oluwabukola'],
                'Gender': ['Male', 'Female', 'Male', 'Male', 'Female'],
                'Age': ['20', '22', '31', '25', '21'],
                'Level': ['200', '300', '100', '400', '200']}
MatricNumber = ['e05767', 'e023245', 'e07863', 'e08678', 'e07658']
result = pd.DataFrame(student_data, index=MatricNumber)
print(result)
