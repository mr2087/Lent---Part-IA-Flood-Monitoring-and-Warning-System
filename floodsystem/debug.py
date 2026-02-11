from datetime import datetime

class Debug:
    def __init__(self, log : str) -> None:
        self.log_file = log
        self.t = datetime.now()

    def warn(self, fsrc : str, *msgs) -> None:
        # potential to change behaviour later
        wt = ''.join([f"{str(self.t)} -- {fsrc} -- [WARNING]", *msgs])

        print(wt)
        with open(self.log_file, 'a') as lf:
            lf.write(''.join([wt, '\n']))

    def error(self, fsrc : str, error : Exception, *msgs) -> None:
        wt = ''.join([f"{str(self.t)} -- {fsrc} -- [FATAL|{str(error)}]", *msgs])

        with open(self.log_file, 'a') as lf:
            lf.write(''.join([wt, '\n']))
        raise error(wt)