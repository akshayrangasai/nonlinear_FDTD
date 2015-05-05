from sklearn.gaussian_process import GaussianProcess as GMM
#from sklearn.svm import SVR as GMM
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
FILE = 'data/sheet.csv'
dataset = np.vstack(set(map(tuple,np.genfromtxt(FILE, delimiter=','))))

def addNoise(snr):
    signal = dataset[:,-1]
    #print signal
    signalstd = np.std(signal)
    noisestd = signalstd/np.sqrt(snr)
    noise = np.random.normal(0,noisestd,len(signal))
    datasetnoisy = dataset
    datasetnoisy[:,-1] = datasetnoisy[:,-1] + noise
    return datasetnoisy

def ensemble(value, noise):

    #mixture = GMM(C = 100)
    mixture = GMM()
    newdataset = addNoise(noise)
    temp = np.copy(newdataset[:,-1])
    #newdataset[:,-1] = newdataset[:,2]
    #newdataset[:,2] = temp
    #print newdataset[:,-1], newdataset[:,3]
    for ensemble in range(0,value):
        np.random.shuffle(newdataset)
        train = np.copy(newdataset[0:-10,:])
        test =  np.copy(newdataset[-10:-1,:])
        test_pred = np.copy(test)
        mixture.fit(newdataset[0:-10,0:-2],newdataset[0:-10,-1])
        preds = mixture.predict(newdataset[-10:-1,0:-2])
        test_pred[:,-1] = preds
        errorabs =  abs(dataset[-10:-1,-1]-preds)/(dataset[-10:-1,-1])
        meanerrorabs = np.mean(errorabs)
        stderrorabs = np.std(errorabs)
        #print errorabs
        print meanerrorabs, stderrorabs
        #plt.plot(abs(dataset[-10:-1,-1]-preds))
        #plt.ylim(-5e-12,5e-12)
        #plt.scatter(dataset[-10:-1,0],dataset[-10:-1,-1])
        #plt.plot(preds)
        #plt.show()
        np.savetxt('data/forward_train_%d_snr_%d.csv'%(ensemble,noise),train,delimiter=',')
        np.savetxt('data/forward_test_%d_snr_%d.csv'%(ensemble,noise),test,delimiter=',')
        np.savetxt('data/forward_test_predict_%d_snr_%d.csv'%(ensemble,noise),test_pred,delimiter=',')
        #sp.io.savemat('data/train_%d_snr_%d.mat'%(ensemble,noise),train)
        #sp.io.savemat('data/test_%d_snr_%d.mat'%(ensemble,noise),test)
        #sp.io.savemat('data/test_predict_%d_snr_%d.mat'%(ensemble,noise),test_pred)
for noise in range(2,20,2):
    ensemble(1, noise)
