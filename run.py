
import os
try:
 os.mkdir('result')
except:pass
if __name__ == "__main__":
        try:
                __import__("gassken").AORECGANTENG()
        except Exception as e:
                exit(str(e))
