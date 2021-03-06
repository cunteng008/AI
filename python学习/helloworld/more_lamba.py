# 在我们的案例中，我们希望进行一次自定义排序，为此我们需
# 要编写一个函数，但是又不是为函数编写一个独立的 def 块，
# 只在这一个地方使用，因此我们使用 Lambda 表达式来创建一个新函数。
points = [{'x': 2, 'z': 3},
{'x': 4, 'z': 5}]
points.sort(key=lambda i: i['z'])  # 创建函数 i
print(points)