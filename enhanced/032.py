f=open(r'C:\Users\yuerunyu\Desktop\sw14.txt')
info={}
for each_line in f:


    if (each_line[:6] != '------') or (each_line[:6] != "     "):
        print(each_line)
        # (seca,secb) = each_line.split(':', 1)
        # info[seca]=secb
        # # if port == '1/7/1':
        # #     info.append(line_spoken)
        # print(info)
f.close()