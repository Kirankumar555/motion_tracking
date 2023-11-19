import pandas as pd
from matplotlib import pyplot as plt

data=pd.read_csv("E:\sensor\other2\Accelerometer.csv")
g=pd.read_csv("E:\sensor\other2\Gravity.csv")
# gx=g.x
# gy=g.y
#gz=g.z

x=data.x
y=data.y
z=data.z
dt=data.seconds_elapsed
time=data.time
#
# x-=gx
# y-=gy
#z-=gz
t=[0]
for k in range(len(dt)-1):
    if dt[k] !=len(dt):
        del_t=dt[k+1]-dt[k]
        t.append(del_t)
def noice(x,t):

def velocity(acc,t):
    u=[]
    u1=0
    for a,t in zip(acc,t):
        u1+=a*t
        u.append(u1)
    return u
UX=velocity(x,t)
UY=velocity(y,t)
UZ=velocity(z,t)
def position(u,acc,t):
    pos=[]
    p=0
    for j,a,dt in zip(u,acc,t):
        p+=j*dt+(0.5*a*(dt**2))
        pos.append(p)
    return pos
X=position(UX,x,t)
Y=position(UY,y,t)
Z=position(UZ,z,t)

fig = plt.figure()

# ax = plt.axes(projection='3d')
# ax.plot3D(X,Y,Z)
plt.plot(dt,Y)
plt.show()

