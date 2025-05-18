import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import joblib
import mlflow

# Veri setini yükle
data = pd.read_csv('data.csv')

# X ve y’yi tanımla
X = data[['TV', 'Radio', 'Newspaper']]
y = data['Sales']

# Eğitim-test olarak böl
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# MLflow çalıştır
mlflow.start_run()

# Modeli eğit
model = LinearRegression()
model.fit(X_train, y_train)

# Tahmin yap
predictions = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, predictions))

# MLflow’a metrik kaydet
mlflow.log_metric('RMSE', rmse)
mlflow.sklearn.log_model(model, "model")

# Modeli kaydet
joblib.dump(model, 'model.pkl')

# MLflow sonlandır
mlflow.end_run()

print("Model başarıyla eğitildi, RMSE:", rmse)
