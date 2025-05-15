# prediction.py

import pickle
import numpy as np

# تحميل النموذج
with open("random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

# تحميل ترتيب الخصائص
with open("C:/Users/HPPPP/Desktop/water_quality_app/feature_order.pkl", "rb") as f:
    feature_order = pickle.load(f)

def predict_water_safety(input_data_dict):
    """
    input_data_dict: dict فيه المفاتيح هي أسماء الأعمدة والقيم هي القيم المدخلة.
    
    example:
    {
        "aluminium": 1.5,
        "ammonia": 10.2,
        ...
    }
    """

    # التأكد أن الترتيب مطابق
    input_ordered = [input_data_dict[feature] for feature in feature_order]

    # تحويل إلى مصفوفة numpy (2D)
    input_array = np.array(input_ordered).reshape(1, -1)

    # التنبؤ
    prediction = model.predict(input_array)[0]

    return prediction  # 0 or 1
