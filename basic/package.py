# import travel.thailand # I can only use a module or package after "import".
# # import travel.thailand.ThailandPackage(X)
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel import * # 이걸 쓰려면 __init__.py에 '__all__: []'을 써야함
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random)) # checking the place of the module 'random'
print(inspect.getfile(thailand))