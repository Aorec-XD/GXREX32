import os
try:
 os.mkdir('result')
except:pass
if __name__ == "__main__":
        try:
                __import__("gxrex").lisensi()
        except Exception as e:
                exit(str(e))
