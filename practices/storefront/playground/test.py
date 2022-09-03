from genericpath import isdir, isfile
import os


def print_file(q):
    file_list = []
    while len(q) > 0:
        p = q.pop()
        print(p)
        print(len(q))

        if os.path.exists(p):
            os.chdir(p)
            #print('Files for ' + p)
            if os.listdir() is not None:
                files = list(os.listdir())
                for file in sorted(files):
                    if os.path.isfile(file):
                        #print(os.path.join(p+'/'+file))
                        file_list.append(os.path.join(p+'/'+file))
                    elif os.path.isdir(file):
                        q.append(os.path.join(p+file))
                    else:
                        continue
    return file_list

