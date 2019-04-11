import configparser

class ReadIni(object):
    #使用构造函数初始化file_name 和node 节点
    def __init__(self,file_name=None,node = None):
        if file_name == None:
            file_name = "E:/ui_auto/config/LocalElement.ini"
        if node == None:
            self.node = "RegisterElement"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)
    #加载文件
    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf
    #获取value的值
    def get_value(self,key):
        data = self.cf.get(self.node, key)
        return data

if __name__ == '__main__':
    read_init = ReadIni()
    print(read_init.get_value("user_name"))



# cf = configparser.ConfigParser()
# cf.read("E:/ui_auto/config/LocalElement.ini")
# print(cf.get("RegisterElement","user_email"))



