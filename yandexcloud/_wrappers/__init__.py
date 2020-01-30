from yandexcloud._wrappers.dataproc import Dataproc


class Wrappers(object):
    def __init__(self, sdk):
        self.Dataproc = Dataproc
        self.Dataproc.sdk = sdk
