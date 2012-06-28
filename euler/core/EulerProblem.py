import inspect
import datetime
from math import sqrt

__author__ = 'cvw'

class EulerProblem() :

    def run(self):
        for method_name, method_obj in inspect.getmembers(self, predicate=inspect.ismethod):
            if method_name.startswith("solution"):
                print "---------------------"
                print ("running: %s.%s()"% (self.__class__, method_name))
                start_time_stamp = datetime.datetime.now()
                answer = method_obj()
                end_time_stamp = datetime.datetime.now()
                print "   ANSWER:%s "%answer
                print "   elapsed time=%s microseconds"%(end_time_stamp-start_time_stamp).microseconds
                print "   elapsed time=%s seconds"%(end_time_stamp-start_time_stamp).seconds
                print ""
                print ""
        pass

