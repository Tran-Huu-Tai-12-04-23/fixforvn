
import scipy.io 
import numpy as np
from sympy import radsimp, re

''' data = scipy.io.loadmat('data.mat') '''

transactions = np.array([[np.array(['DON1'], dtype = object), np.array(['SP1', 'SP7', 'SP2', 'SP10'], dtype = object)],
                         [np.array(['DON3'], dtype = object), np.array(['SP6', 'SP1', 'SP6'],  dtype = object)],
                         [np.array(['DON2'], dtype = object), np.array(['SP8','SP10', 'SP2', 'SP3', 'SP5'], dtype = object)],
                         [np.array(['DON4'], dtype = object), np.array(['SP1', 'SP9'], dtype = object)],
                         [np.array(['DON5'], dtype = object), np.array(['SP6'], dtype = object)],
                         [np.array(['DON8'], dtype = object), np.array(['SP1', 'SP2', 'SP3', 'SP6', 'SP8'], dtype = object)],
                         [np.array(['DON9'], dtype = object), np.array(['SP2', 'SP7', 'SP1', 'SP9', 'SP3'], dtype = object)],
                         [np.array(['DON7'], dtype = object), np.array(['SP3', 'SP4', 'SP1'], dtype = object)],
                         [np.array(['DON6'], dtype = object), np.array(['SP6', 'SP7','SP10', 'SP3'], dtype = object)],
                         [np.array(['DON10'], dtype = object), np.array(['SP5', 'SP7', 'SP3', 'SP6'], dtype = object)]])
products = np.array([["SP1 ", '20.1', '5', '3'], 
                     ["SP4   ", '10.79', '8', '1'], 
                     ["SP9 ", '20.52', '11', '2'], 
                     ["SP6 ", '30.89', '0', '3'], 
                     ["SP5 ", '10.61', '5', '3'], 
                     ["SP3 ", '30.10', '1', '1'], 
                     ["SP7 ", '30.11', '4', '2'], 
                     ["SP8 ", '20.32', '11', '2'], 
                     ["SP10 ", '20.99', '3', '3'], 
                     ["SP11 ", '10.51', '10', '1'],
                     ["SP2", '20.91', '8', '1']])
history = np.array([[np.array(['K1 '], dtype = object), np.array(['DON2', 'DON6', 'DON1', 'DON8 '], dtype = object)],
                         [np.array(['K2'], dtype = object), np.array(['DON1 ', 'DON3', 'DON6'],  dtype = object)],
                         [np.array(['K4'], dtype = object), np.array(['DON4','DON9'], dtype = object)],
                         [np.array(['K3'], dtype = object), np.array(['DON1', 'DON3'], dtype = object)],
                         [np.array(['K5 '], dtype = object), np.array(['DON8'], dtype = object)],
                         [np.array(['K6 '], dtype = object), np.array(['DON5', 'DON9', 'DON7', 'DON4', 'DON2'], dtype = object)]])

def req8(transactions, history, k):
    try:
        def travegiatriketqualadogiong(vector_U , vector_V):
            items = np.dot( vector_U , vector_V) 
            if( items != 0):
                theSameREq4 = items / ( np.linalg.norm(vector_U) * np.linalg.norm(vector_V))
            return theSameREq4
        def travekqvector(transactions, history, k):
            i = 0 
            d = len(history[:,0])
            listdanhsachmamakhachhangk = []
            while( i < d):
                if(history[i][0][0].strip() == k):
                    listdanhsachmamakhachhangk.append(history[i][0][0].strip())
                i = i + 1 
            
            listmagiaodichcuakhachhangk = []
            for d in listdanhsachmamakhachhangk:
                for j in range(len(history[: , 0])):
                    if( d == history[j][0][0].strip()):
                        for s in history[j][1]:
                            listmagiaodichcuakhachhangk.append(s.strip())
            ''' tim sp cua khach hang k '''
        
            def timspcuakhachhangtrongk( transactions , listmakhachhang):
                
                spcaumakhachahng = []
                for f in listmakhachhang:
                    h = 0 
                    while( h < len(transactions[:, 1])):
                        if( f == transactions[h][0][0].strip()):
                            for i in transactions[h][1]:
                                spcaumakhachahng.append(i)
                        h = h + 1 
                return spcaumakhachahng
                        
            timspcuakhachhangtrongk = timspcuakhachhangtrongk( transactions , listmagiaodichcuakhachhangk)
            
            cacspcotrongcauhangtrongbai = []
            for f in transactions:
                i = 0
                while(i < len(f[1])):
                    cacspcotrongcauhangtrongbai.append(f[1][i])
                    i = i + 1 
            cacspcotrongcauhangtrongbai = list(dict.fromkeys(cacspcotrongcauhangtrongbai))
            
            vector = []
            for i in cacspcotrongcauhangtrongbai :
                vector.append(timspcuakhachhangtrongk.count(i))
            return vector
        
        vectorU = travekqvector(transactions, history, k)
        
        cacamakhachhangkhacK = []
        i = 0
        while( i < len(history[:,0])):
            if( history[i][0][0].strip() != k ):
                cacamakhachhangkhacK.append( history[i][0][0].strip())
            i = i + 1 
        
        cacvectorv = []    
        mangchuadogiongcuahaivectors = []
        for it in cacamakhachhangkhacK:
            it2 = travekqvector(transactions , history , it)
            cacvectorv.append(it2)
        for item in cacvectorv :
            mangchuadogiongcuahaivectors.append(travegiatriketqualadogiong(vectorU , item))
        
        def traveketquacaubaireq8(mangchuadogiongcuahaivectors ,cacamakhachhangkhacK ):
            traveketquacuareq8 = []
            traveketquaindex = 0
            mangtraveketquaindex = []
            d = 0 
            while( d < len(mangchuadogiongcuahaivectors)):
                if( mangchuadogiongcuahaivectors[d] > mangchuadogiongcuahaivectors[traveketquaindex] ):
                    traveketquaindex = d 
                d =  d + 1
            for f in range(len(mangchuadogiongcuahaivectors)):
                if( mangchuadogiongcuahaivectors[f] == mangchuadogiongcuahaivectors[traveketquaindex]):
                    mangtraveketquaindex.append(f)
            for item in mangtraveketquaindex:
                traveketquacuareq8.append(cacamakhachhangkhacK[item])
            return traveketquacuareq8
        return traveketquacaubaireq8(mangchuadogiongcuahaivectors ,cacamakhachhangkhacK )    
    except:
        return []
        
print('req8(transactions, history,\'K1\')', req8(transactions, history,'K1')) #!fix
print('req8(transactions, history,\'K2\')', req8(transactions, history,'K2')) #!fix
print('req8(transactions, history,\'K3\')', req8(transactions, history,'K3')) #!fix
print('req8(transactions, history,\'K4\')', req8(transactions, history,'K4')) #!fix
print('req8(transactions, history,\'K5\')', req8(transactions, history,'K5')) #!fix
print('req8(transactions, history,\'K6\')', req8(transactions, history,'K6')) #!fix
print('req8(transactions, history,\'K7\')', req8(transactions, history,'K7')) #!fix
print('req8(transactions, history,\'K8\')', req8(transactions, history,'K8')) #!fix
print('req8(transactions, history,\'K9\')', req8(transactions, history,'K9')) #!fix
print('req8(transactions, history,\'K9\')', req8(transactions, history,1)) #!fix
print('req8(transactions, history,\'K9\')', req8(12123134, history,'K5')) #!fix
print('req8(transactions, history,\'K9\')', req8(transactions, 234123,'K5')) #!fix