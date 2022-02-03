import sys

class lazyimport:

    def __getattribute__(self, attr):
        callee_globals = sys._getframe().f_back.f_globals
        for key, value in callee_globals.items():
            if value is self:
                self_name = key
                break
        else:
            raise ImportError("Lazyimport should be used at module toplevel and  bound to a single name")
        # Known issue: code in module is executed twice, as "fileone" is not finished running at this point:
        target = __import__(self_name)
        callee_globals[self_name] = target
        return getattr(target, attr)


#def lazyimport(): pass
