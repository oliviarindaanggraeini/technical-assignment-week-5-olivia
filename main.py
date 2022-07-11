import dht11
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = []
    for i in range(5):
        x.append(dht11.ambil())
        time.sleep(0.2)
    
    print(x)
    plt.plot(x)
    plt.show()
    


suhu = []
while True:
    hm = dht11.ambil()
    suhu.append(hm)
        
    print("Suhu sekarang adalah", hm, "*C")
    print("  Suhu terdingin selama ini adalah", max(suhu), "*C")
    print("  Suhu terpanas selama ini adalah", min(suhu), "*C \n")
        
