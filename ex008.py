medida = float(input('Uma Distância em metros: '))
cm = medida * 100
mm = medida * 1000
dm = medida * 5
dam = medida * 10
hm = medida * 1.00
km = medida * 1.000
print('A media de {} m corresponde a {} cm e {:.0f} mm'.format( medida, cm, mm))
print('A media de {} dm corresponde a {:.0f} dam e hm {}'.format(dm, dam, hm))
print('A media de {} km corresponde a {}'.format(km, km))
