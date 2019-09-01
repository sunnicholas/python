import platform

def get_system_Platform():
    print('system and bit'.center(40, '-'))
    print(platform.architecture())
    print
    '\n' * 3

    print('system and deatial'.center(40, '-'))
    print(platform.platform())
    print
    '\n' * 3

    print('system'.center(40, '-'))
    print(platform.system())
    print
    '\n' * 3

    print("python Version".center(40, '-'))
    print(platform.python_version())
    print
    '\n' * 3


def myPlatform():
    sysstr = platform.system()
    if (sysstr == "Windows"):
        print("my platform is:" + "Windows platform".center(40, '-'))
    elif (sysstr == "Linux"):
        print("my platform is:" + "Linux platform".center(40, '-'))
    else:
        print("my platform is:" + "Others platform".center(40, '-'))


get_system_Platform()
myPlatform()
