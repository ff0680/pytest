import logging,time
import os
#log_path是存放日志的路径
class Log:
    def __init__(self,log_path):
        self.log_path=log_path
        self.logname=os.path.join(log_path,'%s.log'%time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s]-%(filename)s]-%(levelname)s:%(message)s')

    def __console(self, level, message):
        fh =logging.FileHandler(self.logname,'a',encoding='utf-8')#这个是python3的  # 追加模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        # 创建一个StreamHandler,用于输出到控制台
        ch=logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
            # 这两行代码是为了避免日志输出重复问题self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
            # 关闭打开的文件
        fh.close()
    def debug(self, message):
        self.__console('debug', message)
    def info(self, message):
        self.__console('info', message)
    def warning(self, message):
        self.__console('warning', message)
    def error(self, message):
        self.__console('error', message)
if __name__ == "__main__":
    log=Log("/Users/xiaoff/python/pytest/test_03/logs")
    log.info("---测试开始----")
    log.info("操作步骤1,2,3")
    log.warning("----测试结束----")


