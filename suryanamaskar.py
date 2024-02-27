from calcangle import calculateAngle
import mediapipe as mp
mp_pose = mp.solutions.pose

def evaluate_surya_namaskar_pose(landmarks):
    suggestions = [] # Store suggestions for improvement

    # Define the Stage enum (you should define this enum based on your needs)
    class Stage:
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5
        six = 6
        seven = 7

    # Add the code for evaluating the posture based on your provided logic.

    # Calculate angles and evaluate the posture
    left_elbow_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value])

    right_elbow_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value])

    left_shoulder_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value])

    right_shoulder_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                         landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                         landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value])

    left_knee_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value])

    right_knee_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value])

    left_hip_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.NOSE.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value])

    right_hip_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.NOSE.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value])

    left_hip_s_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value])

    right_hip_s_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value])
    
    standing_left_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value])

    standing_right_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value])
    print(left_knee_angle)
    print(left_hip_s_angle)
    print(landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][1])
    print(landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value][1])
    print(landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value][1])
    print(landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value][1])
    
    
    # Add your logic to determine the stage of the Surya Namaskar pose
    pose_stage = None
    
    #for pose 1
    if ((pose_stage == None) and (standing_left_angle >= 150 and left_elbow_angle <= 190) and
        (landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value][1]> landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value][1]) and 
        (landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value][1]> landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value][1]) and (left_knee_angle >=150 )):
        pose_stage = Stage.one
    
    #for pose 2
    elif ((pose_stage == None) and (left_elbow_angle >= 135 and right_elbow_angle >= 135) and
        (left_elbow_angle <= 180 and right_elbow_angle <= 180) and (left_knee_angle >= 150 and right_knee_angle >= 150) and 
        ((landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value][0] < landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value][0]))):
        pose_stage = Stage.two
    
    #for pose 3 
    elif ((pose_stage == None) and (left_knee_angle > 130 and right_knee_angle > 130) and
        (left_hip_s_angle < 100 and right_hip_s_angle < 100)) and ((landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][1] < landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value][1]) and
            (landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value][1] < landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value][1])):
        pose_stage = Stage.three
    
    #for pose 4         
    elif((pose_stage == None) and (left_elbow_angle>160 and right_elbow_angle>160) and (left_shoulder_angle>25 and right_shoulder_angle>25) and (left_shoulder_angle<40 and right_shoulder_angle<40)) and (abs(landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value][0]-landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value][0])>0.40):
        pose_stage = Stage.four

    #for pose 5
    elif((pose_stage == None) and (left_knee_angle>160 and right_knee_angle>160) and (left_hip_s_angle<95 and right_hip_s_angle<95) and (left_hip_s_angle>=65 and right_hip_s_angle>=65)):
       if((landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][1]<landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value][1]) and (landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value][1]<landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value][1])):
            pose_stage = Stage.five
            
    #for pose 6
    elif((pose_stage == None) and (left_hip_s_angle>90 and right_hip_s_angle>90) and (left_hip_s_angle<150 and right_hip_s_angle<150) and (left_knee_angle>90 and right_knee_angle>90)):
      if(landmarks[mp_pose.PoseLandmark.NOSE.value][1]>landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value][1]):
        pose_stage = Stage.six
        
    #for pose 7
    elif((pose_stage == None) and (left_knee_angle>150 and right_knee_angle>150) and (left_hip_s_angle>120 and right_hip_s_angle>120)):
      if((landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value][1]>landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value][1]) and (landmarks[mp_pose.PoseLandmark.NOSE.value][1]<landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value][1])):
        pose_stage = Stage.seven
        
    else:
        print("Make sure you are performing surya namaskar asana")
        
    print("pose_stage------->",pose_stage)
    
    if pose_stage == Stage.one:
        t = 0
        if ((left_elbow_angle>= 55 and left_elbow_angle<=105) and (right_elbow_angle >=55 and right_elbow_angle<= 105)):
            t =t+1
        else:
            print("pls bring your hands towards body ")
            suggestions.append("pls bring your hands towards body ")
        if (standing_left_angle>= 160 and standing_left_angle<= 185) and (standing_right_angle>= 160 and standing_right_angle<= 185):
            t = t+1
        else:
            print("Pls stand straight")
            suggestions.append("Pls stand straight")
        if (left_knee_angle >=170 and left_knee_angle <= 185 and right_knee_angle >= 170 and right_knee_angle <= 185):
            t = t+1
        else:
                print("pls dont bend your knees")
                suggestions.append("pls dont your knees")
        if(landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value][1]> landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value][1] and landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value][1]> landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value][1]):
            t = t+1
        else:
            print("pls put your hands below your shoulder ")
            suggestions.append("pls put your hands below your shoulder ")
        if (landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value][1]-landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value][0]<=0.1):
            t = t+1
        else:
            print("pls put your hand together to make a NAMASKAR pose from hands")
            suggestions.append("pls put your hand together to make a NAMASKAR pose from hands")
        if t==5:
            print("you are doing great")
            suggestions.append("you are doing great")
        else:
            print("Please take a look at photo and get in right position")
            suggestions.append("Please take a look at photo and get in right position")
  
    elif pose_stage == Stage.two:
        t = 0
        if((left_elbow_angle>=140 and right_elbow_angle>=140) and (left_elbow_angle<=180 and right_elbow_angle<=180)):
            t = t+1
        else:
            print("please straighten your arms behind your head")
            suggestions.append("please straighten your arms behind your head")
        if( (left_knee_angle>=165 and right_knee_angle>=165)):
            t =t+1
        else:
            print("please don't bend your knees keep them straight")
            suggestions.append("please don't bend your knees keep them straight")
        if((landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value][0]>landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value][0]) or (landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value][0] >landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value][0])):
            t =t+1
        else:
            print("please keep your wrist straight and behind your foot")
            suggestions.append("please keep your wrist straight and behind your foot")
        if (landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value][0] < landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value][0] or landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value][0] > landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value][0]):
            t =t+1
        else:
            print("please push back your hands harder")
            suggestions.append("please push back your hands harder")

        if (landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][0]>=landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value][0] or landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value][0]>=landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value][0]):
            t = t+1
        else:
            print("please bend a bit more backwards ")
            suggestions.append("please bend a bit more backwards ")

        if t==5:
            # print("You are in right position ")
            suggestions.append("You are in right position ")
        else:
            print("Please take a look at photo and get in right position")
            suggestions.append("Please take a look at photo and get in right position")


    elif pose_stage == Stage.three:
        t =0
        if((left_knee_angle>157 and right_knee_angle>157)):
            t =t+1
        else:
            print("Please keep your leg straight and make your ankle touch ground")
            suggestions.append("Please keep your leg straight and make your ankle touch ground")
        if ((left_hip_s_angle<60 and right_hip_s_angle<60)) :
            t =t+1
        else:
            print("Bend yourself properly ")
            suggestions.append("Bend yourself properly ")
        if ((landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][1]<landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value][1]) and (landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value][1]<landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value][1])):
            t = t+1
        else:
            print("Your shoulder should be below your hips")
            suggestions.append("Your shoulder should be below your hips")
        if (landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value][1]<landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value][1] and landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][1]<landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value][1]):
            t =t+1
        else:
            print("please keep your waist down and in line with legs")
            suggestions.append("please keep your waist down and in line with legs")
        if ((landmarks[mp_pose.PoseLandmark.NOSE.value][1]>landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value][1]) and (landmarks[mp_pose.PoseLandmark.NOSE.value][1]>landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value][1])):
            t =t+1
        else:
            print("look down or keep your head down")
            suggestions.append("look down or keep your head down")
        if (landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value][1]<landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value][1] and landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value][1]<landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value][1]):
            t =t+1
        else:
            print("Your right knee should touch the ground ")
            suggestions.append("Your right knee should touch the ground ")

        if t==6:
            print("you are doing great")
            suggestions.append("you are doing great")
    
    elif pose_stage == Stage.four:
        t =0
        if((left_knee_angle>157 and right_knee_angle>157)):
            t =t+1
        else:
            print("Please keep your leg straight and make your ankle touch ground")
            suggestions.append("Please keep your leg straight and make your ankle touch ground")
        if ((left_hip_s_angle<60 and right_hip_s_angle<60)) :
            t =t+1
        else:
            print("Bend yourself properly ")
            suggestions.append("Bend yourself properly ")
        if ((landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][1]<landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value][1]) and (landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value][1]<landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value][1])):
            t = t+1
        else:
            print("Your shoulder should be below your hips")
            suggestions.append("Your shoulder should be below your hips")
        if (landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value][1]<landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value][1] and landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][1]<landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value][1]):
            t =t+1
        else:
            print("please keep your waist down and in line with legs")
            suggestions.append("please keep your waist down and in line with legs")
        if ((landmarks[mp_pose.PoseLandmark.NOSE.value][1]>landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value][1]) and (landmarks[mp_pose.PoseLandmark.NOSE.value][1]>landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value][1])):
            t =t+1
        else:
            print("look down or keep your head down")
            suggestions.append("look down or keep your head down")
        if (landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value][1]<landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value][1] and landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value][1]<landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value][1]):
            t =t+1
        else:
            print("Your right knee should touch the ground ")
            suggestions.append("Your right knee should touch the ground ")

        if t==6:
            print("you are doing great")
            suggestions.append("you are doing great")
    
    else:
        suggestions.append("Try to attempt the asana correctly it is not matching with any stage")
        

    return suggestions