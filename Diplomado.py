import os
import numpy as np
import matplotlib.pyplot as plt
import flopy
name = "mod_mdf06"
h1 = 100
h2 = 90
Nlay = 10
N = 101
L = 400.0
H = 50.0
k = 1.0

sim = flopy.mf6.MFSimulation(
    sim_name=name, exe_name="workspace/mf6", version="mf6", sim_ws="workspace"
)
#Crea el objeto de flopy tdis
tdis = flopy.mf6.ModflowTdis(
    sim, pname="tdis", time_units="DAYS", nper=1, perioddata=[(1.0, 1, 1.0)]
)
#Crea el paquete de objetos flopy tms
ims = flopy.mf6.ModflowIms(sim, pname="ims", complexity="SIMPLE")
#Crea el modelo del flujo del agua
model_nam_file = "{}.nam".format(name)
gwf = flopy.mf6.ModflowGwf(sim, modelname=name, model_nam_file=model_nam_file)

print(sim)