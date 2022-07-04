import time
import os
from typing import Any

from PIL import Image as PILImage
from PIL.Image import Image
from cv2 import cvtColor, imencode, COLOR_BGR2RGB
from yolov5.models.common import Detections

from app.lib.detector.models import YoloV5ModelSingleton
from app.lib.processes.imageProcedures import decodeDataImage, encodeDataImage

from app.lib.files.directories import createDirectory
from app.lib.files.files import OUTPUT_FOLDER

CURRENT_DIR = os.path.join(os.getcwd(), 'yolov5s_helmet.pt')


def predict(files: list[dict[str, str]], statistics=False) -> bool | tuple[list[dict[str, Any]], dict[str, float]] | \
                                                              list[dict[str, Any]]:
    # model: Model = torch.hub.load('yolov5', 'custom', source='local',
    #                               path='yolov5s_helmet.pt')
    #
    # model.classes = [1]
    model = YoloV5ModelSingleton()
    model.loadModel()

    imgs: list[Image] = []
    results: Detections = []

    print('Load images...', end=' ')
    start = time.time()
    try:
        imgs = [PILImage.open(f['filepath']) for f in files]
    except Exception as e:
        print(e)
        return False
    loadingTime = time.time() - start
    print(f'Load in time: {loadingTime:.2f}s')

    print('Predict...', end=' ')
    start = time.time()
    try:
        # results = model(imgs)
        results = model.detect(imgs)
    except Exception as e:
        print(e)
        return False
    predictTime = time.time() - start
    print(f'Predict in time: {predictTime:.2f}s')

    print('Render...', end=' ')
    start = time.time()
    try:
        results.render()
    except Exception as e:
        print(e)
        return False
    renderTime = time.time() - start
    print(f'Render in time: {renderTime:.2f}s')

    print('Save...')
    start = time.time()

    try:
        createDirectory(OUTPUT_FOLDER, deleteContent=True)
        results.save(save_dir=OUTPUT_FOLDER)
    except Exception as e:
        print(e)
        return False
    saveTime = time.time() - start
    print(f'Save in time: {saveTime:.2f}s')

    dictResults = [xyxy.to_dict(orient='records')
                   for xyxy in results.pandas().xyxy]

    result = [{'filename': filename, 'detections': dictResult}
              for filename, dictResult in zip(results.files, dictResults)]

    if statistics:
        return result, {'loadingTime': loadingTime, 'predictTime': predictTime, 'renderTime': renderTime,
                        'saveTime': saveTime}

    return result


def predictRealTime(dataImage, iddle: bool = True):
    model = YoloV5ModelSingleton()

    if iddle:
        img = decodeDataImage(dataImage)

        if img is None:
            yield None, True

        # Detect procces
        predicts = model.detect(img)
        predicts.render()

        numDetections = len(predicts.pandas().xyxy[0].to_dict(orient='records'))
        imgPredicted = predicts.imgs[0]

        # To gray scale
        frame = cvtColor(imgPredicted, COLOR_BGR2RGB)
        (flag, imgCode) = imencode('.jpg', frame)

        if not flag:
            yield None, True
        # if not flag:
        #     continue

        # Return enconded image and flag to proccess next image
        yield encodeDataImage(imgCode), numDetections, True
