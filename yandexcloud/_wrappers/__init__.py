from yandexcloud._wrappers.dataproc import Dataproc, InitializationAction


class Wrappers(object):
    def __init__(self, sdk):
        self.Dataproc = Dataproc
        self.Dataproc.sdk = sdk
        self.InitializationAction = InitializationAction
