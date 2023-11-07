import math

theta_left = -0.1388
theta_right = -0.0998

def rot(bb,Cx,Cy,angle):
    bb_re = [0,0,0,0,0,0,0,0]
    for i in range(4):
        x = bb[2*i]
        y = bb[2*i+1]
        bb_re[2*i] = Cx + (x - Cx) * math.cos(angle) - (y - Cy) * math.sin(angle)
        bb_re[2*i+1] = Cy + (x - Cx) * math.sin(angle) + (y - Cy) * math.cos(angle)
    
    return bb_re

def calcDiv(bb1,bb2):
    sum1 =0
    sum2 =0
    for i in range(4):
        sum1 += bb1[2*i + 1]
        sum2 += bb2[2*i + 1]
    Y1 = sum1 / 4
    Y2 = sum2 / 4
    return Y1 - Y2

def calcCenter(bb):
    x = 0
    y = 0
    for i in range(4):
        x += bb[2 * i]
        y += bb[2 * i + 1]
    return x/4, y/4

def addY(bb,div):
    for i in range(4):
        bb[2*i+1] += div
    return bb
        
def outBb(bb):
    print(f'A=({bb[0]},{bb[1]})')
    print(f'B=({bb[2]},{bb[3]})')
    print(f'C=({bb[4]},{bb[5]})')
    print(f'D=({bb[6]},{bb[7]})')

def rotDiv(bb):
    LCx = (bb[0] + bb[6])/2
    LCy = (bb[1] + bb[7])/2
    RCx = (bb[2] + bb[4])/2
    RCy = (bb[3] + bb[5])/2
    
    Langle = (bb[1] - bb[7])/(bb[0] - bb[6])
    Rangle = (bb[3] - bb[5])/(bb[2] - bb[4])
    print(Langle/abs(Langle))
    thetaL = (math.pi/2 - abs(math.atan(Langle)))*(Langle/abs(Langle))
    thetaR = (math.pi/2 - abs(math.atan(Rangle)))*(Rangle/abs(Rangle))
    
    left_bb = rot(bb,LCx,LCy,thetaL)
    right_bb = rot(bb,RCx,RCy,thetaR)
    
    print("ROTATE BY LEFT")
    print(f'LCx={LCx},LCy={LCy},Langle={Langle},thetaL={thetaL}')
    outBb(left_bb)
    print("--------------------------------")
    print("ROTATE BY RIGHT")
    print(f'RCx={RCx},RCy={RCy},Rangle={Rangle},thetaR={thetaR}')
    outBb(right_bb)
    
    return thetaL, thetaR, left_bb,right_bb
    
bb = [187, 347,228,351,221,424,179,421]
thetaL, thetaR, left_bb,right_bb = rotDiv(bb)
div = calcDiv(left_bb,right_bb)
print(f'div={div}')

bbo = [186,1069,229,1066,227,1099,185,1102]
oCx, oCy = calcCenter(bbo)
bbo = rot(bbo,oCx, oCy,thetaL)
print("--------------------------------")
print(f'center:({oCx},{oCy})')
print("お")
outBb(bbo)

bbturi = [335,1059,372,1057,376, 1095,335, 1098]
turiCx, turiCy = calcCenter(bbturi)
bbturi = rot(bbturi,turiCx, turiCy,thetaL)
print("--------------------------------")
print("釣")
outBb(bbturi)

bb3000 = [518,1049,739,1044,740,1080,518,1084]
mCx, mCy = calcCenter(bb3000)
bb3000 = rot(bb3000,mCx, mCy,thetaR)
bb3000 = addY(bb3000,div)
print("--------------------------------")
print("￥3000")
outBb(bb3000)



