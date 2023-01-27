import pickle
import json
import numpy as np
import joblib

__data_columns = None
__model = None
__data_columns1 = None
__model1 = None
__data_columns2 = None
__model2 = None

def get_estimated_Triage(Sexm,Injuryy,Mental,Painy,New_Saturation,Error_group,New_Age,New_SBP,New_DBP,New_HR,New_RR,New_BT,New_NRS_pain):
    try:
        Mental_index = __data_columns.index(Mental.lower())
        Error_group_index = __data_columns.index(Error_group.lower())
        New_Saturation_index =  __data_columns.index(New_Saturation.lower())
        New_Age_index = __data_columns.index(New_Age.lower())
        New_SBP_index = __data_columns.index(New_SBP.lower())
        New_DBP_index = __data_columns.index(New_DBP.lower())
        New_HR_index = __data_columns.index(New_HR.lower())
        New_RR_index = __data_columns.index(New_RR.lower())
        New_BT_index = __data_columns.index(New_BT.lower())
        New_NRS_pain_index = __data_columns.index(New_NRS_pain.lower())
    except:
        Mental_index = -1
        Error_group_index = -1
        New_Saturation_index = -1
        New_Age_index = -1
        New_SBP_index = -1
        New_DBP_index = -1
        New_HR_index = -1
        New_RR_index = -1
        New_BT_index = -1
        New_NRS_pain_index = -1
    
    x = np.zeros(len(__data_columns))
    
    x[0] = Sexm
    x[1] = Injuryy
    x[5] = Painy
    
    if Mental_index >= 0:
        x[Mental_index] = 1
    if Error_group_index >= 0:
        x[Error_group_index] = 1
    if New_Saturation_index >= 0:
        x[New_Saturation_index] = 1
    if New_Age_index >= 0:
        x[New_Age_index] = 1
    if New_SBP_index >= 0:
        x[New_SBP_index] = 1
    if New_DBP_index >= 0:
        x[New_DBP_index] = 1
    if New_HR_index >= 0:
        x[New_HR_index] = 1
    if New_RR_index >= 0:
        x[New_RR_index] = 1
    if New_BT_index >= 0:
        x[New_BT_index] = 1
    if New_NRS_pain_index >= 0:
        x[New_NRS_pain_index] = 1

    return __model.predict([x])[0]

def get_estimated_Disposition(Sexm,Injuryy,Mental,Painy,New_Saturation,KTAS_expert,Error_group,New_Age,New_SBP,New_DBP,New_HR,New_RR,New_BT,New_NRS_pain):
    try:
        Mental_index = __data_columns1.index(Mental.lower())
        New_Saturation_index =  __data_columns1.index(New_Saturation.lower())
        KTAS_expert_index = __data_columns1.index(KTAS_expert.lower())
        Error_group_index = __data_columns1.index(Error_group.lower())
        New_Age_index = __data_columns1.index(New_Age.lower())
        New_SBP_index = __data_columns1.index(New_SBP.lower())
        New_DBP_index = __data_columns1.index(New_DBP.lower())
        New_HR_index = __data_columns1.index(New_HR.lower())
        New_RR_index = __data_columns1.index(New_RR.lower())
        New_BT_index = __data_columns1.index(New_BT.lower())
        New_NRS_pain_index = __data_columns1.index(New_NRS_pain.lower())
    except:
        Mental_index = -1
        New_Saturation_index = -1
        KTAS_expert_index = -1
        Error_group_index = -1
        New_Age_index = -1
        New_SBP_index = -1
        New_DBP_index = -1
        New_HR_index = -1
        New_RR_index = -1
        New_BT_index = -1
        New_NRS_pain_index = -1
    
    x = np.zeros(len(__data_columns1))
    
    x[0] = Sexm
    x[1] = Injuryy
    x[5] = Painy
    
    if Mental_index >= 0:
        x[Mental_index] = 1
    if New_Saturation_index >= 0:
        x[New_Saturation_index] = 1
    if KTAS_expert_index >= 0:
        x[KTAS_expert_index] = 1
    if Error_group_index >= 0:
        x[Error_group_index] = 1
    if New_Age_index >= 0:
        x[New_Age_index] = 1
    if New_SBP_index >= 0:
        x[New_SBP_index] = 1
    if New_DBP_index >= 0:
        x[New_DBP_index] = 1
    if New_HR_index >= 0:
        x[New_HR_index] = 1
    if New_RR_index >= 0:
        x[New_RR_index] = 1
    if New_BT_index >= 0:
        x[New_BT_index] = 1
    if New_NRS_pain_index >= 0:
        x[New_NRS_pain_index] = 1

    return __model1.predict([x])[0]


def get_estimated_New_Length_of_stay_min_expert(Sexm,Injuryy,Mental,Painy,New_Saturation,Disposition,KTAS_expert,Error_group,New_Age,New_SBP,New_DBP,New_HR,New_RR,New_BT,New_NRS_pain):
    try:
        Mental_index = __data_columns2.index(Mental.lower())
        New_Saturation_index =  __data_columns2.index(New_Saturation.lower())
        Disposition_index =  __data_columns2.index(Disposition.lower())
        KTAS_expert_index = __data_columns2.index(KTAS_expert.lower())
        Error_group_index = __data_columns2.index(Error_group.lower())
        New_Age_index = __data_columns2.index(New_Age.lower())
        New_SBP_index = __data_columns2.index(New_SBP.lower())
        New_DBP_index = __data_columns2.index(New_DBP.lower())
        New_HR_index = __data_columns2.index(New_HR.lower())
        New_RR_index = __data_columns2.index(New_RR.lower())
        New_BT_index = __data_columns2.index(New_BT.lower())
        New_NRS_pain_index = __data_columns2.index(New_NRS_pain.lower())
    except:
        Mental_index = -1
        New_Saturation_index = -1        
        Disposition_index = -1
        KTAS_expert_index = -1
        Error_group_index = -1
        New_Age_index = -1
        New_SBP_index = -1
        New_DBP_index = -1
        New_HR_index = -1
        New_RR_index = -1
        New_BT_index = -1
        New_NRS_pain_index = -1
    
    x = np.zeros(len(__data_columns2))
    
    x[0] = Sexm
    x[1] = Injuryy
    x[5] = Painy
    
    if Mental_index >= 0:
        x[Mental_index] = 1
    if New_Saturation_index >= 0:
        x[New_Saturation_index] = 1
    if Disposition_index >= 0:
        x[Disposition_index] = 1
    if KTAS_expert_index >= 0:
        x[KTAS_expert_index] = 1
    if Error_group_index >= 0:
        x[Error_group_index] = 1
    if New_Age_index >= 0:
        x[New_Age_index] = 1
    if New_SBP_index >= 0:
        x[New_SBP_index] = 1
    if New_DBP_index >= 0:
        x[New_DBP_index] = 1
    if New_HR_index >= 0:
        x[New_HR_index] = 1
    if New_RR_index >= 0:
        x[New_RR_index] = 1
    if New_BT_index >= 0:
        x[New_BT_index] = 1
    if New_NRS_pain_index >= 0:
        x[New_NRS_pain_index] = 1

    return __model2.predict([x])[0]



def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    if __model is None:
        with open('./artifacts/triage.pkl', 'rb') as f:
            __model = pickle.load(f)
            
    global  __data_columns1
    with open("./artifacts/columns1.json", "r") as f:
        __data_columns1 = json.load(f)['data_columns']

    global __model1
    if __model1 is None:
        with open('./artifacts/Diposition.pkl', 'rb') as f:
            __model1 = pickle.load(f)
            
    global  __data_columns2
    with open("./artifacts/columns2.json", "r") as f:
        __data_columns2 = json.load(f)['data_columns']

    global __model2
    if __model2 is None:
        with open('./artifacts/New_Length_of_stay_min.pkl', 'rb') as f:
            __model2 = pickle.load(f)
    print("loading saved artifacts...done")


def get_data_columns():
    return __data_columns

def ValuePredictorKidney(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        loaded_model = joblib.load(r'.\artifacts\kidney_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]

def ValuePredictorHeart(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        loaded_model = joblib.load(r'.\artifacts\heart_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]

if __name__ == '__main__':
    load_saved_artifacts()


