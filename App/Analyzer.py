import joblib
import cv2
class Analyzer:
    def __init__(self,model_path) -> None:
        self.model = joblib.load(model_path)
        self.resize_dimension=(24,24)
    def getImageArray(self,image_path):
        image_array=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
        image_array=cv2.resize(image_array,self.resize_dimension)
        image_array=cv2.bitwise_not(image_array)
        temp_array=[]
        for i in image_array:
            for j in i:
                temp_array.append(j)
        return temp_array
    def predict(self,image_path):
        self.predicted = self.model.predict([self.getImageArray(image_path)])
        return self.predicted
    
    
if __name__ == "__main__":
    Model = Analyzer("../Model/SVM_Model.joblib")
    print(Model.predict("./Images/WorkingImage.png"))