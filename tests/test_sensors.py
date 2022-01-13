import struct

from pyroombaadapter import PyRoombaAdapter, PacketType
import time

if __name__ == '__main__':
    roomba = PyRoombaAdapter("/dev/ttyS0", bau_rate=115200)
    # roomba.change_mode_to_safe()
    roomba.move(0,0)

    for _ in range(3):
        try:
            result = roomba.request_sensor_data([PacketType.BUMP_AND_WHEEL_DROP, PacketType.REQ_VELOCITY], debug=True)
            print(result)
        except Exception as e:
            print(e)
        time.sleep(1)
