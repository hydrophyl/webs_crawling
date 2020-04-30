import re

target = '''@Patient
Name,Sex,DOB,Weight,Height,PhoneNumber
Nguyễn Văn A,M,25/04/1972,87.00,171,0921812525,
@Device
Serial,AppVer
MS3001479TZR;1.7.1260
@Sensor_A
Time,A1,A2,A3
1561571170041,0.092407,0.799255,0.593933
1561571170041,0.091797,0.798950,0.591187
1561571170041,0.078552,-0.031006,1.026550
1561571170189,0.079102,-0.031006,1.035645
1561571170189,0.079041,-0.030396,1.033752
1561571170189,0.078918,-0.030640,1.033752
@Sensor_B
Time,B1,B2,B3
1561571169993,-1.920732,-3.860518,-0.213415
1561571169993,-0.758384,-2.907774,1.539634
1561571169993,-0.807927,-0.194360,-0.522104
1561571170140,-0.636433,-0.201982,-0.590701
1561571170140,-0.510671,0.080030,-0.438262
1561571170140,-0.487805,0.000000,-0.48399'''

#print(target)
#print(re.findall(r'@\w+',target))

#print(re.findall(r'[AB]\d{1}', target))

#print(re.search(r'\w+[ \w+]*', 'Trần Xuân Thy, Matnr. 2359864'))

#print(re.search(r'\w+ [ \w+]*', target))

print(re.findall(r'Se\w+', target))
print(re.findall('\d{10}', target))
print(re.findall('\d*/\d*/\d*', target))
print(re.findall(r'MS\w+', target))
print(re.findall('[0-3][.]\d{3,6}', target))
