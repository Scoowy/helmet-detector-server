import yolov5
from yolov5.models.common import Detections
from yolov5.models.yolo import Model


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


class YoloV5ModelSingleton(metaclass=SingletonMeta):

    def __init__(self):
        self.model: Model = None

    def loadModel(self):
        if self.model is None:
            # self.model: Model = torch.hub.load('app/lib/yolov5', 'custom', source='local', path='yolov5s_helmet.pt')
            self.model = yolov5.load('yolov5s_helmet.pt')
            self.model.classes = [1]

        return self.model

    def detect(self, imgs):
        results: Detections = []
        if self.model is not None:
            results = self.model(imgs)

        return results
