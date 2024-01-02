import numpy as np

def calculate(list):
  if len(list)!=9:
    raise ValueError('List must contain nine numbers.')
  mat=np.resize(list,(3,3))
  calculations={}
  calculations['mean']=[np.mean(mat,axis=0).tolist(),np.mean(mat,axis=1).tolist(),np.mean(list)]
  calculations['variance']=[np.var(mat,axis=0).tolist(),np.var(mat,axis=1).tolist(),np.var(list)]
  calculations['standard deviation']=[np.std(mat,axis=0).tolist(),np.std(mat,axis=1).tolist(),np.std(list)]
  calculations['max']=[np.max(mat,axis=0).tolist(),np.max(mat,axis=1).tolist(),np.max(list)]
  calculations['min']=[np.min(mat,axis=0).tolist(),np.min(mat,axis=1).tolist(),np.min(list)]
  calculations['sum']=[np.sum(mat,axis=0).tolist(),np.sum(mat,axis=1).tolist(),np.sum(list)]
  
  return calculations