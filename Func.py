

steel = 0
miners = 1

def trueSteelTime(labelSteel):
    def sTimeFind():
        global miners
        global steel
        steelVar = miners
        steeltime = (1000 / steelVar)
        steel = steel + 1
        labelSteel.config(text="Steel: " + str(steel))
        labelSteel.after(int(steeltime), sTimeFind)
    sTimeFind()

def HireButton():
    currentbottomframe = 0



