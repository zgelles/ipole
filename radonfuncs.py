import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft
import gc

#res = 32769

rpu = 4.848136811094136e-12 #rads per uas
fluxtot = 0.712991454883995 #flux of the total image

#arrdir = '/bd4/hires/data'

def makestuff(res):
    arrdir = '/bd4/hires/fov_study/res{}'.format(res)
    arrdirnew = arrdir
    def makegaussvec(nx, ny, fovuas, fwhmuas, savetext):
        fwhmuas *= rpu
        sigma = fwhmuas / 2 / np.sqrt(2*np.log(2))
        psize = (fovuas*rpu)/nx

        xvals =  yvals = np.arange(0, -nx, -1) * psize + (psize * nx) / 2.0 - psize / 2.0

        x, y = np.meshgrid(xvals, yvals)
        gaussvec = np.exp(-(x**2+y**2)/2/sigma**2)
        #gaussvec /= np.max(gaussvec)
        gaussvec = gaussvec[0:nx, 0:ny]


        np.save(savetext, gaussvec)
        return

    def saveradon(fullarrtext, savetexts, thetavals): #theta=0 means summing down a column
        arr1 = np.load(fullarrtext)
        for i in range(len(savetexts)):
            ax1 = 0 if thetavals[i] == 0 else 1 #currently only horizontal or vertical
            arr2 = np.sum(arr1, axis=ax1)
            np.save(savetexts[i], arr2)

        return


    def savecx(fullarrtext, savetexts): #theta=0 means summing down a column
        arr1 = np.load(fullarrtext)
        np.save(savetexts[0], arr1[len(arr1)//2])
        np.save(savetexts[1], arr1[:,len(arr1)//2])
        return

    def saveradonall():
        namespre = ['tot', '0', '1', '2']
        for i in range(len(namespre)):
            print(i)
            nameload = arrdir+'/n'+namespre[i]+'array.npy'
            savetexts = [arrdirnew+'/radontransforms/n{}theta0.npy'.format(namespre[i]), arrdirnew+'/radontransforms/n{}theta90.npy'.format(namespre[i])]
            thetavals = [0, 90]
            saveradon(nameload, savetexts, thetavals)
            gc.collect()

    def savecxall():
        namespre = ['tot', '0', '1', '2']
        for i in range(len(namespre)):
            print(i)
            nameload = arrdir+'/n'+namespre[i]+'array.npy'
            savetexts = [arrdirnew+'/intensitycx/n{}horizontalcx.npy'.format(namespre[i]), arrdirnew+'/intensitycx/n{}vertcx.npy'.format(namespre[i])]
            savecx(nameload, savetexts)
            gc.collect()


    def downsample(ogtext, newnxvals, savetexts):
        x1 = np.load(ogtext)
        for i in range(len(newnxvals)):
            int1 = (len(x1)-1)//(newnxvals[i]-1)
            print(int1)
            newvec = x1[0::int1, 0::int1]
            np.save(savetexts[i], newvec)
            
        return

    def downsampleall():
        newvals = [1025, 2049, 4097, 8193, 16385, 32769]
        namespre = ['tot', '0', '1', '2']
        for i in range(len(namespre)):
            ogtext = arrdir+'/n'+namespre[i]+'array.npy'
            savetexts = ['/bd4/hires/fov_study/res{}/n{}array.npy'.format(newvals[j],namespre[i]) for j in range(len(newvals))]
            downsample(ogtext, newvals, savetexts)
            gc.collect()
        return

    saveradonall() 
    savecxall()

    return

resvals = [1025, 2049, 4097, 8193, 16385, 32769]
for res in resvals:
    makestuff(res)
    gc.collect()

        

# saveradonall()
# savecxall()
#downsampleall()
    

