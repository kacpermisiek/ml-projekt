# Wykorzystano model EfficentNetB3 z wagami inicjalizacyjnymi zbioru ImageNet

## Parametry:
lr - 0.0001  
epochs - 10  
batch_size - 32  
optimizer - Adam  
loss - sparse categorical crossentropy  
metrics - accuracy  

Wynik:
Wyniki ostatniej epoki:  
accuracy: 0.9991  
loss: 0.0057  
val_accuracy: 1.0000  


Test accuracy: 0.993%

Classification report:
```
              precision    recall  f1-score   support  
           0       1.00      0.98      0.99       100  
           1       1.00      1.00      1.00       100  
           2       1.00      0.98      0.99       100  
           3       1.00      1.00      1.00       100  
           4       0.98      1.00      0.99       100  
           5       0.98      1.00      0.99       100  
    accuracy                           0.99       600

   macro avg       0.99      0.99      0.99       600  
weighted avg       0.99      0.99      0.99       600  
```


Wykresy:
![image](https://github.com/kacpermisiek/ml-projekt/assets/56176866/8eedccbe-aaad-4804-a679-f8442f243ce1)


Macierze błędów:
Zbiór testowy:  
![image](https://github.com/kacpermisiek/ml-projekt/assets/56176866/47c32c10-e97a-4adc-95d9-a065eae21713)

  
Zbiór walidacyjny:
![image](https://github.com/kacpermisiek/ml-projekt/assets/56176866/7d553529-2c72-449e-be92-474010764d34)





# Czas treningu: ~90 minut
## GPU: Testla P100


Zauważono, że skuteczność jest bardzo wysoka już na 3 epoce, dalsze epoki nie wnoszą już przyrostu skuteczności, 
więc zbudowano jeszcze raz model, tym razem dla 3 epok (reszta parametrów bez zmian)
