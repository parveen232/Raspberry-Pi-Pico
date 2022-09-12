import machine
import utime

sensor_pir = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)

def pir_handler(pin):
    utime.sleep_ms(100)
    if pin.value():
        print("ALARM! Motion Detected!")
        for i in range(50):
            led.toggle()
            utime.sleep_ms(100)

sensor_pir.irq(trigger = machine.Pin.IRQ_RISING, handler = pir_handler)