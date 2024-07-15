import pandas as pd
import os

input_path = r'D:\UMA_Dataset\UMAFall_Dataset\User1'
out_path1 = r'D:\UMA_Dataset\Accelerometer_Waist_User1'
out_path2 = r'D:\UMA_Dataset\Gyroscope_Waist_User1'
out_path3 = r'D:\UMA_Dataset\Magnetometer_Waist_User1'

os.makedirs(out_path1, exist_ok=True)
os.makedirs(out_path2, exist_ok=True)
os.makedirs(out_path3, exist_ok=True)

#檔名記得要改
#df = pd.read_csv(r'D:\UMA_Dataset\UMAFall_Dataset\User1\UMAFall_Subject_01_ADL_HandsUp_1_2017-04-14_23-32-44.csv')
#print(df.iloc[32,0].split(';'))



for i in range(0,len(os.listdir(path=input_path))):
    df = pd.read_csv(os.path.join(input_path , os.listdir(input_path)[i])) #去讀裡面其中的資料
    filtered_data = pd.DataFrame(columns=df.columns)

    #這是去抓資料裡面的第幾行
    for index in range(32, len(df)):
    #df.iloc[index,0].split(';')[6] 是做手部腰部的分類
    #df.iloc[index,0].split(';')[5] 是做感測器的分類
    #之後去判斷拆解說 這個split裡面是啥 去抓感測器和腰部一些分類
        if(df.iloc[index,0].split(';')[5] == '0' and df.iloc[index,0].split(';')[6] == '2'):
            data = {
            'TimeStamp': int(df.iloc[index, 0].split(';')[0]),  # 轉換為整數
            'Sample No': int(df.iloc[index, 0].split(';')[1]),  # 轉換為整數
            'X-Axis': float(df.iloc[index, 0].split(';')[2]),  # 轉換為浮點數
            'Y-Axis': float(df.iloc[index, 0].split(';')[3]),  # 轉換為浮點數
            'Z-Axis': float(df.iloc[index, 0].split(';')[4]),  # 轉換為浮點數
            'Sensor Type': int(df.iloc[index, 0].split(';')[5]),  # 轉換為整數
            'Sensor ID': int(df.iloc[index, 0].split(';')[6])   # 轉換為整數
            }
            #print(df.iloc[index, 0].split(';'))
            filtered_data = pd.concat([filtered_data, pd.DataFrame([data])], ignore_index=True)
            
    output_file = os.path.join(out_path1,'Accelerometer_waist'+str(i)+'.csv')            
    filtered_data.to_csv(output_file, index=False,sep=',')

for i in range(0,len(os.listdir(path=input_path))):
    df = pd.read_csv(os.path.join(input_path , os.listdir(input_path)[i])) #去讀裡面其中的資料
    filtered_data = pd.DataFrame(columns=df.columns)

    #這是去抓資料裡面的第幾行
    for index in range(32, len(df)):
    #df.iloc[index,0].split(';')[6] 是做手部腰部的分類
    #df.iloc[index,0].split(';')[5] 是做感測器的分類
    #之後去判斷拆解說 這個split裡面是啥 去抓感測器和腰部一些分類
        if(df.iloc[index,0].split(';')[5] == '1' and df.iloc[index,0].split(';')[6] == '2'):
            data = {
            'TimeStamp': int(df.iloc[index, 0].split(';')[0]),  # 轉換為整數
            'Sample No': int(df.iloc[index, 0].split(';')[1]),  # 轉換為整數
            'X-Axis': float(df.iloc[index, 0].split(';')[2]),  # 轉換為浮點數
            'Y-Axis': float(df.iloc[index, 0].split(';')[3]),  # 轉換為浮點數
            'Z-Axis': float(df.iloc[index, 0].split(';')[4]),  # 轉換為浮點數
            'Sensor Type': int(df.iloc[index, 0].split(';')[5]),  # 轉換為整數
            'Sensor ID': int(df.iloc[index, 0].split(';')[6])   # 轉換為整數
            }
            #print(df.iloc[index, 0].split(';'))
            filtered_data = pd.concat([filtered_data, pd.DataFrame([data])], ignore_index=True)
            
    output_file = os.path.join(out_path2,'Gyroscope_waist'+str(i)+'.csv')            
    filtered_data.to_csv(output_file, index=False,sep=',')

for i in range(0,len(os.listdir(path=input_path))):
    df = pd.read_csv(os.path.join(input_path , os.listdir(input_path)[i])) #去讀裡面其中的資料
    filtered_data = pd.DataFrame(columns=df.columns)

    #這是去抓資料裡面的第幾行
    for index in range(32, len(df)):
    #df.iloc[index,0].split(';')[6] 是做手部腰部的分類
    #df.iloc[index,0].split(';')[5] 是做感測器的分類
    #之後去判斷拆解說 這個split裡面是啥 去抓感測器和腰部一些分類
        if(df.iloc[index,0].split(';')[5] == '2' and df.iloc[index,0].split(';')[6] == '2'):
            data = {
            'TimeStamp': int(df.iloc[index, 0].split(';')[0]),  # 轉換為整數
            'Sample No': int(df.iloc[index, 0].split(';')[1]),  # 轉換為整數
            'X-Axis': float(df.iloc[index, 0].split(';')[2]),  # 轉換為浮點數
            'Y-Axis': float(df.iloc[index, 0].split(';')[3]),  # 轉換為浮點數
            'Z-Axis': float(df.iloc[index, 0].split(';')[4]),  # 轉換為浮點數
            'Sensor Type': int(df.iloc[index, 0].split(';')[5]),  # 轉換為整數
            'Sensor ID': int(df.iloc[index, 0].split(';')[6])   # 轉換為整數
            }
            #print(df.iloc[index, 0].split(';'))
            filtered_data = pd.concat([filtered_data, pd.DataFrame([data])], ignore_index=True)
            
    output_file = os.path.join(out_path3,'Magnetometer_waist'+str(i)+'.csv')            
    filtered_data.to_csv(output_file, index=False,sep=',')           

#df = pd.DataFrame([data])

# 指定要保存的 CSV 檔案名稱
#output_file也一定要改 不然會一直重複
#output_file = 'Accelerometer_wrist.csv'

# 將 DataFrame 存放到 CSV 檔案中
#filtered_data.to_csv(output_file, index=False,sep=',')
