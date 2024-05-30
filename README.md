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




Wykresy:  
![image](https://github.com/kacpermisiek/ml-projekt/assets/56176866/8eedccbe-aaad-4804-a679-f8442f243ce1)

# Czas treningu: ~90 minut
## GPU: Testla P100


Zauważono, że skuteczność jest bardzo wysoka już na 3 epoce, dalsze epoki nie wnoszą już przyrostu skuteczności, 
więc zbudowano jeszcze raz model, tym razem dla 3 epok (reszta parametrów bez zmian)  - pozostałe hiperparametry nie uległy zmianie

Czas treningu: 60 minut
Train accuracy: 0.997
Test accuracy: 0.992
Valid accuracy: 0.998


Classification report:
```
              precision    recall  f1-score   support

           0       0.99      1.00      1.00       700
           1       0.99      0.99      0.99       700
           2       0.98      0.99      0.98       700
           3       1.00      0.99      0.99       700
           4       0.99      1.00      1.00       700
           5       1.00      0.98      0.99       700

    accuracy                           0.99      4200
   macro avg       0.99      0.99      0.99      4200
weighted avg       0.99      0.99      0.99      4200
```


## Macierze błędu:  
### Valid set:  
![image](https://github.com/kacpermisiek/ml-projekt/assets/56176866/3c035d1b-8c04-40dc-9d18-be70775b8a20)

### Test set:  
![image](https://github.com/kacpermisiek/ml-projekt/assets/56176866/9f453abb-e9fa-4ff1-9926-ca42938b4777)


## Złe predykcje ze zbioru testowego:
![image](https://github.com/kacpermisiek/ml-projekt/assets/56176866/3eec6a1e-bea4-4d0f-b6f5-9bf2319f9bda)

### Jak widać model ma problemy ze znakami odwołującymi znak.








