import wpilib
#!/usr/bin/env python3
"""
	This is a good foundation to build your robot code on
"""

import wpilib

class MyRobot(wpilib.IterativeRobot):

	def robotInit(self):
		"""
		This function is called upon program startup and
		should be used for any initialization code.
		"""
		self.shootbot = wpilib.Jaguar(4)
		self.spiderbot = wpilib.Jaguar(5)
		self.spiderbot1 = wpilib.Jaguar(6)
		self.robot_drive = wpilib.RobotDrive(0,3)
		self.stick = wpilib.Joystick(1)
		self.brazito = wpilib.Jaguar(7)

	def autonomousInit(self):
		"""This function is run once each time the robot enters autonomous mode."""
		self.auto_loop_counter = 0

	def autonomousPeriodic(self):
		"""This function is called periodically during autonomous."""

		# Check if we've completed 100 loops (approximately 2 seconds)
		if self.auto_loop_counter < 100:
			self.robot_drive.drive(-0.5, 0) # Drive forwards at half speed
			self.auto_loop_counter += 1
		elif self.auto_loop_counter  < 200:
			self.robot_drive.drive(1,1)
			self.auto_loop_counter += 1
		elif self.auto_loop_counter < 300:
			self.robot_drive.drive(-0.5, 0) # Drive forwards at half speed
			self.auto_loop_counter += 1
		elif self.auto_loop_counter  < 400:
			self.robot_drive.drive(1,1)
			self.auto_loop_counter += 1
		elif self.auto_loop_counter < 500:
			self.robot_drive.drive(-0.5, 0) # Drive forwards at half speed
			self.auto_loop_counter += 1
		elif self.auto_loop_counter  < 600:
			self.robot_drive.drive(1,1)
			self.auto_loop_counter += 1
		elif self.auto_loop_counter < 700:
			self.robot_drive.drive(-0.5, 0) # Drive forwards at half speed
			self.auto_loop_counter += 1
		elif self.auto_loop_counter  < 800:
			self.robot_drive.drive(1,1)
			self.auto_loop_counter += 1
		else:
			self.robot_drive.drive(0, 0)    #Stop robot

	def teleopPeriodic(self):
		a_is_pressed = self.stick.getButton(0)
		b_is_pressed = self.stick.getButton(1)
		rb_is_pressed = self.stick.getButton(5)

		
		self.robot_drive.arcadeDrive(self.stick)

	def testPeriodic(self):
		"""This function is called periodically during test mode."""
		wpilib.LiveWindow.run()

if __name__ == "__main__":
	wpilib.run(MyRobot)
