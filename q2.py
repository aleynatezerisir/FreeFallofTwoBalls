from drawingpanel import *
def main():
    panel = DrawingPanel(600, 600)
    #Ball-1
    ball1x = 100
    ball1y = 0
    v01 = 25
    #Ball-2
    ball2x = 200
    ball2y = 100
    v02 = 15
    #Bal3
    ball3x = 300
    ball3y = 0
    v03 = 50

    for time in range(0, 80, 1):
        disp1 = displacement(v01, time/10, 9.81)
        panel.canvas.create_oval(ball1x, ball1y + disp1, ball1x + 10, ball1y + 10 + disp1)
        disp2 = displacement(v02, time/10, 9.81)
        panel.canvas.create_oval(ball2x, ball2y + disp2, ball2x + 10, ball2y + 10 + disp2)
        disp3 = displacement(v03, time/10, 9.81)
        panel.canvas.create_oval(ball3x, ball3y + disp3, ball3x + 10, ball3y + 10 + disp3)
        panel.sleep(50) # pause for 50 ms
        panel.canvas.create_rectangle(0, 0, 600, 600, fill="white", width=0)

def displacement(v,time,a):
    dp = (v*time)+(a*time*time)/2
    return dp

main()
