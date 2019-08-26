import netifaces as ni
import winreg as wr

def get_connection_name_from_guid(iface_guids):
    #接口名字和windows唯一ID的清单
    iface_dict = {}
    #打开"HKEY_LOCAL_MACHINE"
    reg = wr.ConnectRegistry(None,wr.HKEY_LOCAL_MACHINE)
    # 打开r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}'，固定的
    reg_key = wr.OpenKey(reg , r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}')

    for i in iface_guids:
        try:
            #尝试读取每一个接口ID下对应的Name
            #print(i) #
            reg_subkey = wr.OpenKey(reg_key , i + r'\Connection')
            #如果存在Name，写入iface_dict字典
            iface_dict[wr.QueryValueEx(reg_subkey , 'Name')[0]] = i  #读取Name放入印刷的字典
        except FileNotFoundError:
            pass
    # print('所有接口信息字典列表： ' + str(iface_dict) + '\n')
    return iface_dict

def win_from_name_get_id(ifname):
    x = ni.interfaces()
    #print(x)
    # x为获取的接口清单 [... '{A7584008-7824-4760-B2E0-1D0F483FD64E}', '{CD94297B-D746-4494-91F7-3E40C091A0FC}',
    # '{652C7833-4B8D-400F-A72F-F7C89C30FD03}'...] ，太多就省略了
    return get_connection_name_from_guid(x).get(ifname)

if __name__ == '__main__':
    print(win_from_name_get_id('WLAN'))
