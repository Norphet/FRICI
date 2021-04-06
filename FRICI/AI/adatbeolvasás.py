import numpy as np
import pandas as pd

import os
df = pd.concat([pd.read_json('train.json'), pd.read_json('test.json')]).reset_index()

df.ingredients = df.ingredients.apply(lambda ings : [ing.lower() for ing in ings])

#print(df.head(10))
#print(df.columns)
import itertools
# Example of what the itertools.combinations function does.
print(list(itertools.combinations(df.ingredients[0][:5], 2)))

from collections import Counter
cooc_counts = Counter()
ing_count  = Counter()
for ingredients in df.ingredients:
    for ing in ingredients:
        ing_count[ing] += 1
    for (ing_a, ing_b) in itertools.combinations(set(ingredients), 2):
        # NOTE: just making sure we added pairs in a consistent order (a < b); you can also add both (a,b) and (b,a) if you want.
        if ing_a > ing_b:
            ing_a, ing_b = ing_b, ing_a
        cooc_counts[(ing_a, ing_b)] += 1

cooc_df = pd.DataFrame(((ing_a, ing_b, ing_count[ing_a], ing_count[ing_b], cooc) for (ing_a, ing_b), cooc in cooc_counts.items()), columns=['a', 'b', 'a_count', 'b_count', 'cooc'])
print(cooc_df.sample(10))

print(cooc_df[cooc_df.a == 'chillies'].sort_values('cooc', ascending=False).head(10))