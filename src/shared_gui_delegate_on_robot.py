"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Hanrui Chen, Shixin Yan, and Weizhou Liu.
  Winter term, 2018-2019.
"""
import m2_extra

class Receiver(object):
    def __init__(self,robot):
        """ :type robot: rosebot.Rosebot"""
        self.robot = robot
        self.is_time_to_stop = False

######################Movement Dynamics############################
    def forward(self, left_wheel_speed, right_wheel_speed):
        print("Got forward", left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))

    def stop(self):
        print("Stop")
        self.robot.drive_system.stop()

    def backward(self, left_wheel_speed, right_wheel_speed):
        print("Backward", left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.back(int(left_wheel_speed), int(right_wheel_speed))

    def left(self, left_wheel_speed, right_wheel_speed):
        print("Turn Left", left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.left(int(left_wheel_speed), int(right_wheel_speed))

    def right(self, left_wheel_speed, right_wheel_speed):
        print("Turn Right", left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.right(int(left_wheel_speed), int(right_wheel_speed))

    def GSFS(self, time, speed):
        print("Go straight for seconds:", time, speed)
        self.robot.drive_system.go_straight_for_seconds(int(time), int(speed))

    def GSFIUT(self, distance, speed):
        print("Go straight for inches using time:", distance, speed)
        self.robot.drive_system.go_straight_for_inches_using_time(int(distance), int(speed))

    def GSFIUE(self, distance, speed):
        print("Go straight for inches using encoder", distance, speed)
        self.robot.drive_system.go_straight_for_inches_using_encoder(int(distance), int(speed))

##########################Color sensors###############################

    def stop_by_less_intensity(self, intensity, speed):
        print("Move to less intensity", intensity, speed)
        self.robot.drive_system.go_straight_until_intensity_is_less_than(int(intensity), int(speed))

    def stop_by_more_intensity(self, intensity, speed):
        print("Move to more intensity", intensity, speed)
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(int(intensity), int(speed))

    def go_until_color_is(self, color, speed):
        print("Move to color", color, speed)
        self.robot.drive_system.go_straight_until_color_is(color, int(speed))

    def go_until_color_is_not(self, color, speed):
        print("Move to not that color", color, speed)
        self.robot.drive_system.go_straight_until_color_is_not(color, int(speed))

###########################Arm dynamics################################

    def raise_arm(self):
        print("Raise")
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        print("Lower")
        self.robot.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        print("Calibrate")
        self.robot.arm_and_claw.calibrate_arm()

    def move_arm_to_position(self, position):
        print("Move to position", position)
        self.robot.arm_and_claw.move_arm_to_position(int(position))


#########################IR sensor#####################################

    def move_forward_by_Ir(self, distance, speed):
        print("Move forward until distance is less than", distance)
        self.robot.drive_system.go_forward_until_distance_is_less_than(int(distance), int(speed))

    def beep_and_closer(self, distance, speed, init_pace, rate_of_pace):
        print("Beep and closer", distance, speed, init_pace, rate_of_pace)
        self.robot.drive_system.beep_and_closer(int(distance), int(speed), int(init_pace), int(rate_of_pace))

    def tone_and_closer(self, distance, speed, init_frequency, rate_of_frequency):
        print("Tone and closer", distance, speed, init_frequency, rate_of_frequency)
        self.robot.drive_system.tone_and_closer(int(distance), int(speed), int(init_frequency), int(rate_of_frequency))

    def LED_and_closer(self, distance, speed, init_led_frequency, rate_of_led_frequency):
        print("LED and closer", distance, speed, init_led_frequency, rate_of_led_frequency)
        self.robot.drive_system.LED_and_closer(int(distance), int(speed), int(init_led_frequency), int(rate_of_led_frequency))

#########################Sound system##################################

    def beep(self, n):
        print("Beeping")
        for _ in range(int(n)):
            self.robot.sound_system.beeper.beep().wait()

    def tone(self, fre, dui):
        print("Tones")
        self.robot.sound_system.tone_maker.play_tone(int(fre), int(dui))

    def speaker(self, phs):
        print("Speaking")
        self.robot.sound_system.speech_maker.speak(str(phs))

#########################Quit system###################################

    def quit(self):
        print('Now quit')
        self.is_time_to_stop = True

#######################################################################
    def data(self):
        print('Data')
        self.robot.drive_system.display_camera_data()

    def clock(self,speed, area):
        print('Spin clockwise')
        self.robot.drive_system.spin_clockwise_until_sees_object(int(speed),int(area))

    def counterclock(self,speed,area):
        print('Spin counterclockwise')
        self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed),int(area))


    def go_and_get_some_water(self,speed):
        print("Find water")
        m2_extra.go_and_get_some_water(int(speed))

    def stop_and_ask(self):
        print("Stop and wait")
        m2_extra.stop_and_ask()

    def go_back_and_give_me_the_water(self,speed):
        print("Return")
        m2_extra.go_back_and_give_me_the_water(int(speed))


