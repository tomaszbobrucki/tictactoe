dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

words = input().split()

new1 = [i for i in words if i not in dictionary]
if len(new1) > 0:
    print("\n".join(new1))
else:
    print("OK")
