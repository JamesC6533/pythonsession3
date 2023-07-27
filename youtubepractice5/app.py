from ecommerce import shipping
from pathlib import Path

# shipping.calc_shipping()
# path = Path("emails")
# print(path.mkdir())
# print(path.rmdir())

# print(path.exists())

# get all files in current directories ('*.*')
path = Path()
print(path.glob('*.py'))

for file in path.glob('*.py'):
    print(file)