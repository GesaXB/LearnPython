# Merubah sebuah tipedata
# tipedata = string,interger,float

## INTERGER
print('===INTERGER===')
data_int = 10
print('Data = ', data_int , " Type = ", type(data_int))

data_float = float(data_int)
data_string = str(data_int)
data_boolean = bool(data_int) # akan false jika nilai data_int = 0
print('Data = ', data_float, ' Type = ', type(data_float))
print('Data = ', data_string, ' Type = ', type(data_string))
print('Data = ', data_boolean, ' Type = ', type(data_boolean))

## STRING 
# tipe string tidak bisa di ubah menjadi float
print('===STRING===')
data_string = 'NaisaCantik'
print('Data = ', data_string , " Type = ", type(data_string))

data_int = str(data_string)
data_boolean = bool(data_string)
print('Data = ', data_string, ' Type = ', type(data_string))
print('Data = ', data_boolean, ' Type = ', type(data_boolean))



