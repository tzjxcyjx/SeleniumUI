import sys
sys.path.append("E:/ui_auto/")
from util.excel_util import ExcelUtil
from keyword_selenium.actionMethod import ActionMethod
class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = ExcelUtil("E:/ui_auto/config/keyword.xls")
        case_lines = handle_excel.get_lines()
        #print(case_lines)
        if case_lines:
            for i in range(1,case_lines):
                is_run = handle_excel.get_col_values(i,3)
                print(is_run)
                if is_run =="yes":
                    method = handle_excel.get_col_values(i,4)
                    print(method)
                    send_value = handle_excel.get_col_values(i, 5)
                    #print(send_value)
                    handle_value = handle_excel.get_col_values(i, 6)
                    #print(handle_value)
                    expect_result_method = handle_excel.get_col_values(i,7)
                    expect_result = handle_excel.get_col_values(i,8)
                    # 空判断为"" 而不是None
                    self.run_method(method,send_value,handle_value)
                    if expect_result != "":
                        expect_value = self.get_expec_result_value(expect_result)
                        #print("---->",expect_value)
                        if expect_value[0] == "text":
                            #print(expect_result_method)
                            result = self.run_method(expect_result_method)
                            #print("*************",result)
                            if expect_value[1] in result:
                                handle_excel.write_value(i,9,"pass")
                            else:
                                handle_excel.write_value(i,9,"fail")

                        elif expect_value[0] == "element":
                            result = self.run_method(expect_result_method,expect_value[1])
                            if result:
                                handle_excel.write_value(i,9,"pass")
                            else:
                                handle_excel.write_value(i,9,"fail")
                    else:
                        print("预期结果为空")


    #获得预期结果值
    def get_expec_result_value(self,data):
        return data.split("=")

    def run_method(self,method,send_value="",handle_value=""):
        print(send_value ,"--------->" ,handle_value)
        method_value = getattr(self.action_method,method)
        if send_value !="" and handle_value != "":
            result = method_value(send_value,handle_value)
        elif send_value == "" and handle_value != "":
            result = method_value(handle_value)
        elif send_value != "" and handle_value == "":
            result = method_value(send_value)
        else:
            result = method_value()
        return  result

if __name__ == '__main__':
    keyword_case = KeywordCase()
    keyword_case.run_main()



    #拿到行数
        #循环行数，去执行每一行的case
        #if 是否执行
            #拿到执行方法
            #拿到操作值
            #拿到输入数据
            #if 是否有输入数据
                #执行方法（输入数据，操作元素）
            #if 没有输入数据
                #执行方法（操作元素）
