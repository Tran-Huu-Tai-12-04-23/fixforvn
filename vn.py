from cmath import exp
import scipy.io 
import numpy as np

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
print("----------END----------")
def req1(transactions):
    try:   
        list_product = []
        listsolan = []
        result_max = []
        result_min = []
        ''' list[i1 , i2 , i3 , i4 , i5 ] '''
        '''  '''
        ''' list2[i1 , i2 , i1 , i4 , i4 , i5......] '''
        for i in transactions[:,1]:
            for j in i:
                list_product.append(j.strip())
        # print(list_product)

        new_list = list(set(list_product))
        for k in new_list:
            solan = list_product.count(k)
            listsolan.append(solan)
            
        vannhi_max = max(listsolan)
        ''' tao mang chua index cua cac phan tu max trong new_list '''
        arrIndexMaxOfNewList =[]
        for i in range(0, len(listsolan)):
            if(listsolan[i]==vannhi_max):
                arrIndexMaxOfNewList.append(i)
        for i in arrIndexMaxOfNewList:
            result_max.append(new_list[i])
            
        vannhi_min = min(listsolan)
        ''' tao mang chua index cua cac phan tu min trong new_list '''
        arrIndexMinOfNewList =[]
        for i in range(0, len(listsolan)) :
            if(listsolan[i]==vannhi_min) :
                arrIndexMinOfNewList.append(i)
        print(arrIndexMinOfNewList)
        for i in arrIndexMinOfNewList :
            result_min.append(new_list[i])
    except:
        result_min = []
        result_max = []
    return sorted(result_max), sorted(result_min)


print("-----------END(Cau 1)-----------")

def req2(products):
    try:    
        name_product = []
        listtonkho = []
        result_max = []
        result_min = []
        for i in products[:,0]:
            name_product.append(i.strip())
        # print(name_product)
        for i in products[:,2]:
            listtonkho.append(np.double(i))
        tonkho_max = max(listtonkho)
        arrIndexMaxOfListTonKho = []
        for i in range(0, len(listtonkho)):
            if(listtonkho[i] == tonkho_max):
                arrIndexMaxOfListTonKho.append(i)
        for i in arrIndexMaxOfListTonKho:
            result_max.append(name_product[i])

        tonkho_min = min(listtonkho)
        arrIndexMinOfListTonKho = []
        for i in range(0, len(listtonkho)):
            if(listtonkho[i] == tonkho_min):
                arrIndexMinOfListTonKho.append(i)
        for i in arrIndexMinOfListTonKho:
            result_min.append(name_product[i])
    except:
        result_min = []
        result_max = []
    return sorted(result_max), sorted(result_min)

print("----------END(Cau 2)----------")

def req3(transactions, products):
    try:
        list_product = []
        list_gia = []
        ''' list[i1 , i2 , i3 , i4 , i5 ] '''
        '''  '''
        ''' list2[i1 , i2 , i1 , i4 , i4 , i5......] '''
        for i in transactions[:,1]:
            for j in i:
                list_product.append(j.strip())
        ''' listsanpham= [ i1 , i2 , i5 , i4,...... ] '''
        arrPriceOfListProduct = []
        for i in range(0, len(list_product)):
            for j in range(len(products[:,0])):
                if( list_product[i] == products[j][0].strip()):
                    arrPriceOfListProduct.append(np.double(products[j][1].strip()))
        result = np.sum(arrPriceOfListProduct)
    except:
        result = []
    return result

print("-----------END(Cau 3)----------")
def req4(transactions, products):
    list_product = []
    listsolan = []
    list_doanhthu = []
    result = []
    ''' list[i1 , i2 , i3 , i4 , i5 ....] '''
    ''' list3 = [2 , 1 ,0 , 2 , 1 ..... ] '''
    ''' list2[i1 , i2 , i1 , i4 , i4 , i5......] '''
    for i in transactions[:,1]:
        for j in i:
            list_product.append(j.strip())
    # print(list_product)
    
    new_list = list(set(list_product))
    print(new_list)
    for k in new_list:
        solan = list_product.count(k)
        listsolan.append(solan)
    # print(new_list)
    print(listsolan)
    ''' ['I4', 'I3', 'I2', 'I5', 'I1']
        [60, 7*20, 8*20, 2*10, 7*10]==> max = 8*20 ==> index 2==> 'i2'
        [30 , 20 , 20 , 10 , 10]'''
    ''' tao man chua gia tuong ung cho aray listsolan va new_list '''
    listgiacuamanglistsolan = []
    # lay tung index cua mang 0 , 1 , 2 , 3 , 4 , ... len(new_list)
    for j in range(len(new_list)):
        for i in range(len(products[:,0])):
            if( new_list[j].strip() == products[i][0].strip()) :
                listgiacuamanglistsolan.append(np.double(products[i][1]))
    # print(listgiacuamanglistsolan)
    for i in range(len(listsolan)):
        listsolan[i] = listsolan[i] * listgiacuamanglistsolan[i]
    max_doanhthu = max(listsolan)
    # print(listsolan)
    # print(max_doanhthu)
    arrIndexMaxOfListSoLan =[]
    for i in range(0, len(listsolan)) :
        if(listsolan[i]==max_doanhthu) :
            arrIndexMaxOfListSoLan.append(i)
    # print(arrIndexMaxOfListSoLan)
    
    for i in arrIndexMaxOfListSoLan :
        result.append(new_list[i])
    return sorted(result)

print("----------END(Cau 4)----------")

def req5(history, k):
    try:
        list_khachhang = []
        list_solangiaodich = [] 
        result = []
        for i in history[:,0]:
            list_khachhang.append(i[0])
        print(list_khachhang)

        for i in history[:,1]:
            list_solangiaodich.append(len(i))
        print(list_solangiaodich)
        
        arrIndex = []
        d  = 0
        while( d < k ) :
            d = d + 1 
            maxn = 0 
            for i in range( 0 , len(list_solangiaodich)) :
                if( list_solangiaodich[i] > list_solangiaodich[maxn] ) :
                    maxn = i 
            arrIndex.append(maxn)
            list_solangiaodich[maxn] = 0
        print(arrIndex)

        for i in arrIndex:
            result.append(list_khachhang[i])
    except:
        result = []
    return result
    

print("----------END(Cau 5)----------")

def req6(transactions, history, k):
    try:
        list_magiaodich = []
        list_allma = []
        for i in range(len(history)):
            for j in range(len(history[i,1])):
                if(history[i,0] == k):
                    list_magiaodich.append(history[i,1][j].split())
        # print(list_magiaodich)

        for i in range(len(transactions)):
            for j in range(len(transactions[i,0])):
                list_allma.append(transactions[i,0][j].split())
        # print(list_allma)
        list_sanpham = []
        for i in range(len(transactions)):
            add = ''
            for j in range(len(transactions[i,1])):
                add += transactions[i,1][j] + " "
            list_sanpham.append(add.split())
        # print(list_sanpham)
        list_spcanlietke = [] #Cac sap pham theo ma GD
        for i in range(len(list_magiaodich)):
            for j in range(len(list_allma)):
                if(list_magiaodich[i] == list_allma[j]):
                    list_spcanlietke.append(list_sanpham[j])
        # print('list_spcanlietke:',list_spcanlietke)

        dem = [] 
        outmang = []
        for i in range(len(list_spcanlietke)-1):
            dem.append(list_spcanlietke.count(list_spcanlietke[i]))
        for j in range(len(dem)-1):
            if(dem[i] == max(dem)):
                outmang.append(list_spcanlietke[i])
    except:
        outmang 
    return sorted(outmang)

print("----------END(Cau 6)----------")

def req7(transactions, history):
    try:
        list_khachhang = []
        list_solangiaodich = [] 
        list_allma = []
        list_maGD = []
        maGD_min = []
        arrOfSPitban = []
        for i in history[:,0]:
            list_khachhang.append(i[0])

        for i in history[:,1]:
            list_solangiaodich.append(len(i))
        
        for i in history[:,1]:
            list_maGD.append(i)

        for i in range(len(transactions)):
            for j in range(len(transactions[i,0])):
                list_allma.append(transactions[i,0][j].split())

        minOfSoLanGD = min(list_solangiaodich)
        arrIndexOfMinGD =[]
        for i in range(0, len(list_solangiaodich)) :
            if(list_solangiaodich[i]== minOfSoLanGD) :
                arrIndexOfMinGD.append(i)
        for i in arrIndexOfMinGD :
            maGD_min.append(list_maGD[i][0])

        arrOfAllSpTuongUngMaGD = []
        for i in range(len(transactions)):
            add = ''
            for j in range(len(transactions[i,1])):
                add += transactions[i,1][j] + " "
            arrOfAllSpTuongUngMaGD.append(add.split())

        list_spcanlietke = [] #Cac sap pham theo ma GD da dua ra
        for i in range(len(maGD_min)):
            for j in range(len(list_allma)):
                if(maGD_min[i] == list_allma[j][0]):
                    for it in arrOfAllSpTuongUngMaGD[j]:
                        list_spcanlietke.append(it)

        dem = []
        outmang = []
        for i in range(len(list_spcanlietke)-1):
            dem.append(list_spcanlietke.count(list_spcanlietke[i]))
        
        # tao motj mang moi chua ten cua san pham khong trung nhau
        arrNameOnly = list(set(list_spcanlietke))

        listsolan = []
        result = []
        for k in arrNameOnly:
            solan = list_spcanlietke.count(k)
            listsolan.append(solan)
        xuathiennhieunhat = max(listsolan)
        ''' tao mang chua index cua cac phan tu max trong new_list '''
        arrIndexMaxOfNewList =[]
        for i in range(0, len(listsolan)):
            if(listsolan[i]==xuathiennhieunhat):
                arrIndexMaxOfNewList.append(i)
        for i in arrIndexMaxOfNewList:
            result.append(arrNameOnly[i])
    except:
        result = []
    return sorted(result)
    

print("----------END(Cau 7)----------")

def req8(transactions, history, k):
    # try :
    def tinhvector(k , history, transactions):
        vector = []
        list_magiaodich = []
        for i in range(len(history)):
            for j in range(len(history[i, 1])):
                if(history[i][0][0].strip() == k):
                    list_magiaodich.append(history[i][1][j].strip())
        list_SPTuongung = []
        for i in range(len(transactions)):
            for j in range(len(list_magiaodich)):
                if(transactions[i,0][0].strip() == list_magiaodich[j].strip()):
                    for d in transactions[i,1]:
                        list_SPTuongung.append(d.strip())
        list_tatcaSP = []
        for i in transactions[:,1]:
            for j in i:
                list_tatcaSP.append(j.strip())
        mangDaXoaTrung = list(set(list_tatcaSP))
        def countpt(str1, arr):
            d = 0
            for i in arr:
                if i == str1:
                    d = d + 1
            return d
        for i in mangDaXoaTrung:
            vector.append(countpt(i, list_SPTuongung))
        return vector
    vectorU = tinhvector(k , history, transactions)
    mangChuaMaGDKhacK = []
    for i in history[:,0]:
        if(i[0].strip() != k):
            mangChuaMaGDKhacK.append(i[0])
    arrVecTorV = []
    for i in mangChuaMaGDKhacK:
        print(i)
        arrVecTorV.append(tinhvector(i , history, transactions))
    print("arrVecTorV : " , arrVecTorV)
    list_DoGiongNhau = []
    def doDoTuongTu(vectorU, vectorV):
        kq = np.dot(vectorU, vectorV)
        if( kq != 0 ):
            dogiong = kq /((np.linalg.norm(vectorU)) * np.linalg.norm(vectorV))
            return dogiong
        else : 
            resultDoGiong = []
    for i in arrVecTorV:
        list_DoGiongNhau.append(doDoTuongTu(vectorU, i))
    
    indexViTri = []
    resultDoGiong = []
    result = max(list_DoGiongNhau)
    for i in range(0, len(list_DoGiongNhau)):
        if(list_DoGiongNhau[i]==result):
            indexViTri.append(i)
    for i in indexViTri:
        resultDoGiong.append(mangChuaMaGDKhacK[i])
    ''' except:
        resultDoGiong = [] '''
    return resultDoGiong

print("----------END(Cau 8)----------")

def req9(transactions, history, products):
    try:
        list_maGD = []
        list_allma = []
        for i in history[:,1]:
            list_maGD.append(i)

        for i in range(len(transactions)):
            for j in range(len(transactions[i,0])):
                list_allma.append(transactions[i][0][j].strip())

        # arrOfAllSpTuongUngMaGD = []
        newArr = []
        for i in range(len(list_allma)):
            for j in range(len(transactions[:,0])) :
                if( list_allma[i] == transactions[j][0][0].strip()):
                    print(transactions[j][1])
                    for k in transactions[j][1]:
                        newArr.append(k)
            
        mangSauKhiXoaTrung = list(set(newArr))

        list_TatCaSPCuaHangCo = []
        for i in products[:,0]:
            list_TatCaSPCuaHangCo.append(i.strip())
        
        SPKhongBanDuoc = []
        for i in list_TatCaSPCuaHangCo:
            if i not in mangSauKhiXoaTrung:
                SPKhongBanDuoc.append(i)
    except:
        SPKhongBanDuoc = []
    return SPKhongBanDuoc

print("----------END(Cau 9)----------")

def req10(history, transactions, products, k):
    try:
        list_maGD = []
        list_allma = []
        for i in range(len(history)):
                for j in range(len(history[i, 1])):
                    if(history[i][0][0].strip() == k):
                        list_maGD.append(history[i][1][j].strip())
        for i in range(len(transactions)):
            for j in range(len(transactions[i,0])):
                list_allma.append(transactions[i][0][j].strip())
        list_SPTuongung = []
        for i in range(len(list_allma)):
            for j in range(len(list_maGD)):
                if(list_allma[i].strip() == list_maGD[j].strip()):
                    for d in transactions[i,1]:
                        list_SPTuongung.append(d.strip())
        arrOfPhanKhuc = []
        for j in range(len(list_SPTuongung)):
            for i in range(len(products[:,3])):  
                if(products[i][0].strip() == list_SPTuongung[j].strip()):
                    arrOfPhanKhuc.append(int(products[i][3]))
        new_list = list(dict.fromkeys(arrOfPhanKhuc))
        list_solan = []
        for k in new_list:
            solan = sorted(arrOfPhanKhuc).count(k)
            list_solan.append(solan)

        result_max = []
        timmax = max(list_solan)
    
        ''' tao mang chua index cua cac phan tu max trong new_list '''
        for i in range(0, len(list_solan)):
            if(list_solan[i]==timmax):
                resultIndex = i
                break
        result_max = new_list[resultIndex]
    except:
        print("hello wo")
        result_max = []
    return result_max
# print(" cau 1: " , req1(transactions))    
# print(" cau 2: " , req2(products))	
# print(" cau 3: " , req3(transactions, products)) 
# print(" cau 4: " , req4(transactions,products)) 
# print(" cau 5: " , req5(history, 3)) 
# print(" cau 6: " , req6(transactions,history,'K6'))
# print(" cau 6: " , req6(transactions,history,'K5'))
# print(" cau 6: " , req6(transactions,history,'K4'))
# print(" cau 6: " , req6(transactions,history,'K3'))
# print(" cau 6: " , req6(transactions,history,'K2'))
# print(" cau 6: " , req6(transactions,history,'K1'))
# print(" cau 7: " , req7(transactions, history))
print(" cau 8: " , req8(transactions, history,'K4')) #!fix
print(" cau 8: " , req8(transactions, history,'K3')) #!fix
print(" cau 8: " , req8(transactions, history,'K2')) #!fix
print(" cau 8: " , req8(transactions, history,'K1')) #!fix
print(" cau 8: " , req8(transactions, history,'K5')) #!fix
print(" cau 8: " , req8(transactions, history,'K6')) #!fix
# print(" cau 9: " , req9(transactions, history, products))
# print(" cau 10: " , req10(history, transactions, products, 'K6'))
# print(" cau 10: " , req10(history, transactions, products, 'K1'))
# print(" cau 10: " , req10(history, transactions, products, 'K2'))
# print(" cau 10: " , req10(history, transactions, products, 'K3'))
# print(" cau 10: " , req10(history, transactions, products, 'K4'))
# print(" cau 10: " , req10(history, transactions, products, 'K5'))