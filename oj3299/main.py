'''แปลงดอกไม้'''
band_size, flower_count = map(int, input().split())

diagonal = 0
total = 0

while total < flower_count:
    diagonal += 1
    total += diagonal

band = (diagonal + band_size - 1) // band_size

print(band)
