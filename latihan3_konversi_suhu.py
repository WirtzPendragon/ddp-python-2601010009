#Program konversi suhu dari Celcius ke Fahrenheit dan Kelvin

#Mengambil input suhu dalam Celcius dari user
celcius = float(input("Masukkan suhu dalam Celcius: "))

#Menghitung suhu dalam Fahrenheit dan Kelvin
fahrenheit = (celcius * 9/5) + 32
kelvin = celcius + 273.15

#Menampilkan hasil konversi suhu
print(f"Suhu dalam Fahrenheit: {fahrenheit}°F\nSuhu dalam Kelvin: {kelvin}°K")