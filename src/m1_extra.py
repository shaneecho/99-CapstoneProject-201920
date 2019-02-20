import rosebot
import time
def enter_pyramid(speed):
    robot=rosebot.RoseBot()
    robot.sound_system.speech_maker.speak("Ok, I gonna go into the dangerous pyramid!")
    robot.drive_system.go(speed,speed)
    while True:
        if robot.sensor_system.color_sensor.get_color() == "black":
            robot.drive_system.left(speed, speed)
            time.sleep(0.01)
            robot.drive_system.go(speed, speed)
        else:
            robot.drive_system.right(speed, speed)
            time.sleep(0.01)
            robot.drive_system.go(speed, speed)
        # if robot.sensor_system.color_sensor.get_color() == "black":
        #     robot.drive_system.left(speed,speed)
        #     time.sleep(0.1)
        #     robot.drive_system.go(speed,speed)
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()<2:
            break
    robot.drive_system.stop()
# def detect_danger():