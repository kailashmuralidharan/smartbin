import logging

class BinAppLogger :
   __instance = None
   # # Gets or creates a logger
   _logger = logging.getLogger(__name__)
   # set log level
   _logger.setLevel(logging.WARNING)
    # define file handler and set formatter
   _file_handler = logging.FileHandler('logfile.log')
   _formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
   _file_handler.setFormatter(_formatter)
    # add file handler to logger
   _logger.addHandler(_file_handler)

# Logs

   @staticmethod 
   def getAppLogger():
      """ Static access method. """
      if BinAppLogger.__instance == None:
         BinAppLogger()
      return BinAppLogger.__instance
   def __init__(self):
      """ Virtually private constructor. """
      if BinAppLogger.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         BinAppLogger.__instance = self
   
   def LogException(self,exceptionMessage):
       self._logger.critical(exceptionMessage)

   def LogWarning(self,warningMessage):
       self._logger.critical(warningMessage)

   def LogSchedulerInformation(self,message):
       self._logger.critical(message)

   def LogSchedulerException(self,exceptionMessage):
       self._logger.critical(exceptionMessage)
       
# def main():
#     s = BinAppLogger()
#     print (s)

#     s = BinAppLogger.getAppLogger()
#     print (s)

#     s = BinAppLogger.getAppLogger()
#     print (s)

#     s.LogException("404 error")
#     s.LogWarning("Warning test")

# if __name__ == "__main__":
#     main()
