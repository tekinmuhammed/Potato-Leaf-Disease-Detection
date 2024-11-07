# Potato-Leaf-Disease-Detection

## Potato Leaf Disease Classification Using Deep Learning Techniques

________________________________________
### Abstract: 
This study explores the application of deep learning techniques for the classification of potato leaf diseases. Utilizing convolutional neural networks (CNNs), we aim to accurately identify and categorize different stages of diseases in potato leaves, facilitating timely and effective agricultural interventions. The dataset comprises 4062 images categorized into three classes: Early Blight, Healthy, and Late Blight. Two models were developed and evaluated, including a custom CNN and a transfer learning model with InceptionV3. The results indicate that both models perform well, with the transfer learning model slightly outperforming the custom CNN.
Keywords: Potato leaf disease, Deep learning, Convolutional neural networks, Transfer learning, InceptionV3
________________________________________
### 1. Introduction
In this project, we aim to classify potato leaf diseases using deep learning techniques. By leveraging convolutional neural networks (CNNs), we can accurately identify and categorize different stages of disease in potato leaves, aiding in timely and effective agricultural interventions. Potato crops are highly susceptible to various diseases, which can significantly impact yield and quality. Early detection and accurate classification of these diseases are crucial for effective management and intervention.
________________________________________
### 2. Our Dataset
The dataset comprises 4062 images of potato leaves. Images are categorized into three classes: Early Blight, Healthy, and Late Blight. Each image is 256x256 pixels, ensuring uniformity for model training. The dataset was split into training, validation, and testing sets to facilitate model development and evaluation.
________________________________________
### 3. Classes
We classified the potato leaf images into three distinct categories:
** •	Early Blight: ** Characterized by dark spots with concentric rings on older leaves.
** •	Healthy: ** Leaves without any visible signs of disease.
** •	Late Blight: ** Symptoms include brown or black lesions on leaves, often accompanied by white fungal growth on the undersides.
________________________________________
### 4. Training the Model
We trained two models for this classification task:
** •	Model 1: Custom CNN ** A custom-built convolutional neural network trained for 25 epochs using augmented training data. Data augmentation techniques were applied to prevent overfitting. The model's architecture included several convolutional layers followed by max-pooling and dense layers for classification.
** •	Model 2: Transfer Learning with InceptionV3 ** Utilized the pre-trained InceptionV3 model, adding custom dense layers for classification. This model was also trained for 25 epochs with data augmentation. Transfer learning leverages the pre-trained weights of InceptionV3, which has been trained on a large dataset, to improve classification performance on our specific dataset.
________________________________________
### 5. Results
Both models were evaluated on the test dataset. The results are summarized as follows:
#### •	Model 1: Custom CNN
o	Test Accuracy: 91.15%
o	Classification Report:
	Early Blight: Precision: 0.41, Recall: 0.46, F1-Score: 0.44
	Healthy: Precision: 0.29, Recall: 0.27, F1-Score: 0.28
	Late Blight: Precision: 0.31, Recall: 0.28, F1-Score: 0.30
#### •	Model 2: Transfer Learning with InceptionV3
o	Test Accuracy: 90.89%
o	Classification Report:
	Early Blight: Precision: 0.44, Recall: 0.49, F1-Score: 0.47
	Healthy: Precision: 0.26, Recall: 0.21, F1-Score: 0.23
	Late Blight: Precision: 0.37, Recall: 0.38, F1-Score: 0.37
________________________________________

### 6. Conclusion
Both models demonstrated strong overall accuracy in classifying potato leaf diseases. The transfer learning model with InceptionV3 slightly outperformed the custom CNN in terms of precision and recall for Early Blight and Late Blight. The custom CNN had a marginally better test accuracy. Future improvements could involve refining data augmentation techniques and experimenting with different pre-trained models. This project highlights the potential of deep learning in agricultural disease management, enabling timely and precise intervention.
________________________________________
### REFERENCES
Rizwan Saeed. (2021, June 1).Potato Disease Leaf Dataset(PLD). Kaggle. https://www.kaggle.com/datasets/rizwan123456789/potato-disease-leaf-datasetpld

Ravi-Chan. (2022, March 16). How to download any data set from Kaggle. Medium. Retrieved May 18, 2024, from https://ravi-chan.medium.com/how-to-download-any-data-set-from-kaggle-7e2adc152d7f#c62

Ravi Ramaknishnan. (2023, September 21). Potato Plant Disease Detection. Medium. Retrieved June 30, 2024, from https://ravaldo07.medium.com/ ravi20076-data-set-from-kaggle-7e234914#2410
