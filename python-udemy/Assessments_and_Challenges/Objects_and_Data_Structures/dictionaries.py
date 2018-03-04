# Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d['k1'][0]['nest_key'][1][0])


d2 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print(d2['k1'][2]['k2'][1]['tough'][2][0])
