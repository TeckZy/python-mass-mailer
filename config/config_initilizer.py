class ConfigInitilizer():
    def __init__(self,mode):
        self._mode = mode

    def detectOs(self):
        import os
        print(os.uname())
        '''
        Detect The Operating Sytstem using os Module of python
        '''
        # pass
    def hasConfig(self):
        '''
        Checks For Config File in The same Directory
        '''

