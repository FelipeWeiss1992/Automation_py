import rpa as r
import pyautogui as p

r.init()

r.url('https://github.com/login')


r.wait(2.0)
r.type('//*[@name="login"]', 'felipeweiss92@gmail.com')
r.wait(2.0)
r.type('//*[@name="password"]', '*******[enter]')

r.wait(2.0)
      