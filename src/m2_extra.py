import rosebot
import time
def go_and_get_some_water(speed):
    robot=rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    robot.sound_system.speech_maker.speak("Are you thirsty now").wait()
    while True:
        if robot.sensor_system.touch_sensor.is_pressed():
            robot.drive_system.spin_clockwise_until_sees_object(speed,1600)
            robot.drive_system.go_forward_until_distance_is_less_than(0.1,speed)
            break
    robot.arm_and_claw.move_arm_to_position(3000)

def stop_and_ask():
    robot=rosebot.RoseBot()
    robot.sound_system.speech_maker.speak("Oh you don't want water").wait()
    while True:
        if robot.sensor_system.touch_sensor.is_pressed():
            break
    robot.drive_system.stop()
    robot.arm_and_claw.lower_arm()
    robot.sound_system.speech_maker.speak("Call me if you are thirsty").wait()

def go_back_and_give_me_the_water(speed):
    robot=rosebot.RoseBot()
    robot.sound_system.speech_maker.speak("Now I get the water").wait()
    while True:
        robot.drive_system.right(speed,speed)
        if robot.sensor_system.color_sensor.get_reflected_light_intensity()<=20:
            robot.drive_system.stop()
            break
    robot.arm_and_claw.lower_arm()
    robot.sound_system.speech_maker.speak("Now you can enjoy your water").wait()







