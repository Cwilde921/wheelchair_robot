import mpu6050 from mpu6050

mpu = mpu6050()

print(mpu.get_accel_data())
