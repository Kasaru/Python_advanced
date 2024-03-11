s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
result = {}
l = s.split()
i = 0
while len(s) > 0 and i < len(l):
    if l[i] not in result.keys():
        result[l[i]] = s.count(l[i])
        s = s.replace(l[i], '')
    i += 1
new_result = {value:key for key, value in result.items()}
print(new_result.get(max(new_result.keys())))