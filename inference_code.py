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

        }

        PD_dict = {}

        DCT_dict = {}

        FS_dict = {}

        AG1_dict = {}

        GE_dict = {}    

        FGP_dict = {}

        default = 10.5

        dcm = dcm_dict[double(input("Enter D cover material"))]
        

        pogo_output = default*dcm*dct


