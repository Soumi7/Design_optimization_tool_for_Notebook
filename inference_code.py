fan_orientation = input("Enter fan orientation, Hub facing D cover or Hub facing C cover")

if fan_orientation == "Hub Facing D cover":
    unit_of_measure = input("Enter unit of measure, options : Metric and English")

    if unit_of_measure == "Metric":
        print("Enter pogo specifications next :")
        system_weight = double(input("Enter system weight"))

        base_thickness = double(input("Enter basethickness"))

        if system_weight<1.5 and base_thickness<10:
            pogo_spec = 45
        elif system_weight<1.5 and base_thickness>10:
            pogo_spec = 45
        elif system_weight>1.5 and base_thickness<10:
            pogo_spec = 60
        else:
            pogo_spec = 60

        
        print("Select system design parameters next :")

        dcm_dict = {
            "Magnesium" : 1,
            "Alumunium" : 1.4,
            "AL+B4C" : 1.9,
            "CFRP" : 3.5,
            "PC ABS" : 0.06,
        }

        PD_dict = {
        "10":1,
        "15":1.0825,
        "20":1.165,
        "25":1.2475,
        "30": 1.33,
        "35":1.4125,
        "40":1.495,
        "45":1.5775,
        "50" :1.66,
        }
        
        DCT_dict = {
            
"0.5": 0.74,
"0.6": 1,
"0.7":1.35,
"0.8":1.82,
"0.9":2.46,
"1":3.3,
"1.1":4.4,
"1.2":5.8,
"1.3":7.83,
"1.4":9.8,
}

AG1_dict = {
"0.3":0.44,
"0.35":0.476,
"0.4":0.5,
"0.45":0.55,
"0.5":0.58,
"0.55":0.64,
"0.6":0.68,
"0.65":0.743,
"0.7":0.79,
"0.75":0.86,
"0.8":0.92,
"0.85":1,
"0.9":1.08,
"0.95":1.16,
"1":1.25,
"1.05":1.34,
"1.1":1.42,
"1.15":1.56,
"1.2":1.68,
"1.25":1.81,
"1.3":1.9,
"1.35":2.09,
"1.4":2.2,
"1.45":2.3,
"1.5":2.4,
"1.55":2.6,
"1.6":2.89,
"1.65":3.12,
"1.7":3.37,
"1.75":3.6,
"1.8":3.8,
"1.85":4.1,
"1.9":4.5,
"1.95":4.8,
"2":5.2,
"2.05":5.7,
}

FS_dict = {






            
        }
GE_dict = {



        }    
FGP_dict = {         
"Pinhole":1,
"Clean D":1.72,
"Jailbar":0.72,
}

default = 10.5

dcm = dcm_dict[double(input("Enter D cover material"))]
        

Pogo_output = default*dcm*dct


