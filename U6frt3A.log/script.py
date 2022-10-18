#!/usr/bin/python23
# # Importer les éléments nécessaires pour créer le serveur
from pymodbus.server import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

# Créer un jeu de données et lu affecter des valeurs
store = ModbusSlaveContext(
    di = ModbusSequentialDataBlock(1, [17]*100),    # Entrées discrètes
    co = ModbusSequentialDataBlock(0, [17]*100),    # Coils
    hr = ModbusSequentialDataBlock(0, [17]*100),    # Holding Register
    ir = ModbusSequentialDataBlock(0, [17]*100))    # Input Registers
context = ModbusServerContext(slaves=store, single=True)

# Ces champs permettent d'identifier le serveur modbus

identity = ModbusDeviceIdentification()
identity.VendorName  ='Schneider'
identity.ProductCode ='BetaTest'
identity.VendorUrl   ='https://monserver.com'
identity.ProductName ='Serveur ModbusBeta'
identity.ModelName   ='PyModBus'
identity.MajorMinorRevision ='0.1'

#Bind le serveur sur le port TCP 502
StartTcpServer(context=context, identity=identity, address=("0.0.0.0", 502))