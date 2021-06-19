#coding=utf-8
import platform
bit=platform.architecture()[0]
if bit=='32bit':
    import arm
    arm.main()
else:
    import aarch
    aarch.main()
