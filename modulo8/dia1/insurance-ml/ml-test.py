import joblib
import numpy as np

# Cargar el modelo y los escaladores
loaded_model = joblib.load('./model/model.pkl')
loaded_scaler_x = joblib.load('./model/scaler_x.pkl')
loaded_scaler_y = joblib.load('./model/scaler_y.pkl')

print('Model and scalers loaded successfully.')

def predict_charges(smoker, age, bmi):
    """
    Predice los cargos de seguro para nuevos valores.

    Args:
        smoker (int): 0 for 'no' smoker, 1 for 'yes' smoker.
        age (int): Age of the individual.
        bmi (float): BMI of the individual.

    Returns:
        float: Predicted insurance charges.
    """
    # Prepare the input features as a 2D array
    new_data = np.array([[smoker, age, bmi]])

    # Scale the new data using the loaded scaler_x
    scaled_new_data = loaded_scaler_x.transform(new_data)

    # Make a prediction using the loaded model
    scaled_prediction = loaded_model.predict(scaled_new_data)

    # Inverse transform the prediction to get the actual charges
    prediction = loaded_scaler_y.inverse_transform(scaled_prediction)

    return prediction[0][0]

# Ejemplo de uso:
# Supongamos un no fumador de 30 años con un IMC de 25
new_smoker = 0  # no smoker
new_age = 30
new_bmi = 25.0
predicted_charge = predict_charges(new_smoker, new_age, new_bmi)
print(f'Predicted insurance charge for a non-smoker, 30 years old, with BMI 25: {predicted_charge:.2f}')

# Supongamos un fumador de 40 años con un IMC de 35
new_smoker_2 = 1  # smoker
new_age_2 = 40
new_bmi_2 = 35.0
predicted_charge_2 = predict_charges(new_smoker_2, new_age_2, new_bmi_2)
print(f'Predicted insurance charge for a smoker, 40 years old, with BMI 35: {predicted_charge_2:.2f}')
#print("\n")
print("Ingrese Datos de Nuevo Paciente")
new_smokerP =int(input("Ingrese si es fumador (1) o No fumador (0):"))
new_ageP =int(input("Ingrese edad en valor entero:"))
new_bmiP =float(input("Ingrese valor de BMI en valor decimal:"))
predicted_chargeP = predict_charges(new_smokerP, new_ageP, new_bmiP)
sfum = "Fumador" if  new_smokerP==1 else "No Fumador"
print(f'Cargo de Seguro predicho para un {sfum} , con {new_ageP} años, y con BMI de {new_bmiP}: {predicted_chargeP:.2f}')
